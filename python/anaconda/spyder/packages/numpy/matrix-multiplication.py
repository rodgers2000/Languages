#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 11:14:15 2018

@author: Mjr
"""

import numpy as np

A = np.array([[1, 0],
              [1, 1]])
B = np.array([[1, 1],
              [0, 1]])

print(A.dot(B))
print(np.dot(A, B))
print(B.dot(A))
print(np.dot(B, A))
