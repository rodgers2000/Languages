#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 17:36:31 2019

@author: mrodgers
"""

# 2. Import libraries and modules
import numpy as np
import pandas as pd
 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
 
# 3. Load red wine data.
X = np.random.rand(100, 10)
y = np.random.choice([0, 1], 100)
 
# 4. Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=123, 
                                                    stratify=y)

steps = [('one', StandardScaler()), ('two', SVC())]

pipeline = Pipeline(steps)

parameters = {'two__C':[.01, .1, 10], 'two__gamma':[.1, .01]}

grid = GridSearchCV(pipeline, param_grid=parameters, cv=2, n_jobs=-1)

grid.fit(X, y)

grid.score(X_test, y_test)
grid.best_params_
