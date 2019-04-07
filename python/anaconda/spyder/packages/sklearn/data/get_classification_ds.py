#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 20:51:36 2018

@author: mrodgers
"""

import sklearn.cross_validation  # cv and ds are folders
import sklearn.datasets
import pandas as pd
import numpy as np

digits = sklearn.datasets.load_digits()

print(digits.keys())
print(digits.target_names)
print(digits.data.shape)
print(digits.target.shape)

X = np.array(digits.data)
X = X.reshape(X.shape[0], -1)
Y = digits.target

print(X.shape, Y.shape)

# =============================================================================
# SPLITTING TO TRAIN AND TEST DATASETS
# =============================================================================


X_train, X_test, Y_train, Y_test = sklearn.cross_validation.train_test_split(X, Y, test_size = 0.33, random_state = 5)  #analysis:ignore

print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

ds_CLS = {}
ds_CLS['X_train'] = X_train
ds_CLS['X_test'] = X_test
ds_CLS['Y_train'] = Y_train
ds_CLS['Y_test'] = Y_test

del X, Y, X_test, X_train, Y_test, Y_train, digits

# =============================================================================
# DATA IS IN (N, P) FORM
# =============================================================================
