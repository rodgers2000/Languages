#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:18:57 2019

@author: mrodgers
"""
# this is assignment by reference
a = [1, 2, 3]
b = a
#b = [1, 2, 3]

print(b is a)
print(a is b)

b.append(4)
print(a)
print(b)