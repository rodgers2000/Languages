#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 21:51:04 2018

@author: mrodgers
"""

import numpy as np

m = 10

a = np.arange(m)
b = np.arange(m)

# hstack will make (m, ) arrays (m + m, ) arrays

print(np.hstack((a, b)).shape)

# hstack will make (m, 1) arrays (m, 2) arrays

a.resize((m, 1))
b.resize(m, 1)

print(np.hstack((a, b)).shape)

for i in a:
    print(i)

for i in range(0, len(a), 1):
    print(a[i])
