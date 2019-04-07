#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 20:32:45 2018

@author: Mjr
"""

class DS():
    pass

mybook = DS()

mybook.x = 10
mybook.y = [1, 2, 3]
mybook.z = [[1, 2, 3], [4, 5, 6]]

print mybook.x, mybook.y, mybook.z

getattr(mybook, dir(mybook)[2:][1])

mylap = {}
mylap['x'] = 1
mylap['y'] = 2
mylap['z'] = [1, 2, 3]

print mylap['x'], mylap['y'], mylap['z']

#### function calls

def this_func(x, data):
    data[str(x)] = x
    return data

print this_func(10, {})