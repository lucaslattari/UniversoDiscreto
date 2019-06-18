import preprocessing as pre
import numpy as np
import pandas as pd

#temporizador
import time
from functools import wraps

def computeSupportVectorRegressionModel(X, y, k, d):
    from sklearn.svm import SVR
    if(k == "poly"):
        regressor = SVR(kernel = k, degree = d)
    else:
        regressor = SVR(kernel = k)
    regressor.fit(X, np.ravel(y))

    return regressor

def showPlot(XPoints, yPoints, XLine, yLine):
    import matplotlib.pyplot as plt

    plt.scatter(XPoints, yPoints, color= 'red')
    plt.plot(XLine, yLine, color = 'blue')
    plt.title("Comparando pontos reais com a reta produzida pela regressão de vetor suporte.")
    plt.xlabel("Experiência em anos")
    plt.ylabel("Salário")
    plt.show()

def runSupportVectorRegressionExample(filename):
    start_time = time.time()
    X, y, csv = pre.loadDataset(filename)
    elapsed_time = time.time() - start_time
    print("Load Dataset: %.2f" % elapsed_time, "segundos.")

    start_time = time.time()
    computeSupportVectorRegressionModel(X, y)
    elapsed_time = time.time() - start_time
    print("Compute Support Vector Regression: %.2f" % elapsed_time, "segundos.")

if __name__ == "__main__":
    runSupportVectorRegressionExample("salary.csv")
