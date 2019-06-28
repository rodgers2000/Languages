#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 14:44:04 2018

@author: Mjr
"""

# =============================================================================
# This demonstrates how an object (point) can be used as a template for a seq.
# =============================================================================


import numpy as np


class Point():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def show_point(self):
        return (self.x, self.y, self.z)


points = []

for i in range(0, 10):
    cord = np.random.randint(1, 10, 3)
    point = Point(cord[0], cord[1], cord[2])
    points.append(point)

for i in points:
    print(i.show_point())
