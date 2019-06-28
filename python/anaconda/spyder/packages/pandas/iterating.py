#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 16:16:18 2019

@author: mrodgers
"""

import pandas as pd

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
ab = {'a': a, 'b': b}
mjr = pd.DataFrame(ab)

for i in range(mjr.shape[0]):
    for j in range(mjr.shape[1]):
        print(mjr.iloc[i, j])
        
for i in range(mjr.shape[0]):
    print(mjr.loc[i, 'a'])
    
abc = mjr['a']
for i in range(abc.shape[0]):
    print(abc[i])
