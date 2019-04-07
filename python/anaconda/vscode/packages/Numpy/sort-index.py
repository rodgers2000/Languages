import numpy as np

a = np.array([1, 5, 3])
b = a[a.argsort(axis=0)]

print(b)

