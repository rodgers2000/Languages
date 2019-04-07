#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:49:14 2019

@author: mrodgers
"""

class BubbleSort:
    
    def sort1(self, A):
        
        n = len(A) # total elements
        
        for i in range(0, n): # for each point in A
            for j in range(0, n - i - 1): # push the point to the top
                if A[j+1] < A[j]: # compare points and swap if true
                    A[j], A[j+1] = A[j+1], A[j]                    
        return A
    
    def sort2(self, A):
        
        i = len(A) - 1
        
        while i > 0:
            for j in range(0, i):
                if A[j] > A[j + 1]:
                    A[j], A[j+1] = A[j+1], A[j]
            i -= 1
        return A

mjr = BubbleSort()
mjr.sort2([1, 5, 3, 2, 4])