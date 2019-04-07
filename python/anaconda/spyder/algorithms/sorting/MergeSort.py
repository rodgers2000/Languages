#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 13:20:50 2019

@author: mrodgers
"""

class MergeSort:
        
    def merge(self, L, R):      
        A = []
        
        while len(L) + len(R) != 0: # while there are still numbers
            if len(L) != 0 and len(R) != 0: # if both still have numbers
                if L[0] < R[0]: # compare the smallest numbers
                    A.append(L.pop(0))
                else:
                    A.append(R.pop(0))
            else: # one of the lists does not have elements
                if len(L) != 0: # so remove them in the order they come in 
                    A.append(L.pop(0))
                if len(R) != 0:
                    A.append(R.pop(0))
        return A
        
                
    def mergesort(self, X):
        # escape case: 
        if len(X) == 1:
            return X
        # divide and conquer
        mid = int(len(X) / 2)
        L = X[:mid]
        R = X[mid:]
        # binary split
        L = self.mergesort(L)
        R = self.mergesort(R)
        return self.merge(L, R)
        

mjr = MergeSort()
mjr.mergesort([1, 5, 3, 4, 8])