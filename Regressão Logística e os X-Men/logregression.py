# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 14:03:44 2018

@author: Lucas
"""

import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

def visualizeClassifier(classifier, X, y):
    #min e max alturas
    minX = X[:, 0].min() - 1.0
    maxX = X[:, 0].max() + 1.0
    #min e max pesos
    minY = X[:, 1].min() - 1.0
    maxY = X[:, 1].max() + 1.0
    
    xVals, yVals = np.meshgrid(np.arange(minX, maxX, 0.01), np.arange(minY, maxY, 0.01))
        
    output = classifier.predict(np.c_[xVals.ravel(), yVals.ravel()])
    output = output.reshape(xVals.shape)
       
    plt.figure(figsize=(10,5))
    plt.pcolormesh(xVals, yVals, output)
    plt.scatter(X[:,0], X[:,1], c=y, s=100, edgecolors='blue', cmap=plt.cm.Paired)
    plt.xlim(xVals.min(), xVals.max())
    plt.ylim(yVals.min(), yVals.max())
    
    plt.xticks((np.arange(int(X[:, 0].min() - 1), int(X[:, 0].max() + 1))))
    plt.yticks((np.arange(int(X[:, 1].min() - 1), int(X[:, 1].max() + 1))))
    plt.show()

def main():
    X = np.array([[17.2, 7.2], [18.4, 6.7], [12.9, 5.0], [15.1, 4.5], [16.5, 7.5], [15.6, 6.5], [16.3, 4.9], [13.9, 8.0], [14.8, 10.0], [16.5, 13.4], [11.1, 6.4], [16.7, 8.9]])
    y = np.array([     0     ,       0    ,      0     ,      0     ,      0     ,      0     ,      0     ,      1     ,       1     ,       1     ,      1     ,      1     ])

    #criar o modelo de regressão logística
    classifier = linear_model.LogisticRegression(solver='newton-cg')
    
    #computando o modelo de RL
    classifier.fit(X, y) 
    
    visualizeClassifier(classifier, X, y)

if __name__ == "__main__":
    main()