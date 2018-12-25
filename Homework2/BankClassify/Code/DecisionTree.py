from numpy import *
from math import log
import copy


attribute_path = "C:\\Users\\admin\\Desktop\\attribute"
data_path = "C:\\Users\\admin\\Desktop\\bank-additional-full.csv"
non_numeric_attributes = loadtxt(attribute_path, delimiter=';', dtype=str, usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9, 14))
numeric_attributes = loadtxt(attribute_path, delimiter=';', dtype=str, usecols=(0, 10, 11, 12, 13, 15, 16, 17, 18, 19))
non_numeric_values = loadtxt(data_path, delimiter=';', dtype=str, usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9, 14))
numeric_values = loadtxt(data_path, delimiter=';', dtype=float, usecols=(0, 10, 11, 12, 13, 15, 16, 17, 18, 19))
labels = loadtxt(data_path, delimiter=';', dtype=str, usecols=20)
# train_set and test_set
train_set = []
test_set = []
for i in range(0, len(labels)):
    base = 0
    if i % 10 == (base + 2) % 10 or i % 10 == (base + 5) % 10 or i % 10 == (base + 7) % 10:
        test_set.append(i)
    else:
        train_set.append(i)


def calculate_average_values(values):
    average_values = []
    n = len(values)
    for j in range(len(values[0])):
        sum = 0
        for i in range(len(values)):
            sum += float(values[i][j])
        average_values.append(sum / n)
    return average_values


average_numeric_values = calculate_average_values(numeric_values)


def calculate_entropy(subset):
    n = len(subset)
    record = {}
    for cur in subset:
        label = labels[cur]
        if label not in record.keys():
            record[label] = 0
        record[label] += 1
    entropy = 0
    for key in record.keys():
        pxi = float(record[key]) / n
        entropy -= pxi*log(pxi, 2)
    return entropy


def split_data_numeric(set, feature_index):
    sum = 0
    for cur in set:
        sum += numeric_values[cur][feature_index]
    ave = float(sum) / len(set)
    less = "< " + str(ave)
    greater = ">=" + str(ave)
    subsets = {less: [], greater: []}
    for cur in set:
        if numeric_values[cur][feature_index] < ave:
            subsets[less].append(cur)
        else:
            subsets[greater].append(cur)
    return subsets


def split_data_non_numeric(set, feature_index):
    subsets = {}
    for cur in set:
        feature = non_numeric_values[cur][feature_index]
        if feature not in subsets.keys():
            subsets[feature] = []
        subsets[feature].append(cur)
    # sorted(subsets.items(), key=lambda x: x[1], reverse=True)
    return subsets


def find_best_feature(set, remain_numeric_features, remain_non_numeric_features):
    best_feature_index = -1
    is_numeric_feature = True
    n = len(set)
    for i in remain_numeric_features:
        subsets = split_data_numeric(set, i)
        entropy = 0
        for subset in subsets.values():
            cur_probability = float(len(subset)) / n
            cur_entropy = calculate_entropy(subset)
            entropy += cur_probability * cur_entropy
        if best_feature_index == -1 or min > entropy:
            min = entropy
            best_feature_index = i
            best_feature_name = numeric_attributes[i]
            best_subsets = subsets
    for i in remain_non_numeric_features:
        subsets = split_data_non_numeric(set, i)
        entropy = 0
        for subset in subsets.values():
            cur_probability = len(subset) / n
            cur_entropy = calculate_entropy(subset)
            entropy = cur_probability * cur_entropy
        if best_feature_index == -1 or min > entropy:
            min = entropy
            best_feature_index = i
            best_feature_name = non_numeric_attributes[i]
            best_subsets = subsets
            is_numeric_feature = False
    return best_subsets, is_numeric_feature, best_feature_index, best_feature_name


def find_majority_label(set):
    record = {}
    for cur in set:
        label = labels[cur]
        if label not in record.keys():
            record[label] = 0
        record[label] += 1
    num = -1
    for label in record.keys():
        if num < record[label]:
            num = record[label]
            max_label = label
    return max_label


