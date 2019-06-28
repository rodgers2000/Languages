#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 21:10:54 2019

@author: mrodgers
"""

import numpy as np

mjr = np.arange(6).reshape(3, 2)

mjr[[0, 1]].shape
mjr[0, 1].shape
mjr[0].shape
mjr[[True, False, False]]
mjr[range(2)]

for i in mjr[[0]]:
    print(i)

a = [[1, 2], 
     [3, 4]]
mjr = [1, 2, 3]

b = np.array([a])

b[b > 2] = 0

[1, 2] * b

b[:, 1]

np.array(a)[1][0]
np.array(b)[0][0]

for i in b:
    print(i)
for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j])
mjr = np.array(b).reshape(2, 1)
for i in range(mjr.shape[0]):
    for j in range(mjr.shape[1]):
        print(mjr[i, j])
    
