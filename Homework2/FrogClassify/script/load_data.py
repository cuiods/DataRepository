#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd

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


def get_data():
    return pre_process(get_origin_frog_data()).values


if __name__ == "__main__":
    origin_data = get_origin_frog_data()
    pro_data = pre_process(origin_data)
    print(pro_data)
