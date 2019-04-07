#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 21:53:01 2018

@author: mrodgers
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.pyplot.style.use('ggplot')

df = pd.read_csv("data/AAPL.csv")

df = df.ix[0:20, :]

df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d')

fig, ax = plt.subplots()

ax.plot('Date', 'High', data=df, label='high', color='#11DA97', marker='o')

ax.plot('Date', 'Low', data=df, label='low', color='#116FDA', marker='x')

fig.autofmt_xdate()

ax.set_title('AAPL')

fig.legend()

plt.savefig('graphs/apple-date.pdf')
