#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 10:21:50 2018

@author: Mjr

This is my first divide-and-conquer algorithm
You have to get the base case right!
So remember to divide by 2 (or your log base) at each recursive call.
"""


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    return array


def quicksort(array):
    if len(array) <= 1:
        return array
    p = len(array)-1
    array, l, r, p = partition(array, p)
    left = quicksort(array[0:p])
    right = quicksort(array[p:])
#    temp = [left, right]
    temp = left + right
    return temp


def partition(array, p):
    pivot = array[p]
    if array[0] < pivot:
        s = 1
    if array[0] > pivot:
        s = 0
    for idx in range(1, len(array)-1):
        if array[idx] < pivot and array[idx-1] > pivot:
            # swap idx and s
            array = swap(array, idx, s)
            s += 1
        if array[idx] < pivot:
            s += 1
    # swap p and s
    array = swap(array, p, s)
    # return array, l, r, p
    return array, s-1, s+1, s


print quicksort([1, 10, 6, 2, 7, 5, 8, 3, 12])
print quicksort([1, 4, 5, 2, 3])
