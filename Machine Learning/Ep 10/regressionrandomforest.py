import preprocessing as pre
import numpy as np
import pandas as pd

#temporizador
import time
from functools import wraps

def computeRandomForestRegressionModel(X, y, numberOfTrees):
    from sklearn.ensemble import RandomForestRegressor

    regressor = RandomForestRegressor(n_estimators = numberOfTrees)
    regressor.fit(X, y)

    return regressor

def showPlot(XPoints, yPoints, XLine, yLine):
    import matplotlib.pyplot as plt

    plt.scatter(XPoints, yPoints, color= 'red')
    plt.plot(XLine, yLine, color = 'blue')
    plt.title("Comparando pontos reais com a reta produzida pela regressão de floresta randômica.")
    plt.xlabel("Experiência em anos")
    plt.ylabel("Salário")
    plt.show()

def runRandomForestRegressionExample(filename):
    start_time = time.time()
    X, y, csv = pre.loadDataset(filename)
    elapsed_time = time.time() - start_time
    print("Load Dataset: %.2f" % elapsed_time, "segundos.")

    start_time = time.time()
    computeRandomForestRegressionModel(X, y, 100)
    elapsed_time = time.time() - start_time
    print("Compute Random Forest Regression: %.2f" % elapsed_time, "segundos.")

if __name__ == "__main__":
    runRandomForestRegressionExample("salary.csv")
