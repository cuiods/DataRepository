import pylab as pl
import load_data
import numpy as np
import measure
import math


def agnes(data, k):
    num = data.shape[0]
    group = np.arange(num).reshape(num, 1)
    result = np.arange(num).reshape(num, 1)
    indexed_data = np.hstack((group, data))
    clusters = []
    for i in range(num):
        clusters.append(indexed_data[i])
    dist = update_distance(clusters)
    while len(clusters) > k:
        print(len(clusters))
        (x, y) = find_min(dist)
        clusters[x] = np.vstack((clusters[x], clusters[y]))
        clusters.remove(y)
        dist = update_distance(clusters)
    for i in range(k):
        group_array = clusters[i]
        for j in range(group_array.shape[0]):
            o_index = group_array[j][0]
            result[o_index] = i
    return result


def distance(a, b):
    return np.sqrt(np.power(np.sum(a[:, 1:] - b[:, 1:]), 2))


def cluster_distance(a, b):
    num_a = a.shape[0]
    num_b = b.shape[0]
    dist = np.zeros((num_a, num_b))
    for i in range(num_a):
        for j in range(num_b):
            dist[i][j] = distance(a[i:i+1, :], b[j:j+1, :])
    return np.mean(dist)


def update_distance(clusters):
    num = len(clusters)
    result = np.zeros((num, num))
    for i in range(num):
        for j in range(num):
            result[i][j] = cluster_distance(clusters[i], clusters[j])
            print(i, j)
    return result


def find_min(m):
    return np.argmin(m, axis=1)


if __name__ == '__main__':
    o_data = load_data.get_data(10)
    (x, y) = o_data.shape
    data = o_data[:, 0: y - 4]
    group_result = agnes(data, 4)
    print(measure.measure_k_group(group_result, o_data[:, y - 4:y - 3], 4, 4))

