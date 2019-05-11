import numpy as np
import pandas as pd

basededados = pd.read_csv('svbr.csv', delimiter=';')
X = basededados.iloc[:,:].values

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(X[:,1:3])
X = imputer.transform(X[:,1:3]).astype(str)
X = np.insert(X, 0, basededados.iloc[:,0].values, axis=1)
print(X)
