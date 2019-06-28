import methods.funcs
import pandas as pd

for i in range(10):
    for j in range(10):
        print(funcs.func1(i))

def mjr(a = 10, b = 20):
        return a + b 

name = ["Mike", "Tom", "Sally"]
age = [23, 57, 44]
data = list(zip(name, age)) 
df = pd.DataFrame(data, columns = ['Name', 'Age'])

for index, row in df.iterrows():
        print(row['Age'])


import numpy as np

mjr = np.arange(10).reshape((5, 2))

for i in range(mjr.shape[0]):
        for j in range(mjr.shape[1]):
                print(mjr[i, j]*2)
