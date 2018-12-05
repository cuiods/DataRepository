from numpy import *

attribute_path = "C:\\Users\\admin\\Desktop\\attribute"
data_path = "C:\\Users\\admin\\Desktop\\bank-additional-full.csv"
non_numeric_attributes = loadtxt(attribute_path, delimiter=';', dtype=str, usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9, 14))
numeric_attributes = loadtxt(attribute_path, delimiter=';', dtype=str, usecols=(0, 10, 11, 12, 13, 15, 16, 17, 18, 19))
non_numeric_values = loadtxt(data_path, delimiter=';', dtype=str, usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9, 14))
numeric_values = loadtxt(data_path, delimiter=';', dtype=float, usecols=(0, 10, 11, 12, 13, 15, 16, 17, 18, 19))
labels = loadtxt(data_path, delimiter=';', dtype=str, usecols=20)
# labels_format
labels_format = []
for j in range(len(labels)):
    if labels[j] == "\"yes\"":
        labels_format.append(1)
    else:
        labels_format.append(0)
# train_set
train_set = []
for i in range(0, int(len(labels) * 0.75)):
    train_set.append(i)
# test_set
test_set = []
for i in range(int(len(labels) * 0.75), len(labels)):
    test_set.append(i)


def sigmoid(inx):
    # print(inx)
    return 1.0 / (1 + exp(-inx))


def grad_ascent():
    data_matrix = mat(numeric_values[0:len(train_set)])
    label_matrix = mat(labels_format[0:len(train_set)]).transpose()
    m, n = shape(data_matrix)
    alpha = 0.001
    max_cycle = 5000
    weights = ones((n, 1))
    for k in range(max_cycle):
        h = sigmoid(data_matrix * weights)
        error = (label_matrix - h)
        weights = weights + alpha * data_matrix.transpose() * error
    m, n = shape(weights)
    print(weights)
    return weights


def classify():
    weights = grad_ascent()
    a = 0
    b = 0
    c = 0
    d = 0
    n = len(test_set)
    for i in test_set:
        cur = mat(numeric_values[i])
        res = sigmoid(cur * weights).__float__()
        if res == 1:
            res = "\"yes\""
        else:
            res = "\"no\""
        label = labels[i]
        if label == "\"yes\"" and res == "\"yes\"":
            a += 1
        if label == "\"yes\"" and res == "\"no\"":
            b += 1
        if label == "\"no\"" and res == "\"yes\"":
            c += 1
        if label == "\"no\"" and res == "\"no\"":
            d += 1
        # print(res, " ", label)
    print(len(train_set), " ", len(test_set))
    print(a, " ", b, " ", c, " ", d, " ", a + b + c + d)
    a = float(a) / n
    b = float(b) / n
    c = float(c) / n
    d = float(d) / n
    print(a, " ", b, " ", c, " ", d, " ", a + b + c + d)
    print(a + d)


classify()
