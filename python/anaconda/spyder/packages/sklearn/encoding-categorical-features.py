#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:55:01 2019

@author: mrodgers
"""

import pandas as pd
import numpy as np

mjr = pd.DataFrame()

mjr['a'] = np.arange(5)
mjr['b'] = np.random.choice(['cat', 'dog'], size=5)
mjr['c'] = np.random.choice(['one', 'two', 'three'], size=5)

names = ['a']
for col in mjr.columns[1:len(mjr.columns)]:
    temp = mjr[col]
    values = temp.unique()
    names.extend(values)

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

le = LabelEncoder()

categorical_feature_mask = mjr.dtypes == object
categorical_cols = mjr.columns[categorical_feature_mask].tolist()

mjr[categorical_cols] = mjr[categorical_cols].apply(lambda col: le.fit_transform(col))

print(mjr)

categorical_feature_mask

ohe = OneHotEncoder(categorical_features=categorical_feature_mask, sparse=False)

X_ohe = ohe.fit_transform(mjr)

mjr2 = pd.DataFrame(X_ohe)
mjr2.columns = names


print(mjr2) # b, c, a
print(mjr)
