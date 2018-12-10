import pylab as pl
import load_data
import numpy as np
import measure
import math
from fastdtw import fastdtw


def agnes_pre(data, k):
    num = data.shape[0]
    group = np.arange(0,num,1).reshape((num, 1))
    indexed_data = np.hstack((group, data))
    clusters = []
    for i in range(num):
        clusters.append(indexed_data[i])
    return agens(clusters, k, num)


def result_to_cluster(data, group, group_num):
    num = data.shape[0]
    data_index = np.arange(0, num, 1).reshape((num, 1))
    indexed_data = np.hstack((data_index, data))
    clusters = []
    for i in range(group_num):
        group_index = np.nonzero(group[:, 0] == i)
        if len(group_index[0]) > 0:
            group_current = indexed_data[group_index[0]]
            clusters.append(group_current)
    return clusters


def outer_agens(data, group, group_num, k):
    clusters = result_to_cluster(data, group, group_num)
    return agens(clusters, k, data.shape[0])


def agens(clusters, k, num):
    result = np.arange(num).reshape((num, 1))
    dist = update_distance(clusters)
    while len(clusters) > k:
        min_index = find_min(dist)
        x = min_index[0][0]
        y = min_index[1][0]
        clusters[x] = np.vstack((clusters[x], clusters[y]))
        clusters.pop(y)
        dist = update_distance(clusters)
    for i in range(k):
        group_array = clusters[i]
        print(group_array.shape)
        for j in range(group_array.shape[0]):
            o_index = group_array.item((j,0))
            result[int(o_index),:] = [i]
    return result


def distance(a, b):
    x = a.shape[1]
    a = a.reshape((x, 1))
    y = b.shape[1]
    b = b.reshape((y, 1))
    return np.sqrt(np.power(np.sum(a[:, 1:] - b[:, 1:]), 2))


def cluster_distance(a, b):
    num_a = a.shape[0]
    num_b = b.shape[0]
    dist = np.zeros((num_a, num_b))
    for i in range(num_a):
        for j in range(num_b):
            tmp_dist = distance(a[i:i+1, :], b[j:j+1, :])
            if tmp_dist != 0:
                dist[i][j] = tmp_dist
            else:
                dist[i][j] = np.inf
    return np.mean(dist)


def quick_cluster_distance(a, b):
    return fastdtw(a, b)


def update_distance(clusters):
    num = len(clusters)
    result = np.zeros((num, num))
    for i in range(num):
        for j in range(num):
            if i == j:
                result[i][j] = np.inf
            else:
                t_distance, path = quick_cluster_distance(clusters[i], clusters[j])
                result[i][j] = t_distance
    return result


def find_min(m):
    return np.where(m == np.min(m))


if __name__ == '__main__':
    # o_data = load_data.get_data(10)
    # (x, y) = o_data.shape
    # data = o_data[:, 0: y - 4]
    # group_result = agnes_pre(data, 4)
    # print(measure.measure_k_group(group_result, o_data[:, y - 4:y - 3], 4, 4))
    a = np.arange(9).reshape((3, 3))
    print(np.where(a == np.min(a))[1][0])

