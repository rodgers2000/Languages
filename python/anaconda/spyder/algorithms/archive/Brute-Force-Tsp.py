#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 21:54:40 2018

@author: Mjr
"""

import numpy as np

import math
import itertools


class TSP():

    def __init__(self):
        self.cities = {}  # map to city and coords
        self.Dist = 0
        self.total = math.factorial(25)

    def addData(self, index, x, y):
        self.cities[index] = (x, y)

    def calculateDist(self):
        Dist = np.zeros((25, 25))
        for i in range(0, 25, 1):
            for j in range(0, 25, 1):
                x_d = (self.cities[i][0] - self.cities[j][0])
                y_d = (self.cities[i][1] - self.cities[j][1])
                x_d = math.pow(x_d, 2)
                y_d = math.pow(y_d, 2)
                Dist[i][j] = math.sqrt(x_d + y_d)
        self.Dist = Dist

    def bruteForce(self):
        pathvalues = []
        paths = itertools.permutations(range(0, 25, 1))
        for counter, path in enumerate(paths):
            print(round(counter / self.total * 100, 7), counter)
            pathvalues.append(self.pathValue(path))
        self.pathvalues = pathvalues

    def pathValue(self, path):
        index = 0
        cum_dist = 0
        while index != len(path):
            a = 0
            b = 1
            cum_dist += self.Dist[path[a], path[b]]
            # update
            a += 1
            b += 1
            index += 1
            if index == (len(path) - 1):
                cum_dist += self.Dist[path[-1], path[0]]
                break
        return cum_dist

    def returnMin(self):
        return min(self.pathvalues)


mike = TSP()
mydata = open('tsp.txt', 'r')
index = 0
for line in mydata.readlines()[1:]:
    my_info = line.split(' ')
    mike.addData(index, float(my_info[0]), float(my_info[1]))
    index += 1

mike.calculateDist()
mike.bruteForce()
print('my answer is: ', mike.returnMin())
