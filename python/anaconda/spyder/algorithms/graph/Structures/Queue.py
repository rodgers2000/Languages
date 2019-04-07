#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:35:03 2019

@author: mrodgers
"""

class Queue:
    
    def __init__(self):
        self.Q = []
        
    def enqueue(self, item):
        self.Q.append(item)
        
    def dequeue(self):
        return self.Q.pop(0)
    
    def isempty(self):
        if len(self.Q) > 0:
            return False
        else:
            return True