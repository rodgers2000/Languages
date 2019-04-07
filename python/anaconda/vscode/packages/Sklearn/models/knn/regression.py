from sklearn.neighbors import KNeighborsRegressor
import pandas as pd
import numpy as np
from sklearn import datasets

# pylint: disable=C0321, E1101

iris = datasets.load_iris()

x = pd.DataFrame(iris.data)
y = pd.DataFrame(iris.target)

df = pd.concat([x, y], axis=1)
df.columns = ['0', '1', '2', '3', 'y']

train_error = []
K = []

for k in range(1, 11, 1):
    neigh = KNeighborsRegressor(n_neighbors=k)
    neigh.fit(df.iloc[:, [0, 1, 2]], df.iloc[:, 3])
    yhats = neigh.predict(df.iloc[:, [0, 1, 2]])
    train_error.append(np.power(sum((df.iloc[:, 4] - yhats)), 2) / len(yhats))
    K.append(k)

temp_df = {}
temp_df["k"] = K
temp_df["error"] = train_error

this_df = pd.DataFrame(temp_df)

print(this_df)
