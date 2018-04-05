# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans 

def computeKmeans(totalOfClusters):
    X = np.loadtxt('canal_youtube.txt', delimiter=',')
    
    model = KMeans(init='random', n_clusters=totalOfClusters, n_init = 10)
    model.fit(X)
    
    #x representa pontos de humor
    #y representa pontos de informação científica
    
    xMin, xMax = X[:, 0].min() - 1, X[:, 0].max() + 1
    yMin, yMax = X[:, 1].min() - 1, X[:, 1].max() + 1
    
    xVals, yVals = np.meshgrid(np.arange(xMin, xMax, 0.01), np.arange(yMin, yMax, 0.01))
    
    output = model.predict(np.c_[xVals.ravel(), yVals.ravel()])
    output = output.reshape(xVals.shape)
    
    plt.figure(figsize=(20,10))
    plt.imshow(output, extent=(xVals.min(), xVals.max(), yVals.min(), yVals.max()), cmap=plt.cm.Paired, aspect='auto', origin='lower')
    plt.scatter(X[:,0], X[:,1], marker='o', facecolors='black', edgecolors='red', s = 80)
    
    centroids = model.cluster_centers_
    plt.scatter(centroids[:,0], centroids[:,1], marker = 'x', s = 400, color='blue')
    plt.title("Kmeans - Youtube Channels")
    plt.xlim(xMin, xMax)
    plt.ylim(yMin, yMax)
    plt.xticks(np.arange(xMin, xMax, step=1))
    plt.yticks(np.arange(yMin, yMax, step=1))
    plt.show()
    
if __name__ == "__main__":
    computeKmeans(2)