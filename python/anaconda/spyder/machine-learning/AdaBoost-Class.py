import numpy as np
from sklearn.tree import DecisionTreeClassifier

class AdaBoost:
    
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.n = X.shape[0]
        self.p = X.shape[1]
        self.w = np.repeat(1, X.shape[0]) / X.shape[0]
        self.G = []
        self.a = []
        
    def run(self, times):
        for m in range(times):
            # a
            clf = DecisionTreeClassifier(max_depth = 1, random_state = 1)
            clf.fit(self.X, self.Y, sample_weight = self.w)
            self.G.append(clf)
            # b
            yhats = clf.predict(self.X)
            err = 0
            for i in range(n):
                if self.Y[i] != yhats[i]:
                    err += self.w[i]
            err = err / sum(self.w) 
            # c
            a = np.log((1 - err) / err)
            self.a.append(a)
            # d 
            for i in range(len(self.w)):
                factor = 0
                if self.Y[i] != yhats[i]:
                    factor = a
                self.w[i] = self.w[i] * np.exp(factor)
                
    def predict(self):
        yhats = []
        for i in range(n):
            output = 0
            for j in range(len(self.a)):
                output += self.a[j] * self.G[j].predict(X[i:i+1, :])
            if output > 0:
                yhats.append(1)
            else:
                yhats.append(-1)
            self.yhats = yhats      


n, p = 50, 50

X = np.random.rand(n, n)
Y = np.random.choice([1, -1], n)

mjr = AdaBoost(X, Y)
mjr.run(5)
mjr.predict()
print(np.sum(mjr.yhats == Y) / len(Y))
clf = DecisionTreeClassifier(max_depth = 1, random_state = 1)
clf.fit(X, Y)
yhats = clf.predict(X)
print(np.sum(yhats == Y) / len(Y))
                