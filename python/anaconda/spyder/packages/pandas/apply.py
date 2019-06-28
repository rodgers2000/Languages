#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:25:54 2019

@author: mrodgers
"""

import pandas as pd

a = list(range(5))
b = [6, 7, 8, 9, 10]

mjr = pd.DataFrame()

mjr['a'] = a
mjr['b'] = b

mjr.apply([sum, len, 'mean'], axis=0)

mjr.apply(lambda x: x + 1, axis=0)

