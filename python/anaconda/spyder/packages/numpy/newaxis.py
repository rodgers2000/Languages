#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 20:38:05 2019

@author: mrodgers
"""

import numpy as np

mjr = np.arange(5)

row_vec = mjr[np.newaxis, np.newaxis, :]
col_vec = mjr[:, np.newaxis]
