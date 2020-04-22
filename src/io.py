# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""Functions for file IO"""
from __future__ import print_function, division, absolute_import

from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np

def load_data(x, y):
    #x will represent the first experiment data MatLab file and y will represent the second experiment data
    v2 = loadmat(x)
    v2_2 = loadmat(y)
    print("Type of file:")
    print(type(v2))
    print()
    print("Dictionary files:")
    print(dict.keys(v2))
    return (v2, v2_2); 

exp1 = 'data/NR-z0131.ezrev4.001.p1.mat'
exp2 = 'data/NR-z0126.ezrev4.002.p1.mat'
v2, v2_2 = load_data(exp1, exp2)


#np.set_printoptions(threshold = 99999999)
np.set_printoptions(threshold=10)