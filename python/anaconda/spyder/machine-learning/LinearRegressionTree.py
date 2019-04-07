#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:34:21 2019

@author: mrodgers
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

mean, sd = 0, 10

X = np.random.normal(mean, sd, 100).reshape((10, 10))
Y = np.random.normal(mean, sd, 10).reshape((10, 1))
X_test = np.random.normal(mean, sd, 100).reshape((10, 10))
Y_test = np.random.normal(mean, sd, 10).reshape((10, 1))

class LinearReg:
    
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        
    def train(self):
        reg = LinearRegression().fit(self.X, self.Y)
        self.reg = reg
        
    def predict(self, X):
        return self.reg.predict(X)
    

def pipeline(X, Y):
    models = [] # each element in B is a prediction
    for i in range(20):
        if i == 0:
            reg = LinearReg(X, Y)
            reg.train()
            B = reg.predict(X)
            models.append(reg)
        else:
            reg = LinearReg(X, Y)
            reg.train()
            C = reg.predict(X)
            B = np.hstack((B, C))
            models.append(reg)
    return B

B = pipeline(X_test, Y)
reg = LinearReg(B, Y)
reg.train() 
yhat = reg.predict(B)
print(mean_squared_error(Y_test, yhat))

""""
regular regression
"""

reg = LinearReg(X, Y)
reg.train()
yhat = reg.predict(X_test)
print(mean_squared_error(Y_test, yhat))