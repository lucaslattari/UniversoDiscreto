import numpy as np
import pandas as pd

baseDeDados = pd.read_csv('svbr.csv', delimiter=';')
X = baseDeDados.iloc[:,:].values

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='median')
imputer = imputer.fit(X[:,1:3])
X = imputer.transform(X[:,1:3]).astype(str)
X = np.insert(X, 0, baseDeDados.iloc[:,0].values, axis=1)

print(X)
