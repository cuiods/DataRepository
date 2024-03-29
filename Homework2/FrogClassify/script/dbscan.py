import load_data
import numpy as np
import measure
import agnes as ag
from scipy.spatial import KDTree
from random import choice
import time


def dbscan(data, eps, min_pts):
    m = data.shape[0]
    points = VisitRecord(m)
    group_index = -1
    group = np.zeros((m, 1))-1
    kd_tree = KDTree(data)
    while points.unvisited_num > 0:
        current_visit = choice(points.unvisited)
        points.visit(current_visit)
        print("unvisited", points.unvisited_num)
        round_points = kd_tree.query_ball_point(data[current_visit], eps)
        if len(round_points) >= min_pts:
            group_index += 1
            group[current_visit] = group_index
            for p_index in round_points:
                print("unvisited", points.unvisited_num, group_index)
                if p_index in points.unvisited:
                    points.visit(p_index)
                    round_points_next = kd_tree.query_ball_point(data[p_index], eps)
                    if len(round_points_next) >= min_pts:
                        for i_index in round_points_next:
                            if i_index not in round_points:
                                round_points.append(i_index)
                    if group[p_index] == -1:
                        group[p_index] = group_index
        else:
            group[current_visit] = -1
    return group, group_index


def distance(a, b):
    return np.sqrt(np.power(np.sum(a - b), 2))


class VisitRecord:
    def __init__(self, count=0):
        self.unvisited = [i for i in range(count)]
        self.visited = list()
        self.unvisited_num = count

    def visit(self, point):
        self.visited.append(point)
        self.unvisited.remove(point)
        self.unvisited_num -= 1


if __name__ == '__main__':
    o_data = load_data.get_data()
    (x, y) = o_data.shape
    data = o_data[:, 0: y - 4]
    start = time.clock()
    (group, group_index) = dbscan(data, 0.18, 12)
    true_result = o_data[:, y - 4:y - 3]
    true_result = true_result[np.nonzero(group[:,0] >= 0)[0]]
    group = group[np.nonzero(group[:,0] >= 0)[0]]
    data = data[np.nonzero(group[:,0] >= 0)[0]]
    result = ag.outer_agens(data, group, group_index, 4)
    end = time.clock()
    print("(F-value, Purity)", measure.measure_k_group(result, true_result, 4, 4))
    print("Time:", end - start)