#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 17:01:53 2019

@author: mrodgers
"""

import numpy as np
import pandas as pd

#df = pd.read_csv('data/sp500.csv')
prices = np.random.normal(size=6)
#prices = list(df['Adj Close'])

class BalanceBeam():
    
    def __init__(self, x, degree):
        self.series= x 
        self.degree = degree
    
    def average(self, x):
        return sum(x) / len(x)
    
    def main(self):
        diff = []
        for i in range(self.degree, len(self.series) - self.degree):
            # get indices
            # start from degree - degree: degree
            # end n - 2*degree - 1:n - degree - 1
            left_series = self.series[(i - self.degree):(i)]
            # start from degree + 1: 2*degree + 1
            # end from n - degree:n
            right_series = self.series[(i+1):(i + self.degree + 1)]
            left_avg = self.average(left_series)
            right_avg = self.average(right_series)
            mid_avg = self.average([left_avg, right_avg])
            # get price
            price = self.series[i]
            # calculate differences
            diff.append((mid_avg - price)**2)
        return self.average(diff)
    
mjr = BalanceBeam(prices, 2)
print(mjr.main())
            