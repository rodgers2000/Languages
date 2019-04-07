import sklearn.cross_validation  # cv and ds are folders
import sklearn.datasets
import numpy as np
import pandas as pd

# pylint: disable=C0321u 

""" 
There are two ways to book data. One is through a dictionary; the other is through a class. 
I think the class way is simpler because one does not have to worry about qoutes and brackets, but rather only has to remember the name and the .
 """

class GetData():

    def __init__(self, test_size):
        self.Brain = []
        self.test_size = test_size

    def saveData(self): 
        self.Brain['Train'] = {}
        self.Brain['Val'] = {}
        self.Brain['Train']['X'] = self.X_train
        self.Brain['Train']['Y'] = self.Y_train
        self.Brain['Val']['X'] = self.X_val
        self.Brain['Val']['Y'] = self.Y_val

    def saveData2(self):
        
        class Brain():
            pass
        
        Book = Brain()
        Book.train = Brain()
        Book.train.x = self.X_train 
        Book.train.y = self.Y_train
        Book.val = Brain()
        Book.val.x = self.X_val
        Book.val.y = self.Y_val
        self.Brain = Book

    def digits(self):
        # load data
        digits = sklearn.datasets.load_digits()
        # transform data
        X = np.array(digits.data) 
        X = X.reshape(X.shape[0], -1)
        Y = digits.target 
        # split data and save data
        self.X_train, self.X_val, self.Y_train, self.Y_val = sklearn.cross_validation.train_test_split(X, Y, test_size = self.test_size, random_state = 5)
        # save data
        self.saveData2()
        return self.Brain

    def boston(self):
        # load data
        boston = sklearn.datasets.load_boston()
        # transform data
        bos = pd.DataFrame(boston.data)
        bos.columns = boston.feature_names
        bos['PRICE'] = boston.target
        X = bos.drop('PRICE', axis=1)
        Y = bos['PRICE']
        # split data and save
        self.X_train, self.X_val, self.Y_train, self.Y_val = sklearn.cross_validation.train_test_split(X, Y, test_size = self.test_size, random_state = 5)
        self.saveData2()
        return self.Brain

mjr = Data(.33)

ds = mjr.boston()