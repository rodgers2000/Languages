#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:52:00 2019

@author: mrodgers
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

m = 100
x = np.random.normal(0, 10, m).reshape(25, 4)
y = np.random.choice([0, 1], int(m / 4))

X_train, X_test, y_train, y_test = train_test_split(x, y, train_size=.75, stratify=y)

pipeline = make_pipeline(StandardScaler(), 
                         RandomForestClassifier())

pipeline.get_params()['randomforestclassifier']

hyperparameters = { 'randomforestclassifier__max_features' : ['auto', 'sqrt', 'log2'],
                  'randomforestclassifier__max_depth': [None, 5, 3, 1], 
                  'randomforestclassifier__n_estimators': [10, 100, 1000]}

clf = GridSearchCV(pipeline, hyperparameters, cv=3)
clf.fit(X_train, y_train)
y_preds = clf.predict(X_test)

accuracy_score(y_test, y_preds)
