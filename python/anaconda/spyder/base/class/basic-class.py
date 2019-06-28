#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 11:02:52 2018

@author: Mjr
"""


class Robot():

    def __init__(self):
        self.age = 10

    def move_up(self):
        print('I moved up.')
        self.age += 1

    def move_down(self):
        print('I moved down.')
        self.age += 1

    def random_move(self):
        self.move_down()
        self.move_up()

    def print_age(self):
        print('I am %d years old' % (self.age))


mike = Robot()

mike.move_down()
mike.move_up()
mike.random_move()
mike.print_age()

mike.year = 2017
mike.nickname = 'dirty mike'

print('my nickname is %s' % (mike.nickname))
