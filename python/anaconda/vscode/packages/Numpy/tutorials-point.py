import pandas as pd
import numpy as np

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

mjr = pd.DataFrame({'a':a, 'b':b})

size = mjr.shape

for i in range(size[0]):
    for j in range(size[1]):
        print(mjr.iloc[i, j])