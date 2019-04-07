#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:02:56 2019

@author: mrodgers
"""

class InsertionSort:
    
    def sort1(self, A):
        
        for i in range(1, len(A)): # for all the points in A
            point = A[i] # get point
            j = i - 1 # set index to previous point
            while j >= 0 and point < A[j]: # while there is a positive index and
                # the point is less than the previous point
                A[j+1] = A[j] # swap the point with the point to the left
                j -= 1 # use index to go through array 
            A[j+1] = point # we just swapped the point so put it at Aj
            
        return A
    
    def sort2(self, A):
        n = len(A)
        for i in range(n - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                # done
                i -= 1
                flag = True
                while flag:
                    if A[i] > A[i + 1]:
                        A[i], A[i + 1] = A[i + 1], A[i]
                        i -= 1
                    else:
                        flag = False
        return A
    
mjr = InsertionSort()
mjr.sort2([1, 3, 2, 4]) 