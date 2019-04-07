#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:18:40 2019

@author: mrodgers
"""

class ShellSort:        
    
    def sort1(self, A):
        n = len(A) # get the length of the array
        gap = n // 2 # floor division by 2
        
        while gap > 0: # gaps must end at 1
            
            for i in range(gap, n): # these are the points to consider
                temp = A[i] # first value is the basis point
                
                j = i # the while loop will select one value
                while j >= gap and A[j - gap] > temp: 
                    A[j] = A[j - gap] # swap it
                    j -= gap # this stops the while loop
                A[j] = temp # swap it
                
            gap //= 2 # reduce the gap by half
        return A
    
    def sort2(self, A):
        n = len(A) # store n 
        gap = n // 2 # gap = n / 2 floor
        
        while gap > 0: # while the gap is positive
            for i in range(0, n - gap): # for 0 to n - 1 - gap because when you
                # add gap you get n - 1 for the bottom
                if A[i] > A[i + gap]: # if a point is out of orer
                    # swap
                    A[i], A[i + gap] = A[i + gap], A[i]
                    # end
                    i = i - gap
                    while i >= 0: # get going down the line
                        if A[i] > A[i + gap]:
                            # swap
                            A[i], A[i + gap] = A[i + gap], A[i]
                            # end
                            i = i - gap
                        else:
                            i = i - gap
            gap = gap // 2
        
        return A
            
mjr = ShellSort()
mjr.sort2([5, 2, 7, 8, 3, 1])