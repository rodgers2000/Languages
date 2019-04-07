#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 12:47:39 2018

@author: mrodgers
"""

import numpy as np

X = np.random.rand(100, 64, 64)

print(X[1, ...])

X = X.reshape(X.shape[0], -1)

print(X.shape)  # this gives n x p, we want p x n, so you transpose!!!

print(X[1, ...])

# =============================================================================
# reshape reshaoes by row when you do this,
# so row1, row2, row3, ... until you have a column vector
# =============================================================================
