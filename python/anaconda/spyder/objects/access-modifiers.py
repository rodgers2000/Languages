#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 15:55:46 2019

@author: mrodgers
"""

class A:
    def __init__(self, a, b, c):
        self.a = a
        self._b = b 
        self.__c = c
        
class B:
    def __init__(self, a, b, c, d):
        self.A = A(a, b, c)
        self.d = d
        
mjr = B(1, 2, 3, 4)

mjr.A.a
mjr.A._b
mjr.A.__c # access denied 