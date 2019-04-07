import numpy as np

X = np.arange(30).reshape((2, 3, 5))

for axis0 in range(X.shape[0]):
    for row in range(X.shape[1]):
        for col in range(X.shape[2]):
            val = X[axis0, row, col]
            print(val)
