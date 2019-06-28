#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 13:01:39 2019

@author: mrodgers
"""

class One():
    
    def __init__(self, x):
        self.x = x
        
    def add(self, i):
        self.x += i
        
mjr = One(11)
One.add(mjr, 1)
mjr.x

a = One.__init__(a, 10) # error
