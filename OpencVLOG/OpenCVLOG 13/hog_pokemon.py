# -*- coding: utf-8 -*-
"""
Detector de Objetos usando HOG + SVM

Este é um arquivo de script temporário.
"""
import re
import cv2
from skimage import feature
from sklearn.svm import SVC
import numpy as np
import pickle
from tqdm import tqdm
from os import listdir
from os.path import isfile, join

#rootFolder + trainFolder + objFolder
#rootFolder + trainFolder + bkgFolder
#rootFolder + cropTrainFolder + objFolder
#rootFolder + cropTrainFolder + bkgFolder
#rootFolder + testFolder + objFolder
#rootFolder + testFolder + bkgFolder
#rootFolder + testTrainFolder + objFolder
#rootFolder + testTrainFolder + bkgFolder

rootFolder = "pokemon\\dataset\\"
trainFolder = "images\\"
testFolder = "test-images\\"
obj1Folder = "bulbasaur\\"
obj2Folder = "charmander\\"
obj3Folder = "pikachu\\"
obj4Folder = "squirtle\\"

cropTrainFolder = "trainLucas\\"
cropTestFolder = "testLucas\\"

svmFilename = "pokemon.svm"

widthWindow = 400
heightWindow = 400

orientationsParam = 9
pixelsPerCellParam = 4
cellsPerBlockParam = 2

