#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 16:58:22 2019

@author: mrodgers
"""
mjr = []
mjr.append(((1, 2), (2, 1)))
mjr.append(((1, 2), (1, 2)))

((1, 2), (2, 1)) in mjr

mjr = {}
mjr[1] = {1:1, 2:3}
mjr[2] = {4:5, 6:7}
mjr[3] = {8:9}

for key in mjr.keys():
    for key2 in mjr[key].keys():
            print(mjr[key][key2])
