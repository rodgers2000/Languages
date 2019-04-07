#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 21:37:33 2018

@author: mrodgers
"""

import numpy as np 

m = 10 

a = np.arange(m)
b = np.arange(m)

print(a.shape)
print(b.shape)

# hstack will make (m, ) arrays (m + m, ) arrays

print(np.hstack(a, b)

# hstack will make (m, 1) arrays (m, 2) arrays

