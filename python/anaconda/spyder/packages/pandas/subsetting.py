#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 20:25:43 2019

@author: mrodgers
"""

mjr = pd.DataFrame(np.random.rand(10, 10))

mjr[mjr[0] <= mjr[1]]
mjr.iloc[:, ist(mjr.columns[0:2])]
mjr[(mjr[0] > .5) & (mjr[1] > .5)]