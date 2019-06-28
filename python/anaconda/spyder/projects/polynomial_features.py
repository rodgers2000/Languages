#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 14:31:19 2019

@author: mrodgers
"""

import numpy as np

a = np.array([1, 2, 3, 4]).reshape(4, 1)

def polynomial_features(x=a, degree=2):
    mjr2 = np.zeros((x.shape[0], degree))
    mjr3 = np.ones((x.shape[0], 1))
    mjr4 = np.concatenate((mjr3, mjr2), axis=1)
    for i in range(1, x.shape[1]+2):
        mjr4[:, i] = np.array(x ** i).reshape((4,))
    return mjr4
        
    
print(polynomial_features())
