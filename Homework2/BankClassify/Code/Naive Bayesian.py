from numpy import *

attribute_path = "C:\\Users\\admin\\Desktop\\attribute"
data_path = "C:\\Users\\admin\\Desktop\\bank-additional-full.csv"
non_numeric_attributes = loadtxt(attribute_path, delimiter=';', dtype=str, usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9, 14))
numeric_attributes = loadtxt(attribute_path, delimiter=';', dtype=str, usecols=(0, 10, 11, 12, 13, 15, 16, 17, 18, 19))
non_numeric_values = loadtxt(data_path, delimiter=';', dtype=str, usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9, 14))
numeric_values = loadtxt(data_path, delimiter=';', dtype=float, usecols=(0, 10, 11, 12, 13, 15, 16, 17, 18, 19))
labels = loadtxt(data_path, delimiter=';', dtype=str, usecols=20)
# deal with numeric attribute 16
# for i in range(len(labels)):
#     numeric_values[i][6] -= 90
# formalisation
formalisation = []
for j in range(len(numeric_attributes)):
    min_value = numeric_values[0][j]
    max_value = numeric_values[0][j]
    for i in range(len(numeric_values)):
        if min_value > numeric_values[i][j]:
            min_value = numeric_values[i][j]
        if max_value < numeric_values[i][j]:
            max_value = numeric_values[i][j]
    if max_value >= -min_value:
        formalisation.append(max_value)
    else:
        formalisation.append(min_value)
# train_set and test_set
train_set = []
test_set = []
for i in range(0, len(labels)):
    base = 0
    if i % 10 == (base + 2) % 10 or i % 10 == (base + 5) % 10 or i % 10 == (base + 7) % 10:
        test_set.append(i)
    else:
        train_set.append(i)
# number_label
number_label = {}
for cur in train_set:
    label = labels[cur]
    if label not in number_label.keys():
        number_label[label] = 0
    number_label[label] += 1


def calculate_p_label(train_set):
    P_label = {}
    for cur in train_set:
        label = labels[cur]
        if label not in P_label.keys():
            P_label[label] = 0
        P_label[label] += 1
    for key in P_label.keys():
        P_label[key] /= len(train_set)
    return P_label


# 分为label类的，第j个非数值型数据值为value的个数 / label类样本个数总数
# 也就是在分为label类的前提下，第j个非数值型数据值为value的概率
def calculate_p_non_numeric_attribute(train_set):
    yes = "\"yes\""
    no = "\"no\""
    P_non_numeric_attribute = {yes: {}, no: {}}
    for j in range(len(non_numeric_attributes)):
        P_non_numeric_attribute[yes][j] = {}
        P_non_numeric_attribute[no][j] = {}
        for i in train_set:
            value = non_numeric_values[i][j]
            if value not in P_non_numeric_attribute[yes][j].keys():
                P_non_numeric_attribute[yes][j][value] = float(0)
            if value not in P_non_numeric_attribute[no][j].keys():
                P_non_numeric_attribute[no][j][value] = float(0)
            P_non_numeric_attribute[labels[i]][j][value] += 1
    for j in range(len(non_numeric_attributes)):
        for value in P_non_numeric_attribute[yes][j].keys():
            P_non_numeric_attribute[yes][j][value] /= number_label[yes]
            P_non_numeric_attribute[no][j][value] /= number_label[no]
            # print(value, " ", P_non_numeric_attribute[yes][j][value])
            # print(value, " ", P_non_numeric_attribute[no][j][value])
        # print("******************")
    return P_non_numeric_attribute


# P[yes][j][0-5]
def calculate_p_numerical_attribute(train_set, range_len):
    yes = "\"yes\""
    no = "\"no\""
    P_numeric_attribute = {yes: {}, no: {}}
    for j in range(len(numeric_attributes)):
        P_numeric_attribute[yes][j] = {}
        P_numeric_attribute[no][j] = {}
        for i in train_set:
            value = int(numeric_values[i][j] / formalisation[j] / range_len)
            if value not in P_numeric_attribute[yes][j].keys():
                P_numeric_attribute[yes][j][value] = float(0)
            if value not in P_numeric_attribute[no][j].keys():
                P_numeric_attribute[no][j][value] = float(0)
            P_numeric_attribute[labels[i]][j][value] += 1
    for j in range(len(numeric_attributes)):
        for value in P_numeric_attribute[yes][j].keys():
            P_numeric_attribute[yes][j][value] /= number_label[yes]
            P_numeric_attribute[no][j][value] /= number_label[no]
            # print(value, " ", P_numeric_attribute[yes][j][value])
            # print(value, " ", P_numeric_attribute[no][j][value])
        # print("******************")
    return P_numeric_attribute


def classify(cur, P_label, P_non_numeric_attribute, P_numeric_attribute, range_len, end_point):
    yes = "\"yes\""
    no = "\"no\""
    P_yes = P_label[yes]
    P_no = P_label[no]
    # print(P_yes, " ", P_no)
    for j in range(len(non_numeric_attributes)):
        value = non_numeric_values[cur][j]
        if value not in P_non_numeric_attribute[yes][j].keys() or value not in P_non_numeric_attribute[no][j].keys():
            continue
        P_yes *= P_non_numeric_attribute[yes][j][value]
        P_no *= P_non_numeric_attribute[no][j][value]
    for j in range(len(numeric_attributes)):
        value = int(numeric_values[cur][j] / formalisation[j] / range_len)
        if value not in P_numeric_attribute[yes][j].keys() or value not in P_numeric_attribute[no][j].keys():
            continue
        P_yes *= P_numeric_attribute[yes][j][value]
        P_no *= P_numeric_attribute[no][j][value]
    # print(P_yes, " ", P_no)
    if P_yes > P_no * end_point:
        return yes
    else:
        return no


def naive_bayes(range_len, end_point):
    P_label = calculate_p_label(train_set)
    P_non_numeric_attribute = calculate_p_non_numeric_attribute(train_set)
    P_numeric_attribute = calculate_p_numerical_attribute(train_set, range_len)
    n = len(test_set)
    a = 0
    b = 0
    c = 0
    d = 0
    for cur in test_set:
        res = classify(cur, P_label, P_non_numeric_attribute, P_numeric_attribute, range_len, end_point)
        label = labels[cur]
        if label == "\"yes\"" and res == "\"yes\"":
            a += 1
        if label == "\"yes\"" and res == "\"no\"":
            b += 1
        if label == "\"no\"" and res == "\"yes\"":
            c += 1
        if label == "\"no\"" and res == "\"no\"":
            d += 1
        # print(res, " ", label)
    print(a, " ", b, " ", c, " ", d, " ", a + b + c + d)
    print("Precision: ", float(a) / (a + c))
    print("Recall: ", float(a) / (a + b))
    a = float(a) / n
    b = float(b) / n
    c = float(c) / n
    d = float(d) / n
    # print(a, " ", b, " ", c, " ", d, " ", a + b + c + d)
    print(a + d)


for range_len in [0.5, 0.1, 0.05, 0.01]:
    for end_point in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        print("range_len: ", range_len, "end_point: ", end_point)
        naive_bayes(range_len, end_point)
        print()
