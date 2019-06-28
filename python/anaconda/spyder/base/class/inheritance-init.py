#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 13:27:45 2019

@author: mrodgers
"""

class One():
    
    def __init__(self, x):
        self.x = x
        
class Two(One):
    
    def __init__(self, x, y):
#        One.__init__(self, x)
        super().__init__(x)
        self.y = y
        
mjr = Two(1, 2)
print(mjr.x)
print(mjr.y)
