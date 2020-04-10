import preprocessing as pre
import numpy as np
import pandas as pd

#temporizador
import time
from functools import wraps

def computeLinearRegressionModel(XTrain, yTrain, XTest, yTest):
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(XTrain, yTrain)

    #gerar grafico
    import matplotlib.pyplot as plt
    plt.scatter(XTest, yTest, color="red")
    plt.plot(XTest, regressor.predict(XTest), color="blue")
    plt.title("Inscritos x Visualizações (SVBR)")
    plt.xlabel("Total de Inscritos")
    plt.ylabel("Total de Visualizações")
    plt.show()

def runLinearRegressionExample(filename):
    start_time = time.time()
    baseDeDados = pre.loadDataset(filename)
    elapsed_time = time.time() - start_time
    print("Load Dataset: %.2f segundos." % elapsed_time)

    start_time = time.time()
    baseDeDados.loc[:,('Inscritos',)] = pre.fillMissingData(baseDeDados.loc[:,('Inscritos',)])
    elapsed_time = time.time() - start_time
    print("Fill Missing Data: %.2f segundos." % elapsed_time)

    start_time = time.time()
    XTrain, XTest, yTrain, yTest = pre.splitTrainTestSets(baseDeDados.loc[:,('Inscritos',)], baseDeDados.loc[:,('Visualizações')], 0.8)
    elapsed_time = time.time() - start_time
    print("Split Train Test sets: %.2f segundos." % elapsed_time)

    start_time = time.time()
    computeLinearRegressionModel(XTrain, yTrain, XTest, yTest)
    elapsed_time = time.time() - start_time
    print("Compute Linear Regression: %.2f segundos." % elapsed_time)

if __name__ == "__main__":
    runLinearRegressionExample("svbr.csv")
