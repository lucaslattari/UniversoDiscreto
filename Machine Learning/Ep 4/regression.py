import numpy as np
import pandas as pd

def loadDataSet(filename):
    print("Carregando a base de dados...")
    baseDeDados = pd.read_csv(filename, delimiter=';')
    print("ok!")
    return baseDeDados

def fillMissingData(X):
    print("Preenchendo dados que estão faltando...")
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(missing_values=np.nan, strategy='median')
    X = imputer.fit_transform(X)
    print("ok!")
    return X

def computeCategorization(baseDeDados, compute):
    print("Computando rotulação...")
    from sklearn.preprocessing import LabelEncoder
    labelencoder_X = LabelEncoder()
    for (name, data) in compute.iteritems():
        data = labelencoder_X.fit_transform(data)
        D = pd.get_dummies(data).iloc[:,1:]
        baseDeDados = baseDeDados.drop(name,axis=1)
        for (i, data) in D.iteritems():
            baseDeDados.insert(0,name+'_'+str(i),data)

    print("ok!")
    return baseDeDados

def splitTrainTestSets(X, y, testSize):
    print("Separando conjuntos de teste e treino...")
    from sklearn.model_selection import train_test_split
    XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size = testSize)
    print("ok!")
    return XTrain, XTest, yTrain, yTest

def computeNormalization(XTrain, XTest):
    print("Computando Normalização...")
    from sklearn.preprocessing import StandardScaler
    scaleX = StandardScaler()
    XTrain = scaleX.fit_transform(XTrain)
    XTest = scaleX.fit_transform(XTest)
    print("ok!")
    return XTrain, XTest

def computeLinearRegression(XTrain, yTrain, XTest, yTest):
    import matplotlib.pyplot as plt
    from sklearn.linear_model import LinearRegression

    print("Computando Regressão Linear...")
    regressor = LinearRegression()
    regressor.fit(XTrain, yTrain)
    yPred = regressor.predict(XTest)
    print("ok!")

    print(XTest)

    plt.scatter(XTest, yTest, color = 'red')
    plt.plot(XTest, regressor.predict(XTest), color='blue')
    plt.title("Inscritos x Visualizações")
    plt.xlabel("Inscritos")
    plt.ylabel("Visualizações")
    plt.show()

def runLinearRegressionExample():
    baseDeDados = loadDataSet("svbr.csv")
    baseDeDados.loc[:,('Inscritos',)] = fillMissingData(baseDeDados.loc[:,('Inscritos',)])
    XTrain, XTest, yTrain, yTest = splitTrainTestSets(baseDeDados.loc[:,('Inscritos',)], baseDeDados.loc[:,('Visualizações')], 0.8)
    computeLinearRegression(XTrain, yTrain, XTest, yTest)

if __name__ == "__main__":
    runLinearRegressionExample()
