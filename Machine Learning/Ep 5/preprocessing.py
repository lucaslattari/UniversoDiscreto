import numpy as np
import pandas as pd

def loadDataset(filename):
    baseDeDados = pd.read_csv(filename, delimiter=';')
    return baseDeDados

def fillMissingData(X):
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(missing_values=np.nan, strategy='median')
    X = imputer.fit_transform(X)
    return X

def computeCategorization(baseDeDados, compute):
    from sklearn.preprocessing import LabelEncoder
    labelencoder_X = LabelEncoder()
    for (name, data) in compute.iteritems():
        data = labelencoder_X.fit_transform(data)
        D = pd.get_dummies(data).iloc[:,1:]
        baseDeDados = baseDeDados.drop(name,axis=1)
        for (i, data) in D.iteritems():
            baseDeDados.insert(0,name+'_'+str(i),data)

    return baseDeDados

def splitTrainTestSets(X, y, testSize):
    from sklearn.model_selection import train_test_split
    XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size = testSize)
    return XTrain, XTest, yTrain, yTest

def computeScaling(train, test):
    from sklearn.preprocessing import StandardScaler
    scaleX = StandardScaler()
    train = scaleX.fit_transform(train)
    test = scaleX.fit_transform(test)
    return train, test
