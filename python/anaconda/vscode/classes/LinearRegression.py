import numpy as np


class LinearRegression():

    def __init__(self, X, Y):
        self.Losses = []
        self.X = X
        self.Y = Y
        self.W = 0
        self.B = 0
        self.getCoefficients()

    def getCoefficients(self):
        self.W = np.zeros((self.X.shape[1], self.Y.shape[1]))
        self.B = np.zeros((1, 1))

    def calculateYhat(self):
        yhats = np.dot(self.X, self.W) + self.B
        return yhats

    def calculateLoss(self):
        operation1 = self.Y - self.calculateYhat()
        loss = 1 / self.X.shape[0] * np.dot(operation1.transpose(), operation1)
        return loss

    def gradientDescent(self, epochs, learning_rate):
        for iter in range(epochs):
            self.Losses.append(self.calculateLoss())
            gradientW = np.dot(self.X.transpose(),
                               self.calculateYhat() - self.Y)
            gradientB = np.sum(self.calculateYhat() - self.Y)
            self.W = self.W - learning_rate * gradientW / self.X.shape[0]
            self.B = self.B - learning_rate * gradientB / self.X.shape[0]
            print(iter, '\n')


m = 1000

X = np.array([np.random.normal(0, 1, m),
              np.random.normal(10, 5, m),
              np.random.normal(5, 20, m)]).transpose()

Y = np.array([np.random.normal(0, 1, m)]).transpose()

mjr = LinearRegression(X, Y)
mjr.gradientDescent(1000, .001)

mjr.W
