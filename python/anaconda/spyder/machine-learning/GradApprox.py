#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 19:34:26 2019

@author: mrodgers
"""

import numpy as np

mean, sd = 10, 20

X = np.random.normal(mean, sd, 100).reshape((10, 10))
Y = np.random.normal(mean, sd, 10).reshape((10, 1))

class GradApprox:
    
    def __init__(self, X, Y):
        self.n = X.shape[0]
        self.p = X.shape[1]
        self.X = X
        self.Y = Y # initialization is very important
        self.B = np.random.normal(0, 1, self.p).reshape((self.p, 1))
        
    def Loss(self):
        loss = 1 / self.n * np.sum(np.power(self.Y - np.dot(self.X, self.B), 2))
        return loss        
     
    def Train(self, reps, cross):
        for i in range(reps):
            for beta in range(len(self.B)):
                # loss without difference added
                y1 = self.Loss()
                # next
                rand_num = np.random.normal(cross, cross, 1)
                self.B[beta] += rand_num
                # loss with difference added
                y2 = self.Loss()
                # calculate delta
                change_y = y2 - y1
                change_x = rand_num
                self.B[beta] += - change_y / change_x
        return self.Loss()
                
mjr = GradApprox(X, Y)
losses = []
for i in [10]:
    a = mjr.Train(1000, i)
    losses.append(a)

print(losses)


### check regular lossk

from sklearn.linear_model import LinearRegression

reg = LinearRegression().fit(X, Y)
my_mse = 1 / 10 * np.sum(np.power(Y - np.dot(X, reg.coef_.reshape((10, 1))), 2))
print(my_mse)

