#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 11:53:53 2019

@author: mrodgers
"""

import pandas as pd

mjr = pd.DataFrame()
mjr2 = pd.DataFrame({"a": [1, 2]})
mjr3 = pd.DataFrame({'b': [3, 4]})
mjr4 = pd.concat([mjr, mjr2])
mjr5 = pd.concat([mjr2, mjr3], axis=1)