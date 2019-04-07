#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 22:14:23 2018

@author: Mjr
"""

import numpy as np

# =============================================================================
# you can store data in a list, then turn it into an array
# =============================================================================

# =============================================================================
# a = np.array([1, 2, 3, 4]).reshape(2, 2)
#
# b = np.random.randint(1, 10, 4).reshape(2, 2)
#
# print(a)
# print(b)
# print(a - b)
# print(a @ b)
#
# =============================================================================
# =============================================================================
# we will be working with cubes, so lets be in n-dimenional matrix space
# =============================================================================

m = 100
a = np.arange(m).reshape(10, 2, 5)

my_list = []

for i in range(a.shape[0]):
    my_list.append(a[i])

a = my_list[0]

for i in range(1, len(my_list)):
    a = np.hstack((a, my_list[i]))

print(a)
print(a.shape)
