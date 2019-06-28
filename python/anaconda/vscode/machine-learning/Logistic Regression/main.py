import numpy as np
import LogisticRegression as lr
n = 100
p = 50
X = np.random.rand(n, p)
Y = np.random.randint(2, size=n)
theta = np.random.rand(p)

mjr = lr.LogisticRegression(X, Y, theta)
a = mjr.returnone()
