#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 11:03:12 2018

@author: Mjr
"""

import numpy as np

a = np.arange(24).reshape(2, 3, 2, 2)

print(a)

#a = np.reshape(a, (5, 2))

#print(a)

#a = a.reshape(5, 2)
#
#print(a)


for i in a:
    for j in i:
        for k in j:
            for l in k:
                print(l)

for i in a:
    for j in i:
        print(j)