def build_tree(set, remain_numeric_features, remain_non_numeric_features, end_point):
    # if no samples belong to this branch
    if len(set) == 0:
        return "NULL"
    # stop when all samples in this subset belongs to one class
    label = labels[set[0]]
    flag = True
    for cur in set:
        if labels[cur] != label:
            flag = False
            break
    if flag:
        return label
    # true instances become majority
    num_true = 0
    for cur in set:
        if labels[cur] == "\"yes\"":
            num_true += 1
    if float(num_true) / len(set) > end_point:
        return "\"yes\""
    # return the majority of samples' label in this subset if no extra features available
    if len(remain_numeric_features) == 0 and len(remain_non_numeric_features) == 0:
        return find_majority_label(set)
    # find the best feature
    subsets, is_numeric_feature, best_feature_index, best_feature_name = \
        find_best_feature(set, remain_numeric_features, remain_non_numeric_features)
    # remaining instances cannot be divided by any features
    flag = False
    for subset in subsets:
        if float(len(subset)) / len(set) > 0.95:
            flag = True
    if flag:
        return find_majority_label(set)
    # build an inter node
    node_dictionary = {best_feature_index: {}}
    numeric_feature_copy = copy.copy(remain_numeric_features)
    non_numeric_feature_copy = copy.copy(remain_non_numeric_features)
    # print(best_feature_name, ' ', len(left_set), ' ', len(right_set))
    if is_numeric_feature:
        numeric_feature_copy.remove(best_feature_index)
    else:
        non_numeric_feature_copy.remove(best_feature_index)
    for key in subsets.keys():
        node_dictionary[best_feature_index][key] = \
            build_tree(subsets[key], numeric_feature_copy, non_numeric_feature_copy, end_point)
    return node_dictionary


def classify(tree, test_data):
    if type(tree).__name__ != 'dict':
        return tree
    feature_index = list(tree)[0]
    next_branch = tree[feature_index]
    temp = list(next_branch.keys())[0]
    # judge the current value > or < the pivot (average)
    if temp.startswith("< ") or temp.startswith(">="):
        value = numeric_values[test_data][feature_index]
        ave = float(temp[2:])
        less = "< " + str(ave)
        greater = ">=" + str(ave)
        # print(numeric_attributes[feature_index])
        if value < ave:
            next_branch = next_branch[less]
        else:
            next_branch = next_branch[greater]
    else:
        # print(non_numeric_attributes[feature_index])
        value = non_numeric_values[test_data][feature_index]
        if value in next_branch.keys():
            next_branch = next_branch[value]
        else:
            return "\"no\""
    return classify(next_branch, test_data)


def decision_tree(end_point):
    # print(average_numeric_values)
    remain_numeric_features = []
    for i in range(len(numeric_attributes)):
        remain_numeric_features.append(i)
    remain_non_numeric_features = []
    for i in range(len(non_numeric_attributes)):
        remain_non_numeric_features.append(i)
    tree = build_tree(train_set, remain_numeric_features, remain_non_numeric_features, end_point)
    # print(tree)
    n = len(test_set)
    a = 0
    b = 0
    c = 0
    d = 0
    for i in test_set:
        res = classify(tree, i)
        label = labels[i]
        # print(res, " ", label)
        if label == "\"yes\"" and res == "\"yes\"":
            a += 1
        if label == "\"yes\"" and res == "\"no\"":
            b += 1
        if label == "\"no\"" and res == "\"yes\"":
            c += 1
        if label == "\"no\"" and res == "\"no\"":
            d += 1
    print(a, " ", b, " ", c, " ", d, " ", a + b + c + d)
    print("Precision: ", float(a) / (a + c))
    print("Recall: ", float(a) / (a + b))
    a = float(a) / n
    b = float(b) / n
    c = float(c) / n
    d = float(d) / n
    # print(a, " ", b, " ", c, " ", d, " ", a + b + c + d)
    print(a + d)


for end_point in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
    print("end_point: ", end_point)
    decision_tree(end_point)
    print()
