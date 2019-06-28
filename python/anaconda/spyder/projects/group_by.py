#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 20:58:42 2019

@author: mrodgers
"""

import numpy as np
import pandas as pd

m = 100
a = np.random.choice([0, 1, 2], m)
b = np.random.normal(size=m)
mjr = pd.DataFrame()

mjr['a'] = a
mjr['b'] = b

groups = mjr['a'].unique()
groups = list(groups)
groups.sort()
##1
#data = {i:{} for i in groups}
##2
#data = {}
#for group in groups:
#    data[group] = {}

results = pd.DataFrame(np.zeros((9, 2)), columns=['stats','values'])

i = [0, 1, 2]
for group in groups:
    temp = mjr[mjr['a'] == group]
    mean = np.mean(temp['b'])
    median = np.median(temp['b'])
    std = np.std(temp['b'])
    
    results['values'].iloc[i] = [mean, median, std]
    results['stats'].iloc[i] = ['mean'+'_'+str(group), 'median'+'_'+str(group), 'std'+'_'+str(group)]
    i = list(map(lambda x:x+3, i))
    
print(results)
#    data[group]['mean'] = mean
#    data[group]['median'] = median
#    data[group]['std'] = std
    

#columns = []
#values = []
#for group in groups:
#    for stat in ['mean', 'median', 'std']:
#        string = str(group)+ '_' + stat
#        columns.append(string)
#        value = data[group][stat]
#        values.append(value)
#
#mjr = pd.DataFrame(data=list(map(list, zip(*[columns, values]))), 
#                   columns=['value', 'stat'])

#mjr.to_csv('data/test.csv', index=False)
        