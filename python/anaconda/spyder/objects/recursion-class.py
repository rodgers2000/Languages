#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 11:03:13 2018

@author: Mjr
"""


class Recursion():

    def __init__(self):
        pass

    def fibonacci(self, start):
        if start == 1:
            return 1
        if start == 0:
            return 0
        return self.fibonacci(start - 1) + self.fibonacci(start - 2)


mike = Recursion()

for i in range(0, 10, 1):
    print(i, end=' ')
    print(mike.fibonacci(i), end='\n')
