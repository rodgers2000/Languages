#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 20:39:03 2019

@author: mrodgers
"""

import numpy as np

n = 20
p = 50
X = np.random.rand(n, p)
Y = np.random.randint(2, size=n)
theta = np.random.rand(p)

class LogisticRegression:

    def __init__(self, X, Y, theta):
        self.X = X
        self.Y = Y
        self.theta = theta

    def sigmoid(self):
        num = 1 
        den = 1 + np.exp(-np.dot(self.X, self.theta))
        self.sigmoids = num / den 
    
    def calc_loss(self):
        self.sigmoid()
        this_sum = 0 
        for i in range(len(self.Y)):
            if self.Y[i] == 1:
                this_sum += np.log(self.sigmoids[i])
            else:
                this_sum += np.log(1 - self.sigmoids[i])
        return -this_sum

    def gradientDesc(self, epochs, learning_rate):
        
        for epoch in range(epochs):
            print(self.calc_loss())
            for theta_j in range(len(self.theta)):
                this_sum = 0 
                for i in range(len(self.Y)):
                    this_sum += (self.sigmoids[i] - self.Y[i]) * self.X[i, theta_j]
                self.theta[theta_j] -= learning_rate * this_sum
                
    def gradientDesc2(self, learning_rate, epochs):
        for epoch in range(epochs):
            print(self.calc_loss())
            dz = self.sigmoids - self.Y
            dw = 1 / n * np.matmul(self.X.T, dz)
            self.theta -= learning_rate * dw
                    
                

mjr = LogisticRegression(X, Y, theta)
b = mjr.calc_loss()
#mjr.gradientDesc(10, .001)
mjr.gradientDesc2(.01, 10)