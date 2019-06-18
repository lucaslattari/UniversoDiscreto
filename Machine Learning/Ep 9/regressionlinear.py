import preprocessing as pre
import numpy as np
import pandas as pd

#temporizador
import time
from functools import wraps

def computeLinearRegressionModel(X, y):
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X, y)

    return regressor

def showPlot(X, y, linearRegressor):
    import matplotlib.pyplot as plt

    plt.scatter(X, y, color= 'red')
    plt.plot(X, linearRegressor.predict(X), color = 'blue')
    plt.title("Comparando pontos reais com a reta produzida pela regressão linear.")
    plt.xlabel("Experiência em anos")
    plt.ylabel("Salário")
    plt.show()
        
def runLinearRegressionExample(filename):
    start_time = time.time()
    X, y = pre.loadDataset(filename)
    elapsed_time = time.time() - start_time
    print("Load Dataset: %.2f" % elapsed_time, "segundos.")

    start_time = time.time()
    X = pre.fillMissingData(X, 1, X.shape[1])
    elapsed_time = time.time() - start_time
    print("Fill Missing Data: %.2f" % elapsed_time, "segundos.")

    start_time = time.time()
    X = pre.computeCategorization(X, 0)
    elapsed_time = time.time() - start_time
    print("Compute Categorization: %.2f" % elapsed_time, "segundos.")

    start_time = time.time()
    XTrain, XTest, yTrain, yTest = pre.splitTrainTestSets(X, y, 0.8)
    elapsed_time = time.time() - start_time
    print("Split Train Test sets: %.2f" % elapsed_time, "segundos.")

    start_time = time.time()
    computeLinearRegressionModel(XTrain, yTrain)
    elapsed_time = time.time() - start_time
    print("Compute Linear Regression: %.2f" % elapsed_time, "segundos.")

if __name__ == "__main__":
    runLinearRegressionExample("svbr.csv")
