#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:46:56 2019

@author: mrodgers
"""

import pandas as pd
import methods.compute_percent_change as mc
import methods.gather_indices as mg
import methods.gather_labels as mgl
import methods.standardize_hmc as ms

df = pd.read_csv('data/sp500.csv')
df = mc.compute_percent_change(df)
indices = mg.gather_indices(df, 5)
hmc = mgl.gather_labels(df, indices)
hmc = ms.standardize_hmc(hmc)

for order in range(1, 5):
    indices = mg.gather_indices(df, order)
    hmc = mgl.gather_labels(df, indices)
    hmc = ms.standardize_hmc(hmc)
    new_df = pd.DataFrame()
    new_df['order'] = hmc.keys()
    ones = []
    zeros = []
    for key in hmc.keys():
        for i, value in enumerate(hmc[key].values()):
            if i == 0:
                zeros.append(value)
            else:
                ones.append(value)
    new_df['0'] = zeros
    new_df['1'] = ones            
    new_df.to_csv('data/{}.csv'.format(str(order)), index=False)
