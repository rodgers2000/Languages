#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:52:09 2019

@author: mrodgers
"""

def compute_percent_change(df):
    prices = df['Adj Close']
    percent_change = ['NA']
    for i in range(1, df.shape[0]):
        this_return = (prices[i] - prices[i-1]) / prices[i-1]
        if this_return > 0:
            percent_change.append(1)
        else:
            percent_change.append(0)
    df['percent_change'] = percent_change
    return df

#df = compute_percent_change(df)
