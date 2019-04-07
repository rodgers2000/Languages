#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 00:07:35 2018

@author: mrodgers
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.pyplot.style.use('ggplot')

df = pd.read_csv("data/AAPL.csv")

m = 20

df = df.ix[1:m, :]

df['index'] = range(0, m, 1)

plt.plot('index', 'High', data=df, label='high', color='#11DA97', marker='o')

plt.plot('index', 'Low', data=df, label='low', color='#116FDA', marker='x')

plt.ylim(140, 200)
plt.xlim(0, 25)
plt.title('AAPL')
plt.legend()

plt.savefig('graphs/apple-idx.pdf')
