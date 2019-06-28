#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 21:08:36 2019

@author: mrodgers
"""

mjr = [[1, 2, 3], [4, 5, 6]]

for i in mjr:
    for j in i:
        print(j)
        
for i in range(len(mjr)):
    for j in range(len(mjr[i])):
        print(mjr[i][j])
        
import numpy as np

mjr = np.arange(10).reshape(5, 2)

for i in range(mjr.shape[0]):
    for j in range(mjr.shape[1]):
        print(mjr[i, j])
        print(mjr[i][j])