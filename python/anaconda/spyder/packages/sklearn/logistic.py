#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 20:10:10 2018

@author: mrodgers
"""

# for regression

try:
    runfile('/Users/mrodgers/Documents/other/languages/python/anaconda/packages/sklearn/data/get_regression_ds.py')  #analysis:ignore
except:
    print(' ')

import matplotlib.pyplot as plt
import sklearn.linear_model
import numpy as np

n = ds_REG['X_train'].shape[0]

ols = sklearn.linear_model.LinearRegression()

ols.fit(ds_REG['X_train'], ds_REG['Y_train'])

yhats = {}

yhats['Test'] = ols.predict(ds_REG['X_test'])
yhats['Train'] = ols.predict(ds_REG['X_train'])

mspe = {}

mspe['Train'] = 1 / n * np.sum(np.power(yhats['Train'] - ds_REG['Y_train'], 2))
mspe['Test'] = 1 / n * np.sum(np.power(yhats['Test'] - ds_REG['Y_test'], 2))


print('Train mspe: ' + str(mspe['Train']))
print('Test mspe: ' + str(mspe['Test']))


plt.style.use('ggplot')

plt.scatter(x=range(1, 11), y=np.power(range(1, 11), 2))

plt.savefig('/Users/mrodgers/Documents/other/languages/python/anaconda/packages/sklearn/figures/omg.pdf')