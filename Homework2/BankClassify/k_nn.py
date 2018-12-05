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
for i in range(0, len(labels) - 1200):
    train_set.append(i)
test_set = []
for i in range(len(labels) - 1200, len(labels)):
    test_set.append(i)


def calculate_distance(cur, neighbor):
    dis = 0
    for i in range(len(numeric_attributes)):
        temp = float(numeric_values[cur][i] - numeric_values[neighbor][i]) / formalisation[i]
        dis += temp * temp
    for i in range(len(non_numeric_attributes)):
        if non_numeric_values[cur][i] != non_numeric_values[neighbor][i]:
            dis += 1
    return dis


def classify(cur, k):
    distance_record = {}
    for neighbor in train_set:
        dis = calculate_distance(cur, neighbor)
        distance_record[neighbor] = dis
    distance_record = sorted(distance_record.items(), key=lambda x: x[1], reverse=False)
    count = 0
    num_false = 0
    for i in range(k):
        key = distance_record[i][0]
        if labels[key] == "\"no\"":
            num_false += 1
        count += 1
        if count >= k:
            break
    if num_false >= k * 0.9:
        res = "\"no\""
    else:
        res = "\"yes\""
    print(cur, res)
    return res


def k_nn(k):
    a = 0
    b = 0
    c = 0
    d = 0
    n = len(test_set)
    for i in test_set:
        res = classify(i, k)
        label = labels[i]
        if label == "\"yes\"" and res == "\"yes\"":
            a += 1
        if label == "\"yes\"" and res == "\"no\"":
            b += 1
        if label == "\"no\"" and res == "\"yes\"":
            c += 1
        if label == "\"no\"" and res == "\"no\"":
            d += 1
    print(a, " ", b, " ", c, " ", d, " ", a + b + c + d)
    a = float(a) / n
    b = float(b) / n
    c = float(c) / n
    d = float(d) / n
    print(a, " ", b, " ", c, " ", d, " ", a + b + c + d)
    print(a + d)


k_nn(100)