#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:46:21 2019

@author: mrodgers
"""

def mjr(*args):
    for i in args:
        print(i)

mjr(1, 2, 3)
mjr(*[1, 2, 3])

def mjr2(**kargs):
    for key, value in kargs.items():
        print("key: ", key)
        print("value: ", value)
        
mjr2(one=1, two=2)
mjr2(**{'one':1, 'two':2})