#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 11:19:57 2018

@author: Mjr
"""

import numpy as np

a = np.arange(10).reshape(2, 5)

b = np.arange(10).reshape(2, 5)

print(a, b)

print(a + b)

print(np.add(a, b))

