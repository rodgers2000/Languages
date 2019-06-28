from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

import pandas as pd
import numpy as np

mjr = pd.DataFrame()

mjr['a'] = np.arange(5)
mjr['b'] = np.random.choice(['cat', 'dog'], size=5)
mjr['c'] = np.random.choice(['one', 'two', 'three'], size=5)

le = LabelEncoder()

categorical_feature_masks = mjr.dtypes == object
categorical_cols = mjr.columns[categorical_feature_masks].tolist()

mjr[categorical_cols] = mjr[categorical_cols].apply(lambda col: le.fit_transform(col))

ohe = OneHotEncoder(categorical_features=categorical_feature_masks, sparse=False)

X_ohe = ohe.fit_transform(mjr)

print(X_ohe)
print(mjr)



