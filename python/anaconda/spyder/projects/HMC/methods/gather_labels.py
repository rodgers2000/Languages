#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 14:11:58 2019

@author: mrodgers
"""

def gather_labels(df, indices):
    mjr = {}

    for counter, index1 in enumerate(indices['reg']):
        temp_df = df.iloc[index1]
        this_pattern = tuple(temp_df['percent_change'])
        temp_df2 = df.iloc[indices['pred'][counter]]
        this_pred = tuple([temp_df2['percent_change']])
        if this_pattern not in mjr:
            mjr[this_pattern] = {}
            mjr[this_pattern][this_pred] = 1
            # if this_pred not in mjr[this_pattern].keys
        elif this_pred not in mjr[this_pattern]:
            mjr[this_pattern][this_pred] = 1
        else:
            mjr[this_pattern][this_pred] += 1
    
    # remove NA
    for key in mjr.keys():
        if key[0] == 'NA':
            remove_key = key
    mjr.pop(remove_key)
            
    return mjr
        
#mjr = gather_labels(df, indices)
