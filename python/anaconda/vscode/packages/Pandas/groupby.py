import pandas as pd
import sklearn
import numpy as np
import statistics

iris = pd.read_csv(
    '/Users/mrodgers/Documents/other/languages/python/anaconda/vscode/packages/pandas/data/iris.csv')

Z = np.random.choice([3, 4, 5], iris.count()[1], replace=True)

iris['z'] = Z.astype(str)

aggregations = {}
aggregations['sepal_length'] = [min, max, statistics.mean]
aggregations['sepal_width'] = [min, max, sum]

stats = iris.groupby(['species', 'z']).agg(aggregations)

stats.to_csv(
    '/Users/mrodgers/Documents/other/languages/python/anaconda/vscode/packages/pandas/data/groupby.csv')
