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
# train_set and test_set
train_set = []
test_set = []
for i in range(0, len(labels)):
    base = 0
    if i % 10 == (base + 2) % 10 or i % 10 == (base + 5) % 10 or i % 10 == (base + 7) % 10:
        test_set.append(i)
    else:
        train_set.append(i)


def sigmoid(inx):
    # print(inx)
    return 1.0 / (1 + exp(-inx))


def grad_ascent(step, times):
    data_matrix = mat(numeric_values[0:len(train_set)])
    label_matrix = mat(labels_format[0:len(train_set)]).transpose()
    m, n = shape(data_matrix)
    alpha = step
    max_cycle = times
    weights = ones((n, 1))
    for k in range(max_cycle):
        h = sigmoid(data_matrix * weights)
        error = (label_matrix - h)
        weights = weights + alpha * data_matrix.transpose() * error
    # print(weights)
    return weights


def classify(step, times):
    weights = grad_ascent(step, times)
    a = 1
    b = 1
    c = 1
    d = 1
    n = len(test_set)
    for i in test_set:
        cur = mat(numeric_values[i])
        res = sigmoid(cur * weights).__float__()
        # print(res)
        if abs(res - 1) < 0.001:
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
    # print(a, " ", b, " ", c, " ", d, " ", a + b + c + d)
    Precision = float(a - 1) / (a + c)
    Recall = float(a - 1) / (a + b)
    a = float(a) / n
    b = float(b) / n
    c = float(c) / n
    d = float(d) / n
    # print(a, " ", b, " ", c, " ", d, " ", a + b + c + d)
    Accuracy = a + d
    return Precision, Recall, Accuracy


p = {}
r = {}
a = {}
for times in [500, 1000, 1500, 2000, 3000]:
    p[times] = []
    r[times] = []
    a[times] = []
    for step in [0.1, 0.05, 0.01, 0.005, 0.001, 0.0005]:
        Precision, Recall, Accuracy = classify(step, times)
        p[times].append(Precision)
        r[times].append(Recall)
        a[times].append(Accuracy)
    print(times)
    print(p[times])
    print(r[times])
    print(a[times])
    print()


