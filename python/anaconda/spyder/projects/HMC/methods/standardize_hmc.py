#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 14:40:59 2019

@author: mrodgers
"""

def standardize_hmc(hmc):
    for key in hmc.keys():
        mjr = []
        for key2 in hmc[key].keys():
            mjr.append(hmc[key][key2])
        total = sum(mjr)
        mjr2 = [i / total for i in mjr]
        for i, key2 in enumerate(hmc[key].keys()):
            hmc[key][key2] = mjr2[i]
    return hmc

#mjr = standardize_hmc(hmc)
