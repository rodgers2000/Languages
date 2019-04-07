#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 22:37:39 2018

@author: Mjr
"""

import numpy as np

a = np.array([1, 2, 3])

b = np.array([[1, 2, 3],
              [4, 5, 6]])

c = np.array([[[7,   8,  9],
               [10, 11, 12],
               [13, 14, 15]],
              [[16, 17, 18],
               [19, 20, 21],
               [22, 23, 24]],
              [[25, 26, 27],
               [28, 29, 30],
               [31, 32, 33]]])

d = np.array([
                [[10, 11, 12],
                 [13, 14, 15],
                 [16, 17, 18]],
                [[19, 20, 21],
                 [22, 23, 24],
                 [25, 26, 27]],
                [[28, 29, 30],
                 [31, 32, 33],
                 [34, 35, 36]],
                [[37, 38, 39],
                 [40, 41, 42],
                 [43, 44, 45]]
            ])

print(a)
print(b)
print(c)
print(d.shape)

#for i in range(c.shape[0]):
#    for j in range(c.shape[1]):
#        for k in range(c.shape[2]):
#            print(c[i, j, k])

