#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 20:04:53 2019

@author: mrodgers
"""

class SelectionSort:
    
    def sort1(self, A):
        
        for i in range(len(A)): # for all the points 
            
            min_index = i # find the min and traverse the array
            
            for j in range(i + 1, len(A)): # for the points above i 
                if A[min_index] > A[j]: # if we find a new min
                    min_index = j
                
            A[i], A[min_index] = A[min_index], A[i] # swap the points
            
        return A
    
    def sort2(self, A):
        
        for i in range(0, len(A)):
            point = A[i]
            minP = point
            minI = i
            for j in range(i + 1, len(A)):
                if A[j] < minP:
                    minP = A[j]
                    minI = j
            A[i] = minP
            A[minI] = point
        
        return A
            
mjr = SelectionSort()
mjr.sort2([4, 2, 1, 3])