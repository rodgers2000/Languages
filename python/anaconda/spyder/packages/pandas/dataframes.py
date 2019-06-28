#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 13:43:01 2019

@author: mrodgers
"""
import pandas as pd

a = [1, 2, 3, 4]
b = list(range(1, 5))
ab = {'a': a, 'b': b}
mjr = pd.DataFrame(ab)

""" create new column """
mjr['c'] = mjr['b'] + mjr['a']
mjr['d'] = [5, 6, 7, 8]
mjr['e'] = ['a', 'b', 'c', 'd']

""" change column names """
mjr.columns = ['1', '2', '3'] 

""" slicing a datafreame """
mjr[0:1] 

""" rbind a dataframe """
mjr2 = pd.DataFrame({'1': [69], '2': [69], '3': [69]})
mjr = pd.concat([mjr, mjr2], axis=0) 
mjr.index = list(range(0, mjr.shape[0])) 

""" cbind a dataframe """
mjr3 = pd.DataFrame({'4': [1, 2, 3, 4, 5]})
pd.concat([mjr, mjr3], axis=1)
