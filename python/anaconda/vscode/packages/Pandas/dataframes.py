import pandas as pd
import numpy as np


""" MAKE A DATAFRAME """

# get the number of obs
m = 10
# get the data 
a = [i for i in range(m)]
b = [i**2 for i in range(m)]
c = [i / 2 for i in range(m)]
d = np.random.choice(['m', 'r'], m).tolist()
e = np.random.choice(['j', 'h'], m).tolist()

# combine for iteration
temp = [a, b, c, d, e]
# we go from dictionary to dataframe
df = {}
for i in range(len(temp)):
    df[str(i)] = temp[i]

# make dataframe from the dictionary 
my_df = pd.DataFrame(df)

""" DF ATTRIBUTES """

print(my_df.columns) # get column names
print(my_df.index) # get row names

""" DF STATS """

# dataframe operations
# this is how you sum over the first axis (rows)
print(my_df.agg(['mean', 'median', 'sum'], axis=0))
print(my_df.describe)
type(my_df.ix[0, 0])


""" MAKE A NEW COLUMN """

# this is how you add a column
my_df['5'] = 69

""" ITERATION """

# this is how you loop through a dataframe
n = my_df.shape[0]
p = my_df.shape[1]
evidence = []
for i in range(n):
    for j in range(p):
        evidence.append(my_df.iat[i, j])

# this is how you loop a single column
row1 = []
for i in my_df.index:  # this is a label index, both just be labels
    row1.append(my_df.loc[i, '0'])

# this is how you loop a single row
col1 = []
for i in range(p):
    col1.append(my_df.iloc[0, i]) # both must be numbers

col1 = []
for i in range(p):
    col1.append(my_df.ix[0, i]) # both have to be homo, so all numbers or all labels

""" GROUP BY """

# this is how you groupby 
hold_me = my_df.groupby(['3', '4']).agg([np.median, np.mean, np.sum]) 
# this is how you export the dataframe

""" SAVE DF TO CSV """

hold_me.to_csv('/Users/mrodgers/Documents/other/languages/python/vscode/packages/pandas/data/groupby2.csv')

""" SUBSETTING """

print(my_df)

# keep all m's and h's (LOGICAL SUBSETTING)
this_df = my_df[(my_df['3'] == 'm') & (my_df['4'] == 'h')]

# select a column 
my_df['0']
# drop a column
my_df.drop(['2', '3'], axis=1)
# drop a row
my_df.drop([0, 1], axis=0)

""" SORTING """

my_df.sort_values('2', axis=0, ascending=False)

""" DF APPEND DF by ROW """

df1 = pd.DataFrame()
vec1 = [1, 2, 3, 4]  # default is a column vector 
vec1 = pd.DataFrame(vec1).transpose() # but we want a row vector
df1 = pd.concat([df1, vec1]) #must concatenate two dataframes
print(df1)
