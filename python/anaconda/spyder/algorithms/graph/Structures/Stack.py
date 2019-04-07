#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 13:57:31 2019

@author: mrodgers
"""

class Stack:
    
    def __init__(self):
        self.S = []
        
    def push(self, item):
        self.S.append(item)
    
    def pop(self):
        self.S.pop()
        
    def isempty(self):
        if len(self.S) > 0:
            return False
        else:
            return True