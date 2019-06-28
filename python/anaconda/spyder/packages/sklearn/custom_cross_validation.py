#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 13:05:08 2019

@author: mrodgers
"""

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score

x = np.random.normal(0, 1, 1000).reshape(100, 10)
y = np.random.choice([0, 1], 100)

parameters = {}
parameters['n_estimators'] = [10, 100]
parameters['max_depth'] = [1, 3, 5]
parameters['min_samples_split'] = [2, 4, 6]

def create_array(parameters):
    length = []
    for key, value in parameters.items():
        length.append(len(value))
    
    return np.zeros([i for i in length])

array_of_zeros = create_array(parameters)

def cross_validation_mjr(parameters, array_of_zeros):
    i = 0
    for n_estimator in parameters['n_estimators']:
        j = 0
        for max_depth in parameters['max_depth']:
            k = 0 
            for min_samples_split in parameters['min_samples_split']:
                cv_accuracy = []
                kf = KFold(n_splits=5)
                for train_index, test_index in kf.split(x, y):
                    x_train, x_test = x[train_index], x[test_index]
                    y_train, y_test = y[train_index], y[test_index]
                    rf = RandomForestClassifier(n_estimators=n_estimator, 
                                                max_depth=max_depth,
                                                min_samples_split=min_samples_split)
                    rf.fit(x_train, y_train)
                    y_preds = rf.predict(x_test)
                    accuracy = accuracy_score(y_test, y_preds)
                    cv_accuracy.append(accuracy)
                    
                cv_mean = sum(cv_accuracy) / len(cv_accuracy)
                array_of_zeros[i, j, k] = cv_mean
                k += 1
            j += 1
        i += 1
        return array_of_zeros
    
array_of_scores = cross_validation_mjr(parameters, array_of_zeros)

def find_max_score(array_of_scores):
    maximum = 0
    max_index = (0, 0, 0)
    shapes = array_of_scores.shape
    for i in range(shapes[0]):
        for j in range(shapes[1]):
            for k in range(shapes[2]):
                if array_of_scores[i, j, k] > maximum:
                    max_index = (i, j, k)
                    maximum = array_of_scores[i, j, k]
    return max_index

max_index = find_max_score(array_of_scores)
i = 0 
optimal = {}
for key, value in parameters.items():
    optimal[key] = value[max_index[i]]
    i += 1

print(optimal)







            