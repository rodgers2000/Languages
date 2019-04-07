#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 10:58:28 2018

@author: Mjr
"""


import numpy as np

a = np.zeros((2, 2, 2, 2, 2))

for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        print(i, j)
        print(a[i, j, ...])


for i in range(a.shape[0]):
    print(i)
    print(a[i, ...])