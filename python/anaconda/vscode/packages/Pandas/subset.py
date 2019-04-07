import numpy as np
import pandas as pd

m = 200
x = np.random.choice([0, 1, 2], m, replace=True)
y = np.random.normal(0, 1, size=m)

df = {}
df['x'] = x
df['y'] = y

df_temp = pd.DataFrame(df)

condition1 = df_temp.x == 1
df_subset = df_temp[condition1]

df_subset = df_temp[df_temp['x'] == 1]
