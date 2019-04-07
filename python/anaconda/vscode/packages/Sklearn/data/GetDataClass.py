import sklearn.cross_validation # cv and ds are folders
import sklearn.datasets
import numpy as np
import pandas as pd

# pylint: disable=C0321

""" 
There are two ways to book data. One is through a dictionary; the other is through a class. 
I think the class way is simpler because one does not have to worry about qoutes and brackets, but rather only has to remember the name and the .
 """

class Boston():

	def boston(self, test_size):
		# load data
		boston = sklearn.datasets.load_boston()
		# transform data
		bos = pd.DataFrame(boston.data)
		bos.columns = boston.feature_names
		bos['PRICE'] = boston.target
		X = bos.drop('PRICE', axis=1)
		Y = bos['PRICE']
		# split data and save
		self.X_train, self.X_val, self.Y_train, self.Y_val = sklearn.cross_validation.train_test_split(X, Y, test_size = test_size, random_state = 5)

class Digits():

	def digits(self, test_size):
		# load data
		digits = sklearn.datasets.load_digits()
		# transform data
		X = np.array(digits.data)
		X = X.reshape(X.shape[0], -1)
		Y = digits.target
		# split data and save data
		self.X_train, self.X_val, self.Y_train, self.Y_val = sklearn.cross_validation.train_test_split(X, Y, test_size = test_size, random_state = 5)


class GetData4(Boston, Digits):

	def __init__(self):
		self.Brain = []

	def getBrain(self):

		class Brain():
			pass
			
		Book = Brain()
		Book.train = Brain()
		Book.train.x = self.X_train
		Book.train.y = self.Y_train
		Book.val = Brain()
		Book.val.x = self.X_val
		Book.val.y = self.Y_val
		return Book
		

mjr = GetData4()
mjr.boston(.33)
ds1 = mjr.getBrain()

mjr = GetData4()
mjr.digits(.33)
ds2 = mjr.getBrain()