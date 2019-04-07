#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:08:23 2018

@author: mrodgers
"""

import numpy as np

a = np.ones((3, 2))
b = np.zeros((3, 2))

print(np.concatenate((a, b), axis=1))
print(np.concatenate((a, b), axis=0))

c = np.hstack((a, b))

print(c.shape)

print(np.hsplit(c, (2)))  # split after the third column

print(np.array_split(c, 2, axis=1))

# =============================================================================
# this results in the same, so we can matrix. so they are equivalent
# =============================================================================

# use concatenate and split!!!