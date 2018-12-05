#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

FAMILY = ['Bufonidae','Dendrobatidae','Hylidae','Leptodactylidae']
GENUS=['Adenomera', 'Ameerega', 'Dendropsophus', 'Hypsiboas', 'Leptodactylus', 'Osteocephalus', 'Rhinella','Scinax']
SPECIES=['AdenomeraAndre','AdenomeraHylaedactylus','Ameeregatrivittata','HylaMinuta','HypsiboasCinerascens','HypsiboasCordobae',
         'LeptodactylusFuscus','OsteocephalusOophagus','Rhinellagranulosa','ScinaxRuber']


def get_origin_frog_data():
    data_frame = pd.read_csv('../data/Frogs_MFCCs.csv')
    return data_frame


def pre_process(data_frame):
    data_frame['Family'] = data_frame['Family'].map(lambda x: FAMILY.index(x))
    data_frame['Genus'] = data_frame['Genus'].map(lambda x: GENUS.index(x))
    data_frame['Species'] = data_frame['Species'].map(lambda x: SPECIES.index(x))
    return data_frame


def get_data(n_components=-1):
    o_data = pre_process(get_origin_frog_data()).values
    (x, y) = o_data.shape
    data = o_data[:, 0: y - 4]
    if n_components > 0:
        pca = PCA(data, n_components)
        data = pca.reduce_dimension()
    data = np.hstack((data, o_data[:, y-4:]))
    return data


class PCA(object):

    def __init__(self, x, n_components):
        self.x = x
        self.n_components = n_components

    def reduce_dimension(self):
        average = np.mean(self.x, axis=0)
        m, n = np.shape(self.x)
        avgs = np.tile(average, (m, 1))
        data_aj = self.x - avgs
        cov_x = np.cov(data_aj.T)
        feature, feature_vec = np.linalg.eig(cov_x)
        sorted_index = np.argsort(-feature)
        select_vec = np.matrix(feature_vec.T[sorted_index[:self.n_components]])
        reduced_data = data_aj * select_vec.T
        return reduced_data


if __name__ == "__main__":
    origin_data = get_origin_frog_data()
    pro_data = pre_process(origin_data)
    print(pro_data)
