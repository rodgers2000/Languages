#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 13:04:22 2018

@author: Mjr
"""

import numpy as np

a = np.arange(12).reshape(1, 3, 2, 2)

print(a)

print('python indexing')

for i in range(0, a.shape[0]):
    for j in range(0, a.shape[1]):
        for k in range(0, a.shape[2]):
            for l in range(0, a.shape[3]):
                print(a[i, j, k, l])


print('object indexing')

for i in a:
    for j in i:
        for k in j:
            for l in k:
                print(l)

print('c++ indexing')

for i in range(-a.shape[0], 0):
    for j in range(-a.shape[1], 0):
        for k in range(-a.shape[2], 0):
            for l in range(-a.shape[3], 0):
                print(a[i, j, k, l])

print('flat indexing')

for i in a.flat:
    print(i)
