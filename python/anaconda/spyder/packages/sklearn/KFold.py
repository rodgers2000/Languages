#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 16:43:37 2019

@author: mrodgers
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold

m = 100
x = np.random.normal(0, 10, m).reshape(25, 4)
y = np.random.choice([0, 1], int(m / 4))

kf = KFold(n_splits = 4)

for train_index, test_index in kf.split(x, y):
    print(train_index)
    print(test_index)
    
#indexes = list(range(x.shape[0]))
indexes = 26
folds = 4

groups = []

holder = int(indexes / folds)
remainder = indexes % folds 

for i in range(folds - 1):
    groups.append(list(range(holder * i, holder * i + holder)))
    
groups.append(list(range(holder * (folds - 1), holder * (folds - 1) + holder + remainder)))

test = []
train = []

for i in range(folds):
    test.append(groups[i])
    temp = []
    for j in range(folds):
        if j != i:
            temp.append(groups[j])
    train.append(temp)

#print(train[0])
mjr = []
for i in train:
    train_final = []
    for j in i:
            for k in j:
                train_final.append(k)
    mjr.append(train_final)
    
print(mjr)
        
mjr = []
for i in range(len(train)):
    train_final = []
    for j in range(len(train[i])):
            for k in range(len(train[i][j])):
                train_final.append(train[i][j][k])
    mjr.append(train_final)
    

for i in mjr:
    print(i)
