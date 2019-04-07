import pandas as pd

# get the time period
years = list(range(1950, 2019, 1))
# create book and features
book = {}
features = []
# put the data into the book
for year in years:
    book[str(year)] = ['a', 'b', 'c']
# print our progress and grad features

df = pd.DataFrame()

df['ticker'] = ['AAPL'] * len(years)
df['year'] = 0
df['feat1'] = 0
df['feat2'] = 0
df['feat3'] = 0

index = 0
for key, value in book.items():
    df.loc[index, 'year'] = key
    df.iloc[index, 2:] = value
    index += 1

df.to_csv('/Users/mrodgers/Documents/other/languages/python/anaconda/vscode/templates/book/data/wedidit.csv')