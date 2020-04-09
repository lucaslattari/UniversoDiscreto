import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

baseDeDados = pd.read_csv('admission.csv', delimiter=';')

X = baseDeDados.iloc[:,:-1]
y = baseDeDados.iloc[:,-1]

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='median')
imputer = imputer.fit(baseDeDados.iloc[:,1:-1])
baseDeDados.iloc[:,1:-1] = imputer.transform(baseDeDados.iloc[:,1:-1])

from sklearn.model_selection import train_test_split
XTrain, xTest, yTrain, yTest = train_test_split(baseDeDados.iloc[:,1:-1], baseDeDados.iloc[:,-1], test_size = 0.2)

baseDeDados.loc[:,('predict')] = yTrain
print(yTrain)
print(baseDeDados)
