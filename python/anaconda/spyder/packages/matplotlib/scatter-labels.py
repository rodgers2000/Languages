#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 00:32:11 2018

@author: Mjr
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.style.use('default')

m = 150

x = np.arange(-m, m, 1)
y = x**2 + np.random.normal(250, 2500, 2*m)
label = np.random.choice(range(10), 2*m)
size = np.random.randint(1, 200, 2*m)

my_df = {'x': x, 'y': y, 'label': label, 'size': size}

plt.scatter(x='x', y='y', c='label', s='size', data=my_df)
plt.xlabel('x')
plt.ylabel('y')
plt.title('$y = x^2 + \epsilon$')

plt.savefig("/Users/DirtyMike/Documents/other/languages/python/anaconda/packages/matplotlib/graphs/mike.pdf",
            orientation='landscape')
