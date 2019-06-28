#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:22:43 2019

@author: mrodgers
"""

# Code for printing to a file 
sample = open('data/samplefile.txt', 'w') 
  
print('GeeksForGeeks', file=sample) 
print('Michael Rodgers', file=sample)
sample.close()
