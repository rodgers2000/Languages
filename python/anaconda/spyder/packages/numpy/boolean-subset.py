#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:30:52 2018

@author: mrodgers
"""

import numpy as np

a = np.random.rand(5, 5)

b = a[a > .5]

print(b)

a[a > .5] = 0

print(a)