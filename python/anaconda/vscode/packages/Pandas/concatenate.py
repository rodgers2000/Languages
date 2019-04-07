import pandas as pd
import numpy as np

x = np.arange(10)
y = x ** 2

df1 = pd.DataFrame({'x': x})
df2 = pd.DataFrame({'y': y})

df3 = pd.concat([df1, df2], axis=1)

df4 = pd.DataFrame({'x': [100], 'y': [100]})

df5 = pd.concat([df3, df4], axis=0)
