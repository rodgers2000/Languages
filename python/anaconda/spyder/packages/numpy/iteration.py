#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 20:25:29 2019

@author: mrodgers
"""

import numpy as np

mjr = [[1, 2, 3],
       [4, 5, 6]]

mjr = np.array(mjr)

for i in mjr:
    for j in i:
        print(j)
        
for i in range(mjr.shape[0]):
    for j in range(mjr.shape[1]):
        print(mjr[i, j])
        print(mjr[i][j])
        
i, j = mjr.shape
