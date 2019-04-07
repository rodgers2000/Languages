import numpy as np
import pandas as pd

m = 10
x = np.random.choice([0, 1, 2], m, replace=True)
y = np.random.normal(0, 1, size=m)

df = {}
df['x'] = x
df['y'] = y

df_temp = pd.DataFrame(df)

for row in range(df_temp.shape[0]):
    for col in range(df_temp.shape[1]):
        val = df_temp.iloc[row, col]
        print(val)
    print("\n")
