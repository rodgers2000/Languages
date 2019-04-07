import numpy as np

a = np.arange(20)

b = a.reshape(10, -1)

print(b.shape)
