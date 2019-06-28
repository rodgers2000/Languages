#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:02:21 2018

@author: mrodgers
"""

a = [i for i in range(10) if i != 1 and i != 2]

print(a)

mjr = [i**2 for i in range(10)]

mjr = [(i, j) for i in range(2) for j in range(2)]
