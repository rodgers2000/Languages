import numpy as np

a = np.array([[[1, 5, 3], [69, 9, 4]], [[2, 4, 2], [6, 9, 8]]])

# the two ways for indexing
# dimension 3, dimension 1, dimension 2
a[0][1][1]
a[1, 0, 0]