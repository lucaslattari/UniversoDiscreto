import preprocessing as pre
import numpy as np
import pandas as pd

#temporizador
import time
from functools import wraps

def computeMultipleLinearRegressionModel(XTrain, yTrain, XTest, yTest):
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(XTrain, yTrain)

    yPred = regressor.predict(XTest)

    for i in range(0, yPred.shape[0]):
        print(i,yPred[i],yTest.values[i],abs(yPred[i] - yTest.values[i]))

def runMultipleLinearRegressionExample(filename):
    start_time = time.time()
    baseDeDados = pre.loadDataset(filename)
    elapsed_time = time.time() - start_time
    print("Load Dataset: %.2f segundos." % elapsed_time)

    start_time = time.time()
    baseDeDados.loc[:,('age',)] = pre.fillMissingData(baseDeDados.loc[:,('age',)])
    elapsed_time = time.time() - start_time
    print("Fill Missing Data: %.2f segundos." % elapsed_time)

    start_time = time.time()
    baseDeDados = pre.computeCategorization(baseDeDados, baseDeDados.loc[:,('region',)])
    elapsed_time = time.time() - start_time
    print("Compute Categorization: %.2f segundos." % elapsed_time)

    start_time = time.time()
    XTrain, XTest, yTrain, yTest = pre.splitTrainTestSets(baseDeDados.iloc[:,:-1], baseDeDados.iloc[:,-1], 0.8)
    elapsed_time = time.time() - start_time
    print("Split Train Test sets: %.2f segundos." % elapsed_time)

    start_time = time.time()
    computeMultipleLinearRegressionModel(XTrain, yTrain, XTest, yTest)
    elapsed_time = time.time() - start_time
    print("Compute Multiple Linear Regression: %.2f segundos." % elapsed_time)

if __name__ == "__main__":
    runMultipleLinearRegressionExample("insurance.csv")
