#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:33:07 2019

@author: mrodgers
"""

class QuickSort:
    
    def __init__(self, A):
        self.A = A
        
    def swap(self, i, j):
        temp = self.A[i] # get first element
        self.A[i] = self.A[j] # swap i with j 
        self.A[j] = temp # swap j with i 
        
    def quicksort(self, first, last):
        if first < last: # if there are two or more elements, sort it
            split = self.partition(first, last) # find pivot place holder
            self.quicksort(first, split - 1) # sort left numbers from pivot
            self.quicksort(split + 1, last) # sort right numbers from pivot
        
    def partition(self, first, last):
        pivot = self.A[first] # use first element as pivot
        left = first + 1 # left goes one from pivot
        right = last # right is last index
        
        done = False 
        
        while not done:
            # the left elements must be less than the pivot
            # so keep going till you find one that is greater than the pivot
            while left <= right and self.A[left] <= pivot:
                left += 1
            # the right elements must be greater than tne pivot
            # so keep going till you find one that is less than the pivot
            while left <= right and self.A[right] >= pivot:
                right -= 1
            # if we crossed, and the left will always cross first, we are done
            if right < left:
                done = True
            else:
                # else, we arent done. swap the left and right
                self.swap(left, right)
        # if we are done, swap with the right
        # this is true because left will be greater than right 
        # so we are left with elements less than the pivot at the right spot
        # so swap right with first will give elements less than pivot to the left. 
        self.swap(first, right)
        return right
        
A = [5, 1, 4, 3, 6]
mjr = QuickSort(A)
mjr.quicksort(0, len(A) - 1)
mjr.A
        