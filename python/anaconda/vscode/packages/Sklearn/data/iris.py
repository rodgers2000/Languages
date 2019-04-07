import pandas as pd
import numpy as np
from sklearn import datasets

# pylint: disable=E1101

iris = datasets.load_iris()

x = pd.DataFrame(iris.data)
y = pd.DataFrame(iris.target)

df = pd.concat([x, y], axis=1)
df.columns = ['0', '1', '2', '3', 'y']
