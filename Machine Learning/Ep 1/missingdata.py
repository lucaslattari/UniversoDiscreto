import numpy as np
import pandas as pd

baseDeDados = pd.read_csv('svbr.csv', delimiter=';')

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='median')
imputer = imputer.fit(baseDeDados.loc[:,('Inscritos','Visualizações')])
baseDeDados.loc[:,('Inscritos','Visualizações')] = imputer.transform(baseDeDados.loc[:,('Inscritos','Visualizações')]).astype(str)

print(baseDeDados)
