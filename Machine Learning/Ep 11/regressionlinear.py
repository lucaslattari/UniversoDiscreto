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
    X, y, csv = pre.loadDataset(filename)
    elapsed_time = time.time() - start_time
    #print("Load Dataset: %.2f" % elapsed_time, "segundos.")

    start_time = time.time()
    regressor = computeLinearRegressionModel(X, y)
    elapsed_time = time.time() - start_time
    print("Compute Linear Regression: %.2f" % elapsed_time, "segundos.")

    from sklearn.metrics import r2_score
    return r2_score(y, regressor.predict(X))

if __name__ == "__main__":
    print(runLinearRegressionExample("salary.csv"))
