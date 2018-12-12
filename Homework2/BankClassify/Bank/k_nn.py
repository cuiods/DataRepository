from numpy import *
import operator


attribute_path = "C:\\Users\\admin\\Desktop\\attribute"
data_path = "C:\\Users\\admin\\Desktop\\bank-additional.csv"
non_numeric_attributes = loadtxt(attribute_path, delimiter=';', dtype=str, usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9, 14))
numeric_attributes = loadtxt(attribute_path, delimiter=';', dtype=str, usecols=(0, 10, 11, 12, 13, 15, 16, 17, 18, 19))
non_numeric_values = loadtxt(data_path, delimiter=';', dtype=str, usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9, 14))
numeric_values = loadtxt(data_path, delimiter=';', dtype=float, usecols=(0, 10, 11, 12, 13, 15, 16, 17, 18, 19))
labels = loadtxt(data_path, delimiter=';', dtype=str, usecols=20)
formalisation = []

for j in range(len(numeric_attributes)):
    min_value = numeric_values[0][j]
    max_value = numeric_values[0][j]
    for i in range(len(numeric_values)):
        if min_value > numeric_values[i][j]:
            min_value = numeric_values[i][j]
        if max_value < numeric_values[i][j]:
            max_value = numeric_values[i][j]
    formalisation.append(max_value - min_value)


train_set = []
test_set = []
for i in range(0, len(labels)):
    base = 0
    if i % 10 == (base + 2) % 10 or i % 10 == (base + 5) % 10 or i % 10 == (base + 7) % 10:
        test_set.append(i)
    else:
        train_set.append(i)


def calculate_distance(cur, neighbor):
    dis = 0
    for i in range(len(numeric_attributes)):
        temp = float(numeric_values[cur][i] - numeric_values[neighbor][i]) / formalisation[i]
        dis += temp * temp
    for i in range(len(non_numeric_attributes)):
        if non_numeric_values[cur][i] != non_numeric_values[neighbor][i]:
            dis += 1
    return dis


def classify(cur, k, end_point):
    distance_record = {}
    for neighbor in train_set:
        dis = calculate_distance(cur, neighbor)
        distance_record[neighbor] = dis
    distance_record = sorted(distance_record.items(), key=lambda x: x[1], reverse=False)
    count = 0
    num_true = 0
    for i in range(k):
        key = distance_record[i][0]
        if labels[key] == "\"yes\"":
            num_true += 1
        count += 1
        if count >= k:
            break
    if num_true >= float(k) * end_point:
        res = "\"yes\""
    else:
        res = "\"no\""
    # print(cur, res)
    return res


def k_nn(k, end_point):
    a = 1
    b = 1
    c = 1
    d = 1
    n = len(test_set)
    for i in test_set:
        res = classify(i, k, end_point)
        label = labels[i]
        if label == "\"yes\"" and res == "\"yes\"":
            a += 1
        if label == "\"yes\"" and res == "\"no\"":
            b += 1
        if label == "\"no\"" and res == "\"yes\"":
            c += 1
        if label == "\"no\"" and res == "\"no\"":
            d += 1
        # print(a, " ", b, " ", c, " ", d, " ", a + b + c + d)
    Precision = float(a - 1) / (a + c)
    Recall = float(a - 1) / (a + b)
    a = float(a) / n
    b = float(b) / n
    c = float(c) / n
    d = float(d) / n
    # print(a, " ", b, " ", c, " ", d, " ", a + b + c + d)
    Accuracy = a + d
    print(Precision, Recall, Accuracy)
    return Precision, Recall, Accuracy


p = {}
r = {}
a = {}
for end_point in [0.1, 0.3, 0.5]:
    p[end_point] = []
    r[end_point] = []
    a[end_point] = []
    for k in [1, 3, 5, 10, 20, 50, 100]:
        Precision, Recall, Accuracy = k_nn(k, end_point)
        p[end_point].append(Precision)
        r[end_point].append(Recall)
        a[end_point].append(Accuracy)
    print(end_point)
    print(p[end_point])
    print(r[end_point])
    print(a[end_point])
    print()
