# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 13:38:30 2018

@author: Lucas
"""

import numpy as np

class Perceptron(object):
    
    def __init__(self, learningRate, maxIterations):
        self.learningRate = learningRate
        self.maxIterations = maxIterations
        
    def fit(self, X, y):
        self.W = np.zeros(1 + X.shape[1])
        self.errors = []
        
        for _ in range(self.maxIterations):
            errors = 0
            for xi, yTarget in zip(X, y):
                deltaW = self.learningRate * (yTarget - self.predict(xi))
                self.W[1:] += deltaW * xi
                self.W[0] += deltaW #bias
                errors += int(deltaW != 0.0)
            self.errors.append(errors)
        
    def computePhiZ(self, X):
        return np.dot(X, self.W[1:]) + self.W[0]
        
    def predict(self, X):
        return np.where(self.computePhiZ(X) >= 0.0, 1, -1)
        
        