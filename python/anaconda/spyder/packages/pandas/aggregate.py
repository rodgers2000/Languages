#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:30:22 2019

@author: mrodgers
"""

import pandas as pd

a = list(range(5))
b = [6, 7, 8, 9, 10]
c = ['1', '1', '2', '2', '2']

mjr = pd.DataFrame()

mjr['a'] = a
mjr['b'] = b
mjr['c'] = c

def mean(x):
    return sum(x) / len(x)

mjr.groupby('c').agg({'a': [sum], 'b': [mean, 'std', sum]})
