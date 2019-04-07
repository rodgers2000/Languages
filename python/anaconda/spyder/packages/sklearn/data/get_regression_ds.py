#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 20:16:46 2018

@author: mrodgers
"""

import sklearn.cross_validation  # cv and ds are folders
import sklearn.datasets
import pandas as pd

boston = sklearn.datasets.load_boston()

print(boston.keys())
print(boston.data.shape)
print(boston.feature_names)
print(boston.DESCR)

bos = pd.DataFrame(boston.data)

bos.columns = boston.feature_names

bos['PRICE'] = boston.target

print(bos.head())

# =============================================================================
# SPLITTING TO TRAIN AND TEST DATASETS
# =============================================================================

X = bos.drop('PRICE', axis=1)
Y = bos['PRICE']


X_train, X_test, Y_train, Y_test = sklearn.cross_validation.train_test_split(X, Y, test_size = 0.33, random_state = 5)  #analysis:ignore

print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

ds_REG = {}
ds_REG['X_train'] = X_train
ds_REG['X_test'] = X_test
ds_REG['Y_train'] = Y_train
ds_REG['Y_test'] = Y_test

del X, Y, X_test, X_train, Y_test, Y_train, bos, boston

# =============================================================================
# DATA IS IN (N, P) FORM
# =============================================================================
