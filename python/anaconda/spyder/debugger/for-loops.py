#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:54:11 2019

@author: mrodgers
"""

import numpy as np
import pandas as pd
m = 100
x = np.random.rand(m)
y = np.random.choice([1, 2, 3], size=m)
z = np.random.choice([4, 5, 6], size=m)

mjr = pd.DataFrame()
mjr['x'] = x
mjr['y'] = y
mjr['z'] = z

y_unique = mjr['y'].unique()
z_unique = mjr['z'].unique()

for i in y_unique:
    for j in z_unique:
        temp = mjr[(mjr.y == i) & (mjr.z == j)]
        print(temp)