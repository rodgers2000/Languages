#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:29:29 2018

@author: Mjr
"""


class Twosum():

    def __init__(self):
        self.target_count = 0
        self.data = []

    def addData(self, pt):
        self.data.append(pt)

    def TwoSum(self, lower, upper):
        for sum_cr in range(lower, upper+1, 1):
            print('current iteration:', sum_cr)
            hash_table = {}
            for i in self.data:
                if (sum_cr - i in hash_table and sum_cr - i != i):
                    self.target_count += 1
                    print('current target count:', self.target_count)
                    break
                hash_table[i] = i


mike = Twosum()

dat = open('prob-2sum.txt', 'r')

for line in dat.readlines():
    mike.addData(int(line))

mike.TwoSum(-10000, 10000)

print('my answer is: ', mike.target_count)
