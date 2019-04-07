import numpy as np
import seaborn
import pandas as pd

x = np.arange(10)
y = x**2
labels = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
labels = [str(i) for i in labels]

df = {}
df['x'] = x
df['y'] = y
df['labels'] = labels

this_plot = seaborn.scatterplot(x='x',  y='y', hue='labels', data=df)
fig = this_plot.get_figure()
fig.savefig(
    '/Users/mrodgers/Documents/other/languages/python/anaconda/vscode/packages/seaborn/figures/test.pdf')
