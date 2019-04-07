#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:35:38 2018

@author: mrodgers
"""

import numpy as np

a = np.random.rand(3, 2, 5, 5)  # hyper cube

print(a[0])  # print the first (2, 5, 5) cube

print(a[0, 0, ...])  # print the first (5, 5) matrix

print(a[0, 0, 0, ...])  # print the first (1, 5) vector

print(a[0, 0, 0, 0])  # print the first (1, 1) scalar

# so it goes... 3rd, 2nd, 0th, 1st dimenion

"""
This is a document string. This is very useful
for commenting in large portions.
"""
