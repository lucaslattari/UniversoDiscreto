from logisticregression import LogisticRegression
from knn import KNN
from svm import SVM

import numpy as np
import pandas as pd
from tqdm import tqdm

def getAccuracy(confusionMatrix):
    accuracy = (confusionMatrix[0][0] + confusionMatrix[1][1]) / (confusionMatrix[0][0] + confusionMatrix[1][0] + confusionMatrix[0][1] + confusionMatrix[1][1])
    return accuracy * 100

rlArray = []
for i in tqdm(range(0, 20)):
    cmLR = LogisticRegression.computeExample("titanic.csv")
    rlArray.append(getAccuracy(cmLR))
print("Média da Regressão Logística: %.2f" % np.mean(rlArray))
print("Desvio Padrão da Regressão Logística: %.2f" % np.std(rlArray))

knnArray = []
for i in tqdm(range(0, 20)):
    cmKnn = KNN.computeExample("titanic.csv")
    knnArray.append(getAccuracy(cmKnn))
print("\nMédia do KNN: %.2f" % np.mean(knnArray))
print("Desvio Padrão do KNN: %.2f" % np.std(knnArray))

svmLinearArray = []
for i in tqdm(range(0, 20)):
    cmSVML = SVM.computeExample("titanic.csv", "linear", 0)
    svmLinearArray.append(getAccuracy(cmSVML))
print("\nMédia do SVM Linear: %.2f" % np.mean(svmLinearArray))
print("Desvio Padrão do SVM Linear: %.2f" % np.std(svmLinearArray))

svmPoly3Array = []
for i in tqdm(range(0, 20)):
    cmSVMP3 = SVM.computeExample("titanic.csv", "poly", 3)
    svmPoly3Array.append(getAccuracy(cmSVMP3))
print("\nMédia do SVM Poly 3: %.2f" % np.mean(svmPoly3Array))
print("Desvio Padrão do SVM Poly 3: %.2f" % np.std(svmPoly3Array))

svmPoly4Array = []
for i in tqdm(range(0, 20)):
    cmSVMP4 = SVM.computeExample("titanic.csv", "poly", 4)
    svmPoly4Array.append(getAccuracy(cmSVMP4))
print("\nMédia do SVM Poly 4: %.2f" % np.mean(svmPoly4Array))
print("Desvio Padrão do SVM Poly 4: %.2f" % np.std(svmPoly4Array))

svmGaussArray = []
for i in tqdm(range(0, 20)):
    cmSVMG = SVM.computeExample("titanic.csv", "rbf", 0)
    svmGaussArray.append(getAccuracy(cmSVMG))
print("\nMédia do SVM Gaussiano: %.2f" % np.mean(svmGaussArray))
print("Desvio Padrão do SVM Gaussiano: %.2f" % np.std(svmGaussArray))

import matplotlib.pyplot as plt
plt.plot(rlArray, 'r-', knnArray, 'g--', svmGaussArray, 'b^')
plt.ylabel("Acurácia")
plt.xlabel("Tentativas")
plt.show()
