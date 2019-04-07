#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 15:22:34 2018

@author: Mjr
"""


import numpy as np

a = np.arange(3).reshape(1, 3)
b = np.arange(2).reshape(1, 2)

print(np.vstack((a, b)))  # 2x2 v 2x2 = 4 x 2
print(np.hstack((a, b)))  # 2x2 h 2x2 = 2 x 4
print(np.column_stack((a, b)))

np.hstack
np.column_stack