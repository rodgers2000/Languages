#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 19:39:24 2018

@author: Mjr
"""


class NaiveKnapsack():

    def __init__(self, ks, n):
        self.V = {}
        self.W = {}
        self.ks_size = ks
        self.i_size = n

    def addData(self, index, v, w):
        self.V[index] = v
        self.W[index] = w

    def knapSack(self):
        # make matrix A
        A = []
        for i in range(0, self.i_size + 1, 1):
            row = [0] * (self.ks_size + 1)  # populate with 0's
            A.append(row)
            print(i)

        print(len(A), len(A[0]))

        for i in range(1, self.i_size + 1, 1):
            for w in range(0, self.ks_size + 1, 1):
                print(i, w)
                if self.W[i] < w:
                    A[i][w] = max(A[i - 1][w], self.V[i] + A[i - 1][w - self.W[i]])  #analysis:ignore
                else:
                    A[i][w] = A[i - 1][w]

        return A[self.i_size][self.ks_size]


dat = open('knapsack_big.txt', 'r')
index = 0
for line in dat.readlines():
    line = line.split(' ')
    if index == 0:
        mike_ks = NaiveKnapsack(int(line[0]), int(line[1]))
    else:
        mike_ks.addData(index, int(line[0]), int(line[1]))
    index += 1
    print(index)

print('my answer is: ', mike_ks.knapSack())
