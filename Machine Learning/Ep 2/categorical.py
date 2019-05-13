import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

baseDeDados = pd.read_csv('svbr.csv', delimiter=';')
X = baseDeDados.iloc[:,:].values

imputer = SimpleImputer(missing_values=np.nan, strategy='median')
imputer = imputer.fit(X[:,1:3])
X = imputer.transform(X[:,1:3]).astype(str)
X = np.insert(X, 0, baseDeDados.iloc[:,0].values, axis=1)

from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
X = X[:,1:]

D = pd.get_dummies(X[:,0])
X = np.insert(X, 0, D.values, axis=1)
print(X)
