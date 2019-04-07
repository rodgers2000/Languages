#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 11:24:20 2018

@author: Mjr
"""

# =============================================================================
# You can call the current way multiple inheritance.
# This is the site for the comparison between multiple and multi-level.
# https://www.journaldev.com/14623/python-multiple-inheritance
# =============================================================================


class One():

    global_var = 1000

    def __init__(self, num):
        self.dat_one = num
        print(1)

    def one(self):
        print('class one')


class Two():

    def __init__(self, num):
        self.dat_two = num
        print(2)

    def two(self):
        print('class two')


class Three():

    def __init__(self, num):
        self.dat_three = num
        print(3)

    def three(self):
        print('class three')


class Mega(One, Two, Three):

    def __init__(self):
        One.__init__(self, 1)  # the initializer is called in order (1, 2, 3)
        Two.__init__(self, 2)
        Three.__init__(self, 3)


# with inheritance, all methods and attributes are
# in the scope of the super class.
# methods
mike = Mega()
mike.one()
mike.two()
mike.three()
# attributes
print(mike.dat_one, mike.dat_two, mike.dat_three)
print(mike.global_var)
