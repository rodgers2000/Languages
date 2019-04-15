#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:15:56 2019

@author: mrodgers
"""

# you must lead it to the file name, then access the func or class directly

import objects.Mike as om
import functions.arithmetic as omg

print(omg.add(1, 1))

mjr = om.Mike()

print(mjr.subtract(9, 1))

import os
os.getcwd()