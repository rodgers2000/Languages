#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:59:47 2019

@author: mrodgers
"""

from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class LinearRegCV:
        
    def __init__(self, X, Y):
        
        self.X = X
        self.Y = Y
        self.F = KFold(n_splits = 5)
        
    def run(self):
        
        train_errors = []
        test_errors = []
        for train_index, test_index in self.F.split(self.X):
            
            X_train, X_test = self.X[train_index], self.X[test_index]
            Y_train, Y_test = self.Y[train_index], self.Y[test_index]
            reg = LinearRegression().fit(X_train, Y_train)
            yhat_train = reg.predict(X_train)
            yhat_test = reg.predict(X_test)
            
            mse_train = mean_squared_error(Y_train, yhat_train)
            mse_test = mean_squared_error(Y_test, yhat_test) 
            
            train_errors.append(mse_train)
            test_errors.append(mse_test)
        train_error = sum(train_errors) / len(train_errors)
        test_error = sum(test_errors) / len(test_errors)
        
        return (train_error, test_error)
            
            
import numpy as np
X = np.random.rand(200, 50)
Y = np.random.rand(200, 1)

mjr = LinearRegCV(X, Y)
mjr.run()