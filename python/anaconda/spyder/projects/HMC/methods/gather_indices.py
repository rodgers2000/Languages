#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 14:02:59 2019

@author: mrodgers
"""

def gather_indices(df, order):
    indices = {}
    indices['reg'] = []
    indices['pred'] = []
    for i in range(0, df.shape[0] - order - 1):
        mjr = [i]
        if order != 1:
            for j in range(1, order):
                mjr.append(i + j)
        else:
            j = 0
        indices['reg'].append(mjr)
        indices['pred'].append(i + j + 1)
    return indices
    
#mjr = gather_indices(df, 2)
