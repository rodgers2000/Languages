#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:04:33 2019

@author: mrodgers
"""

import numpy as np
import matplotlib as mpl

x = np.random.normal(0, 10, 100)

mpl.pyplot.hist(x, bins=25, density=True)
mpl.pyplot.title("Michael")
mpl.pyplot.xlabel("Random {}".format("X"))
mpl.pyplot.ylabel("Probability")
mpl.pyplot.savefig("/Users/DirtyMike/Documents/other/languages/python/anaconda/packages/matplotlib/graphs/hist.pdf",
            orientation='landscape')