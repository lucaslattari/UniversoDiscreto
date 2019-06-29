import preprocessing as pre
import numpy as np
import pandas as pd

#temporizador
import time
from functools import wraps

def computeDecisionTreeRegressionModel(X, y):
    from sklearn.tree import DecisionTreeRegressor

    regressor = DecisionTreeRegressor()
    regressor.fit(X, y)

    return regressor

def showPlot(XPoints, yPoints, XLine, yLine):
    import matplotlib.pyplot as plt

    plt.scatter(XPoints, yPoints, color= 'red')
    plt.plot(XLine, yLine, color = 'blue')
    plt.title("Comparando pontos reais com a reta produzida pela regressão de árvore de decisão.")
    plt.xlabel("Experiência em anos")
    plt.ylabel("Salário")
    plt.show()

def runDecisionTreeRegressionExample(filename):
    start_time = time.time()
    X, y, csv = pre.loadDataset(filename)
    elapsed_time = time.time() - start_time
    #print("Load Dataset: %.2f" % elapsed_time, "segundos.")

    start_time = time.time()
    regressor = computeDecisionTreeRegressionModel(X, y)
    elapsed_time = time.time() - start_time
    print("Compute Decision Tree Regression: %.2f" % elapsed_time, "segundos.")

    from sklearn.metrics import r2_score
    return r2_score(y, regressor.predict(X))

if __name__ == "__main__":
    print(runDecisionTreeRegressionExample("salary.csv"))
