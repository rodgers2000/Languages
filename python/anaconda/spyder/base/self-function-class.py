#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 11:16:59 2018

@author: Mjr
"""


class Coordinate():

    def __init__(self, x):
        self.x = x

    def printX(self):
        print(self.x)

    def setX(self, x):
        self.x = x

    def add(self, num):
        self.x += num

    def subtract(self, num):
        self.x -= num

    def multiple(self, num):
        self.x *= num

    def divide(self, num):
        self.x /= num

    def exponent(self, num):
        self.x = self.x**num

    def my_custom_arithmetic(self, num):
        self.exponent(num)
        self.multiple(num)
        self.divide(num)
        self.add(num)
        self.subtract(num)

    def set_custom_arithmetic(self, func1, func2, arg1, arg2):
        func1(arg1)
        func2(arg2)


mike = Coordinate(10)
#mike.my_custom_arithmetic(2)
#mike.printX()

mike.set_custom_arithmetic(mike.add, mike.subtract, 5, 5)
mike.printX()
