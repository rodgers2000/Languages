#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 10:25:52 2018

@author: Mjr
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

m = 50

x = np.linspace(0, 25, m)
y1 = x + np.random.randint(1, 2000, m)
y2 = x**3 + np.random.randint(1, 2000, m)

mpl.style.use('seaborn')

plt.scatter(x, y2, label='line1', color='blue')
plt.plot(x, y2, color='blue')
#plt.plot(x, y2, color='blue')
plt.scatter(x, y1, label='line2', color='orange')
plt.plot(x, y1, color='orange')
#plt.plot(x, y1, color='orange')
plt.legend()
plt.title('beast mode')

plt.savefig("/Users/mrodgers/Documents/other/languages/python/anaconda/spyder/packages/matplotlib/graphs/scatlinelegend.pdf",
            orientation='landscape')
