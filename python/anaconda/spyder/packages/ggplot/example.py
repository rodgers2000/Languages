#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 22:04:36 2018

@author: Mjr
"""

import numpy as np
from ggplot import *
import pandas as pd

m = 10
x = range(m)
y = x + np.random.randn(m)
labels = np.random.choice(['male', 'female'], m).tolist()

my_df = {'x1': x, 'y1': y, 'label': labels}
my_df = pd.DataFrame(my_df)

ggplot(my_df, aes(x='x1', y='y1', color='labels')) + geom_point() + labs(x='x', y='y', title='beast mode')