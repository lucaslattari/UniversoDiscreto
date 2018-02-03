# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:04:52 2018

@author: Lucas
"""

import pandas
import matplotlib.pyplot as plt
import numpy as np
import perceptronlib as plib

URL_IRIS_DATASET = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

def loadData(url):
    #colunas dos dados lidos
    names = ['sepal-length', 'sepala-width', 'petal-length', 'petal-width', 'classes']
    
    return pandas.read_csv(url, names = names)

def showScatterplot(X):
    
    fig = plt.figure(figsize=(10, 7)) #tamanho da img em largura e altura
    plt.rc("font", size = 22) #tamanho da fonte
    
    plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
    plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')

    plt.ylabel("sepal length")
    plt.xlabel("petal length")
    plt.legend(loc='upper left')
    
    plt.show()

def main():
    dataset = loadData(URL_IRIS_DATASET)
    
    #dimensões do dataset
    print(dataset.shape)
    
    #imprime os 20 primeiros elementos
    print(dataset.head(20))
    
    #informações estatísticas do conjunto    
    print(dataset.describe())
    
    y = dataset.iloc[0:100, 4].values
    y = np.where(y == 'Iris-setosa', -1, 1)
    X = dataset.iloc[0:100, [0, 2]].values
    
    showScatterplot(X)
    #p = plib.Perceptron(0.1, 25)
    #p.fit(X, y)
    #plt.plot(range(1, len(p.errors) + 1), p.errors, marker='o')
    #plt.xlabel("Iteracoes")
    #plt.ylabel("Numero de errors")
    #plt.show()
    
    #print(p.W)

if __name__ == "__main__":
    main()
