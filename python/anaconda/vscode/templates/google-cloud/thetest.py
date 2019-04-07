import pandas as pd

df = pd.DataFrame()

a = [range(10)]
a = pd.DataFrame(a)

df.append(a)

df.to_csv('omg.csv')