#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:25:27 2019

@author: mrodgers
"""

import pandas as pd
from datetime import datetime

df_ts = pd.read_csv('/Users/mrodgers/Documents/other/languages/python/anaconda/spyder/projects/data/sp500.csv')

""" convert Date column to datetime """
dates = []
for i in df_ts['Date'].values:
    temp = datetime.strptime(i, '%Y-%m-%d')
    dates.append(temp)
    
df_ts['Date'] = dates

""" find unique months"""

months = []
for i in dates:
    if i.month not in months:
        months.append(i.month)
        
months.sort()

""" find unique years """

years = []
for i in dates:
    if i.year not in years:
        years.append(i.year)

""" find indexes that correspond to the month and year """

data = {}
for year in years:
    for month in months:
        this_data = []
        counter = 0
        for i in df_ts['Date']:
            if i.month == month and i.year == year:
                this_data.append(counter)
            counter += 1
        data[datetime(year=year, month=month, day=1)] = this_data

""" subset the dataframe by index for each month and year """

mjr = {}
for key, value in data.items():
    mjr[key] = df_ts.iloc[value]
    
for year in years:
    for month in months:
        temp = mjr[datetime(year, month, 1)]


""" get rid of empty dataframe """

mjr2 = {}

for key, value in mjr.items():
    if mjr[key].shape[0] == 0:
        next
    else:
        mjr2[key] = value

""" calculate percent change """

mjr3 = {}

for key, value in mjr2.items():
    diff = (value.Close.iloc[value.shape[0]-1] - value.Close.iloc[0]) / value.Close.iloc[0] * 100
    mjr3[key] = diff
    

""" for each month, create a vector of percent changes and then take the mean"""

month_perc = {}
for month in months:
    month_perc[month] = []

for key, value in mjr3.items():
    month_perc[key.month].append(value)
    
for key, value in month_perc.items():
    month_perc[key] = sum(value) / len(value)
    
print(month_perc)

""" put this into a dataframe and export to csv"""

months = []
avg_perc_chg = []

for key, value in month_perc.items():
    months.append(key)
    avg_perc_chg.append(value)
    
omg = {}
omg['months'] = months
omg['avg perc chg'] = avg_perc_chg

pd.DataFrame(omg).to_csv('/Users/mrodgers/Documents/other/languages/python/anaconda/spyder/projects/data/avg_perc_chg_by_month.csv', index=False)















