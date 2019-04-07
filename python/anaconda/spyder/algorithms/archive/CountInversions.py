#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 11:21:21 2018

@author: Mjr
"""

def merge_and_count(a2, a3):
    res_arr, inv_count = [], 0
    while len(a2) > 0 or len(a3) > 0:
        if len(a2) > 0 and len(a3) > 0:
            if a2[0] < a3[0]:
                res_arr.append(a2[0])
                a2 = a2[1:]
            else:
                res_arr.append(a3[0])
                a3 = a3[1:]
                inv_count += len(a2)
        elif len(a2) > 0:
            res_arr.append(a2[0])
            a2 = a2[1:]
        elif len(a3) > 0:
            res_arr.append(a3[0])
            a3 = a3[1:]
            
    return res_arr, inv_count

def sort_and_count(a1):
    arr_len = len(a1)
    if arr_len <= 1:
        return a1, 0
    a2,x = sort_and_count(a1[:(arr_len/2)])
    a3,y = sort_and_count(a1[(arr_len/2):])
    a4,z = merge_and_count(a2, a3)
    
    return a4, x+y+z

t1 = [1,3,5,2,4,6,7]
print "Testing using", t1
print "Expecting:", 3
print "Returned:", sort_and_count(t1)[1]

# change working directory
import os

os.chdir('/Users/DirtyMike/Desktop/coursera/stanford/course-1/assignments/1/')

filename = 'IntegerArray.txt' 
fin=open(filename,'r')
my_vec = []
for line in fin.readlines():
    my_vec.append(int(line))
    
print "Returned:", sort_and_count(my_vec)[1]
