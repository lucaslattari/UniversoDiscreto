import numpy as np
import pandas as pd

def loadDataSet(filename):
    print("Carregando a base de dados...")
    baseDeDados = pd.read_csv(filename, delimiter=';')
    X = baseDeDados.iloc[:,:-1].values
    y = baseDeDados.iloc[:,-1].values
    print("ok!")
    return X, y

def fillMissingData(X):
    print("Preenchendo dados que estão faltando...")
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(missing_values=np.nan, strategy='median')
    X[:,1:] = imputer.fit_transform(X[:,1:])
    print("ok!")
    return X

def computeCategorization(X):
    print("Computando rotulação...")
    from sklearn.preprocessing import LabelEncoder
    labelencoder_X = LabelEncoder()
    X[:, 0] = labelencoder_X.fit_transform(X[:, 0])

    D = pd.get_dummies(X[:,0])
    X = X[:,1:]
    X = np.insert(X, 0, D.values, axis=1)
    print("ok!")
    return X

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

    print(XTest[:,-1])

    plt.scatter(XTest[:,-1], yTest, color = 'red')
    plt.plot(XTest[:,-1], regressor.predict(XTest), color='blue')
    plt.title("Inscritos x Visualizações")
    plt.xlabel("Inscritos")
    plt.ylabel("Visualizações")
    plt.show()

def runLinearRegressionExample():
    X, y = loadDataSet("svbr.csv")
    X = fillMissingData(X)
    X = computeCategorization(X)
    XTrain, XTest, yTrain, yTest = splitTrainTestSets(X, y, 0.8)
    computeLinearRegression(XTrain, yTrain, XTest, yTest)

if __name__ == "__main__":
    runLinearRegressionExample()
