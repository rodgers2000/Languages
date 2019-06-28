#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:14:53 2019

@author: mrodgers
"""

import pandas as pd

df_iris = pd.read_csv('data/iris.csv')

""" sort dataframe """

df_iris.sort_values(df_iris.columns[0], ascending=True)

""" rename column """

values = [i.replace('.', '_') for i in df_iris.columns]

mjr = {}

for i in range(len(values)):
    mjr[df_iris.columns[i]] = values[i]

df_iris.rename(columns = mjr)

""" drop columns """

df_iris.drop(columns = ['variety', 'petal.width'])

""" subset rows """

df_iris[list(df_iris['sepal.length'] > 5)]

""" select column """

list(df_iris.variety)
df_iris.filter(regex='sepal')

""" group by """

mjr = df_iris.groupby(by='variety').agg(['sum', 'mean', 'median'])
mjr.to_csv('data/stats2.csv')

""" apply """

df_iris.iloc[:, list(range(4))].apply(lambda x: sum(x) / len(x), axis=0)

""" plot """

df_iris['sepal.length'].plot()

