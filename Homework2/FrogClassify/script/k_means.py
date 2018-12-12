#!/usr/bin/env python
# -*- coding: utf-8 -*-


import load_data
import numpy as np
import agnes as ag
import random
import measure
import time


def k_means(data, k):
    # random centers
    (num, factor_num) = data.shape
    has_list = []
    centers = np.zeros((k, factor_num))
    counter = 0
    while counter < k:
        random_index = random.randint(0, num)
        if random_index not in has_list:
            has_list.append(random_index)
            centers[counter,:] = data[random_index, :]
            counter = counter + 1

    # k_means algorithm
    group = np.zeros((num, 1))
    convergence = False
    counter = 0
    while not convergence:
        counter = counter + 1
        print(counter)
        if counter > 10:
            break
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
            group[i,:] = [min_index]
        for i in range(k):
            current_group = data[np.nonzero(group[:,0]==i)[0]]
            centers[i, :] = np.mean(current_group, axis=0)

    return centers, group


def distance(a, b):
    x = a.shape[0]
    a = a.reshape((x, 1))
    b = b.reshape((x, 1))
    num = float(a.T * b)
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    cos = num / denom
    return 0.5 + 0.5 * cos


if __name__ == '__main__':
    o_data = load_data.get_data(18)
    (x, y) = o_data.shape
    data = o_data[:, 0: y - 4]
    k_value = 9
    start = time.clock()
    (centers, group) = k_means(data, k_value)
    result = ag.outer_agens(data, group, k_value, 4)
    end = time.clock()
    print("(F-value, Purity)", measure.measure_k_group(result, o_data[:, y - 4:y - 3], 4, 4))
    print("Time:", start-end)