import numpy as np


def measure_k_group(group, result, k, c, beta=1):
    test = np.concatenate((group, result), axis=1)
    n = group.shape[0]
    f_value = 0
    for i in range(k):
        k_group = test[np.nonzero(group[:, 0] == i)[0]]
        total_num = k_group.shape[0]
        max_num = -1
        max_index = -1
        for j in range(c):
            c_group = k_group[np.nonzero(k_group[:, 2] == j)[0]]
            num = c_group.shape[0]
            if num > max_num:
                max_num = num
                max_index = j
        recall_num = result[np.nonzero(result == max_index)[0]].shape[0]
        p = max_num*1.0 / total_num
        r = max_num*1.0 / recall_num
        print(p)
        print(r)
        weight = total_num*1.0 / n
        f_value += weight * ((beta*beta + 1) * p * r) / (beta * beta * p + r)
    return f_value
