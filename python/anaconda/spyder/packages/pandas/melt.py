#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 21:22:35 2019

@author: mrodgers
"""

import pandas as pd
df = pd.DataFrame({'A': [0, 1, 2, 3],
                   '2018': [4, 5, 6, 7],
                   '2019': [8, 9, 10, 11]})

df = df.melt(id_vars=['A'], var_name='year', value_name='data')

df.pivot(index='A', columns='year', values='data')
