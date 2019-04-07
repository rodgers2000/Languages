#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 11:15:14 2018

@author: Mjr
"""


class Person():

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self, first, last)
        self.staffnumber = staffnum

    def __str__(self):
        return self.firstname + " " + self.lastname + ", " + self.staffnumber


x = Person('mike', 'rodgers')
y = Employee('mike', 'rodgers', '2000')

print(x)
print(y)
print(y.firstname)
