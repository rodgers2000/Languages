#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 11:25:37 2018

@author: Mjr
"""

import numpy as np

a = np.arange(10)**3

for i in a:
    print(i)


def f(x, y):
    return 10*x+y


b = np.fromfunction(f, (5, 4), dtype=int)

b[0:5, 1]
b[:, 1]

b[1:3, :]

b[-5, :]

for i in b:
    print(i)

for i in range(-10, 0, 1):
    print(i)