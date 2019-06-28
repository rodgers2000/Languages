#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:10:49 2019

@author: mrodgers
"""

import datetime as dt
import pandas as pd


mjr = dt.datetime(year=2015, month=7, day=4, hour=12, minute=20, second=5, microsecond=10000)

mjr + dt.timedelta(seconds=10)

dates = []

for i in range(10):
    dates.append(mjr + dt.timedelta(seconds=i))
    
mjr = pd.DataFrame()
mjr['a'] = range(10)
mjr['time'] = dates 

mjr = mjr.set_index('time')
mjr[mjr.index <= '2015-{}-04 12:{}:10'.format(7, 20)]
mjr.index.second > 10

mjr.loc[mjr['a'] > 5, :]



""" strip date """

mjr = dt.datetime.strptime('09-06-1995 12:20:10', '%m-%d-%Y %H:%M:%S')