def extractFilenamesFromFolder(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    return onlyfiles

def cropRegionOfEachPosImage(path, trainFolder, cropFolder, listOfImages, isTrain):
    i = 0
    if(isTrain == 1):
        print("Montando base de imagens de bulbassauro para treino.")
    elif(isTrain == 2):
        print("Montando base de imagens de charmander para teste.")
    elif(isTrain == 3):
        print("Montando base de imagens de pikachu para teste.")
    elif(isTrain == 4):
        print("Montando base de imagens de squirtle para teste.")

    for eachImage in tqdm(listOfImages):
        if(isTrain == 1):
            img = cv2.imread(path + trainFolder + obj1Folder + eachImage)
        elif(isTrain == 2):
            img = cv2.imread(path + trainFolder + obj2Folder + eachImage)
        elif(isTrain == 3):
            img = cv2.imread(path + trainFolder + obj3Folder + eachImage)
        else:
            img = cv2.imread(path + trainFolder + obj4Folder + eachImage)

        img = cv2.resize(img, (widthWindow, heightWindow))
        flipImg = cv2.flip(img, 1)
        
        stringImg = listOfImages[i].split("/", 1)
        
        if(isTrain == 1):
            cv2.imwrite(path + cropFolder + obj1Folder + stringImg[0], img)
            cv2.imwrite(path + cropFolder + obj1Folder + "flip_" + str(i) + ".png", flipImg)
        elif(isTrain == 2):
            cv2.imwrite(path + cropFolder + obj2Folder + stringImg[0], img)
            cv2.imwrite(path + cropFolder + obj2Folder + "flip_" + str(i) + ".png", flipImg)
        elif(isTrain == 3):
            cv2.imwrite(path + cropFolder + obj3Folder + stringImg[0], img)
            cv2.imwrite(path + cropFolder + obj3Folder + "flip_" + str(i) + ".png", flipImg)
        elif(isTrain == 4):
            cv2.imwrite(path + cropFolder + obj4Folder + stringImg[0], img)
            cv2.imwrite(path + cropFolder + obj4Folder + "flip_" + str(i) + ".png", flipImg)

        i += 1

def setDatabase():
    #train bulbasaur
    vectorOfFilenameImagesPos = extractFilenamesFromFolder(rootFolder + trainFolder + obj1Folder)
    cropRegionOfEachPosImage(rootFolder, trainFolder, cropTrainFolder, vectorOfFilenameImagesPos, 1)

    #train charmander
    vectorOfFilenameImagesPos = extractFilenamesFromFolder(rootFolder + trainFolder + obj2Folder)
    cropRegionOfEachPosImage(rootFolder, trainFolder, cropTrainFolder, vectorOfFilenameImagesPos, 2)

    #train pikachu
    vectorOfFilenameImagesPos = extractFilenamesFromFolder(rootFolder + trainFolder + obj3Folder)
    cropRegionOfEachPosImage(rootFolder, trainFolder, cropTrainFolder, vectorOfFilenameImagesPos, 3)

    #train squirtle
    vectorOfFilenameImagesPos = extractFilenamesFromFolder(rootFolder + trainFolder + obj4Folder)
    cropRegionOfEachPosImage(rootFolder, trainFolder, cropTrainFolder, vectorOfFilenameImagesPos, 4)


def trainSVM():
    X = np.empty(0)
    Y = np.empty(0)
    dimensionOfFeatureVector = 0
    
    print("Extraindo feature HOG de Bulbassauro.")
    vectorOfFilenameImagesPos = extractFilenamesFromFolder(rootFolder + cropTrainFolder + obj1Folder)
    for eachImage in tqdm(vectorOfFilenameImagesPos):
        eachImage = eachImage.split("/", -1)
        eachImage = rootFolder + cropTrainFolder + obj1Folder + eachImage[0]
        
        img = cv2.imread(eachImage, 0)
        img = cv2.resize(img, (widthWindow, heightWindow))
        H = feature.hog(img, orientations=orientationsParam, pixels_per_cell=(pixelsPerCellParam, pixelsPerCellParam), cells_per_block=(cellsPerBlockParam, cellsPerBlockParam), block_norm='L2-Hys', feature_vector = True)
        H = np.array(H)
        
        if(X.shape[0] == 0):
            X = H
            dimensionOfFeatureVector = X.shape[0]
        else:
            X = np.append(X, H)
            
        if(Y.shape[0] == 0):
            Y = np.array([0])
        else:
            Y = np.append(Y, np.array([0]))
             
    print("Extraindo feature HOG de Charmander.")
    vectorOfFilenameImagesPos = extractFilenamesFromFolder(rootFolder + cropTrainFolder + obj2Folder)
    for eachImage in tqdm(vectorOfFilenameImagesPos):
        eachImage = eachImage.split("/", -1)
        eachImage = rootFolder + cropTrainFolder + obj2Folder + eachImage[0]
        
        img = cv2.imread(eachImage, 0)
        img = cv2.resize(img, (widthWindow, heightWindow))
        H = feature.hog(img, orientations=orientationsParam, pixels_per_cell=(pixelsPerCellParam, pixelsPerCellParam), cells_per_block=(cellsPerBlockParam, cellsPerBlockParam), block_norm='L2-Hys', feature_vector = True)
        H = np.array(H)
        
        X = np.append(X, H)            
        Y = np.append(Y, np.array([1]))
             
    print("Extraindo feature HOG de Pikachu.")
    vectorOfFilenameImagesPos = extractFilenamesFromFolder(rootFolder + cropTrainFolder + obj3Folder)
    for eachImage in tqdm(vectorOfFilenameImagesPos):
        eachImage = eachImage.split("/", -1)
        eachImage = rootFolder + cropTrainFolder + obj3Folder + eachImage[0]
        
        img = cv2.imread(eachImage, 0)
        img = cv2.resize(img, (widthWindow, heightWindow))
        H = feature.hog(img, orientations=orientationsParam, pixels_per_cell=(pixelsPerCellParam, pixelsPerCellParam), cells_per_block=(cellsPerBlockParam, cellsPerBlockParam), block_norm='L2-Hys', feature_vector = True)
        H = np.array(H)
        
        X = np.append(X, H)            
        Y = np.append(Y, np.array([2]))
        
    print("Extraindo feature HOG de Squirtle.")
    vectorOfFilenameImagesPos = extractFilenamesFromFolder(rootFolder + cropTrainFolder + obj4Folder)
    for eachImage in tqdm(vectorOfFilenameImagesPos):
        eachImage = eachImage.split("/", -1)
        eachImage = rootFolder + cropTrainFolder + obj4Folder + eachImage[0]
        
        img = cv2.imread(eachImage, 0)
        img = cv2.resize(img, (widthWindow, heightWindow))
        H = feature.hog(img, orientations=orientationsParam, pixels_per_cell=(pixelsPerCellParam, pixelsPerCellParam), cells_per_block=(cellsPerBlockParam, cellsPerBlockParam), block_norm='L2-Hys', feature_vector = True)
        H = np.array(H)
        
        X = np.append(X, H)            
        Y = np.append(Y, np.array([3]))

    print("Treinando o SVM.\n")
    X = np.reshape(X, (-1, dimensionOfFeatureVector))

    svm = SVC(kernel='linear')
    svm.fit(X, Y)
    return svm

def testImages(svmObj):
    font = cv2.FONT_HERSHEY_SIMPLEX
    vectorOfFilenameImagesPos = extractFilenamesFromFolder(rootFolder + testFolder)
    print("Classificando imagens.")
    for eachImage in tqdm(vectorOfFilenameImagesPos):
        eachImage = eachImage.split("/", -1)
        eachImage = rootFolder + testFolder + eachImage[0]
        
        img = cv2.imread(eachImage, 0)
        imgShow = cv2.imread(eachImage, 1)
        h, w, _ = imgShow.shape
        img = cv2.resize(img, (widthWindow, heightWindow))

        H = feature.hog(img, orientations=orientationsParam, pixels_per_cell=(pixelsPerCellParam, pixelsPerCellParam), cells_per_block=(cellsPerBlockParam, cellsPerBlockParam), block_norm='L2-Hys', feature_vector = True)
        X = np.array(H)
        X = np.reshape(X, (-1, X.shape[0]))
        
        if(svmObj.predict(X) == 0):
            cv2.putText(imgShow, 'Bulbassauro', (0, int(h * 0.15)), font, 1, (0, 255, 0), 3, cv2.LINE_AA)
        elif(svmObj.predict(X) == 1):
            cv2.putText(imgShow, 'Charmander', (0, int(h * 0.15)), font, 1, (0, 0, 255), 3, cv2.LINE_AA)
        elif(svmObj.predict(X) == 2):
            cv2.putText(imgShow, 'Pikachu', (0, int(h * 0.15)), font, 1, (0, 255, 255), 3, cv2.LINE_AA)
        elif(svmObj.predict(X) == 3):
            cv2.putText(imgShow, 'Squirtle', (0, int(h * 0.15)), font, 1, (255, 0, 0), 3, cv2.LINE_AA)
            
        cv2.imshow("Resultado", imgShow)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
def saveSVM(obj):
    pickle.dump(obj, open(svmFilename, "wb"))    

def loadSVM():
    return pickle.load(open(svmFilename, "rb"))

def main():
    
    #constroi a base de dados
    #setDatabase()
    
    #treina o SVM
    #svmObj = trainSVM()
    #saveSVM(svmObj)
    
    #testa o SVM
    svmObj = loadSVM()
    testImages(svmObj)

if __name__ == "__main__":
    main()