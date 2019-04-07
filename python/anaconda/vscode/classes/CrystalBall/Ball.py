import numpy as np
import sklearn

class Ball:
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.X = np.random.rand(n, p)
        self.Y = np.random.choice([0, 1], n)
        self.Beta = np.random.rand(p, 1)
        print(self.Y)
    
    def speaktootherside(self):
        model = sklearn.neighbors.KNeighborsClassifier(n_neighbors=50)
        model.fit(self.X, self.Y)
        yhat = model.predict(np.random.rand(1, self.p))
        print(yhat)
        if yhat == 1:
            print("yes")
        else:
            print("no")

mjr = Ball(10000, 10)
mjr.speaktootherside()