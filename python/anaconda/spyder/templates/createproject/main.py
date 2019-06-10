#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:15:56 2019

@author: mrodgers
"""

# you must lead it to the file name, then access the func or class directly
# 1. 
exec(open("functions/arithmetic.py").read())
# 2. 
import objects.Mike as om
# both ways load the functions to the global environment, 
# if you have naming conflicts, option 2 is better

#import functions.arithmetic as fa
#from functions.arithmetic import *
#

print(add(1, 1))

mjr = om.Mike()

print(mjr.subtract(9, 1))

import os
os.getcwd()