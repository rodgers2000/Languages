#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 13:06:43 2018

@author: Mjr
"""

# =============================================================================
# This can be called multi-level inheritance.
# =============================================================================


class One():

    global_var = 1000

    def __init__(self):
        self.dat_one = 1
        super(One, self).__init__()
        print(1)

    def one(self):
        print('class one')


class Two():

    def __init__(self):
        self.dat_two = 2
        super(Two, self).__init__()
        print(2)

    def two(self):
        print('class two')


class Three():

    def __init__(self):
        self.dat_three = 3
        super(Three, self).__init__()
        print(3)

    def three(self):
        print('class three')


class Mega(One, Two, Three):

    def __init__(self):
        super(Mega, self).__init__()
        # the initializer is called in order (3, 2, 1)


mike = Mega()
mike.one()
mike.two()
mike.three()

print(mike.dat_one, mike.dat_two, mike.dat_three)
print(mike.global_var)
