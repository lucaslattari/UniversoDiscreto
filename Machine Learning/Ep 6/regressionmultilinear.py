import preprocessing as pre
import numpy as np
import pandas as pd
import time
from functools import wraps

def computeAutomaticBackwardElimination(XTrain, yTrain, XTest, sl):
    import statsmodels.formula.api as sm
    XTrain = np.insert(XTrain, 0, 1, axis=1)
    XTest = np.insert(XTest, 0, 1, axis=1)

    numVars = len(XTrain[0])
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(yTrain, XTrain.astype(float)).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        if maxVar > sl:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    #print("Deletar coluna", j)
                    XTrain = np.delete(XTrain, j, 1)
                    XTest = np.delete(XTest, j, 1)

    #regressor_OLS.summary()
    return XTrain, XTest

def computeBackwardElimination(X, y):
    #precisa do pip pra statsmodels e patsy
    import statsmodels.formula.api as sm

    #adicionamos 1 coluna pra incluir b0 no modelo
    X = np.insert(X, 0, 1, axis=1)

    #ajustamos o modelo para todos os possiveis preditores (variaveis independentes)
    XOtimo = X[:,[0, 1, 2, 3, 4, 5, 6]]
    regressor = sm.OLS(y, XOtimo.astype(float)).fit()
    #examinamos o maior p-valor e se ele ultrapassar o limiar de 0.05, removemos
    #print(regressor.summary())
    #print(XOtimo[0,:])

    #ajustamos o modelo removendo x5, pois esta recebeu maior p-valor
    XOtimo = X[:,[0, 1, 2, 3, 4, 6]]
    regressor = sm.OLS(y, XOtimo.astype(float)).fit()
    #examinamos o maior p-valor e se ele ultrapassar o limiar de 0.05, removemos
    #print(regressor.summary())
    #print(XOtimo[0,:])

    #ajustamos o modelo removendo x5, pois esta recebeu maior p-valor
    XOtimo = X[:,[0, 1, 2, 3, 4]]
    regressor = sm.OLS(y, XOtimo.astype(float)).fit()
    #examinamos o maior p-valor e se ele ultrapassar o limiar de 0.05, removemos
    #print(regressor.summary())
    #print(XOtimo[0,:])

    #ajustamos o modelo removendo x4, pois esta recebeu maior p-valor
    XOtimo = X[:,[0, 1, 2, 3]]
    regressor = sm.OLS(y, XOtimo.astype(float)).fit()
    #examinamos o maior p-valor e se ele ultrapassar o limiar de 0.05, removemos
    #print(regressor.summary())
    #print(XOtimo[0,:])

    #ajustamos o modelo removendo x3, pois esta recebeu maior p-valor
    XOtimo = X[:,[0, 1, 2]]
    regressor = sm.OLS(y, XOtimo.astype(float)).fit()
    #examinamos o maior p-valor e se ele ultrapassar o limiar de 0.05, removemos
    #print(regressor.summary())
    #print(XOtimo[0,:])

    #ajustamos o modelo removendo x3, pois esta recebeu maior p-valor
    XOtimo = X[:,[1, 2]]
    regressor = sm.OLS(y, XOtimo.astype(float)).fit()
    #examinamos o maior p-valor e se ele ultrapassar o limiar de 0.05, removemos
    print(regressor.summary())
    print(XOtimo[0,:])

#https://medium.com/@manjabogicevic/multiple-linear-regression-using-python-b99754591ac0
def computeMultipleLinearRegressionModel(XTrain, yTrain, XTest, yTest):
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(XTrain, yTrain)

    yPred = regressor.predict(XTest)
    '''for i in range(0, yPred.shape[0]):
        print(yPred[i], yTest[i], abs(yPred[i] - yTest[i]))
        time.sleep(0.5)'''

def runMultipleLinearRegressionExample(filename):
    start_time = time.time()
    X, y = pre.loadDataset(filename)
    elapsed_time = time.time() - start_time
    print("Load Dataset: %.2f" % elapsed_time, "segundos.")

    start_time = time.time()
    X = pre.fillMissingData(X, 0, 2)
    elapsed_time = time.time() - start_time
    print("Fill Missing Data: %.2f" % elapsed_time, "segundos.")

    start_time = time.time()
    X = pre.computeCategorization(X, 3)
    elapsed_time = time.time() - start_time
    print("Compute Categorization: %.2f" % elapsed_time, "segundos.")

    start_time = time.time()
    XTrain, XTest, yTrain, yTest = pre.splitTrainTestSets(X, y, 0.8)
    elapsed_time = time.time() - start_time
    print("Split Train Test sets: %.2f" % elapsed_time, "segundos.")

    start_time = time.time()
    XTrain, XTest = computeAutomaticBackwardElimination(XTrain, yTrain, XTest, 0.05)
    elapsed_time = time.time() - start_time
    print("Compute Automatic Backward Elimination: %.2f" % elapsed_time, "segundos.")

    start_time = time.time()
    computeMultipleLinearRegressionModel(XTrain, yTrain, XTest, yTest)
    elapsed_time = time.time() - start_time
    print("Compute Multiple Linear Regression: %.2f" % elapsed_time, "segundos.")

    '''start_time = time.time()
    computeBackwardElimination(XTrain, yTrain)
    elapsed_time = time.time() - start_time
    print("Compute Backward Elimination: %.2f" % elapsed_time, "segundos.")
'''

if __name__ == "__main__":
    runMultipleLinearRegressionExample("insurance.csv")
