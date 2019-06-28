import numpy as np

n = 100
p = 50
X = np.random.rand(n, p)
Y = np.random.randint(2, size=n)
theta = np.random.rand(p)

class LogisticRegression:

    def __init__(self, X, Y, theta):
        self.X = X
        self.Y = Y
        self.theta = theta

    def sigmoid(self):
        num = 1 
        den = 1 + np.exp(-np.dot(self.X, self.theta))
        return num / den

    def returnone(self):
        return [1, 2, 3]

mjr = LogisticRegression(X, Y, theta)
a = mjr.returnone()