#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 18:16:12 2019

@author: mrodgers
"""

import numpy as np
import pandas as pd

mjr = pd.DataFrame(np.random.rand(10, 10))

means= []
stds = []

for col in range(mjr.shape[1]):
    mjr2 = mjr.iloc[:, col]
    means.append(mjr2.mean())
    stds.append(mjr2.std())

a = mjr[[0]] # a datafrane
b = pd.DataFrame(mjr2)

c = {}
c['means'] = means
c['stds'] = stds

final = pd.DataFrame(c)

final.to_csv('/Users/mrodgers/Documents/other/languages/python/anaconda/spyder/packages/pandas/data/stats.csv')


