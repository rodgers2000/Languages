import numpy as np

a = np.arange(4).reshape((2, 2))
b = np.random.random_integers(0, 10, 4).reshape((2, 2))

# the three different ways
np.vstack((a, b))
np.row_stack((a, b))
np.concatenate((a, b), axis=0)
