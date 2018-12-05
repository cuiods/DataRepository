#!/usr/bin/env python
# -*- coding: utf-8 -*-


import load_data
import numpy as np
import measure


def k_means(data, k):
    # random centers
    random = np.random.RandomState(0)
    (num, factor_num) = data.shape
    centers = np.zeros((k, factor_num))
    for i in range(factor_num):
        vec = data[:, i]
        centers[:, i] = random.uniform(vec.min(), vec.max(), k)

    # k_means algorithm
    group = np.zeros((num, 2))
    convergence = False
    while not convergence:
        convergence = True
        for i in range(num):
            min_distance = np.inf
            min_index = -1
            for j in range(k):
                dis = distance(centers[j,:], data[i,:])
                if dis < min_distance:
                    min_distance = dis
                    min_index = j
            if group[i,0] != min_index:
                convergence = False
            group[i,:] = [min_index, min_distance]
        for i in range(k):
            current_group = data[np.nonzero(group[:,0]==i)[0]]
            centers[i, :] = np.mean(current_group, axis=0)

    return centers, group


def distance(a, b):
    return np.sqrt(np.power(np.sum(a - b), 2))


if __name__ == '__main__':
    o_data = load_data.get_data(18)
    (x, y) = o_data.shape
    data = o_data[:, 0: y - 4]
    (centers, group) = k_means(data, 4)
    print(measure.measure_k_group(group, o_data[:, y - 4:y - 3], 4, 4))