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

#rootFolder + trainFolder + objFolder
#rootFolder + trainFolder + bkgFolder
#rootFolder + cropTrainFolder + objFolder
#rootFolder + cropTrainFolder + bkgFolder
#rootFolder + testFolder + objFolder
#rootFolder + testFolder + bkgFolder
#rootFolder + testTrainFolder + objFolder
#rootFolder + testTrainFolder + bkgFolder

rootFolder = "INRIAPerson\\"
trainFolder = "Train\\"
testFolder = "Test\\"
objFolder = "pos\\"
bkgFolder = "neg\\"
cropTrainFolder = "trainLucas\\"
cropTestFolder = "testLucas\\"

imagesListPos = "pos.lst"
imagesListNeg = "neg.lst"
annotationsList = "annotations.lst"
svmFilename = "obj.svm"

widthWindow = 64
heightWindow = 128

orientationsParam = 9
pixelsPerCellParam = 8
cellsPerBlockParam = 2

def extractFilenamesFromFolder(path, file):
    listFilenames = []
    with open(path + file) as f:
        listFilenames = [line.rstrip() for line in f]
    return listFilenames

def cropRegionOfEachPosImage(path, folder, listOfImages, ListOfAnnotations, isTrain):
    i = 0
    if(isTrain == 1):
        print("Montando base de imagens de pedestres para treino.")
    else:
        print("Montando base de imagens de pedestres para teste.")

    for eachAnnotationFile in tqdm(ListOfAnnotations):
        with open(path + eachAnnotationFile) as file:
            data = file.readlines()
        bboxLine = str(data[-2:])
        m = re.search(r"\([0-9]+, [0-9]+\) - \([0-9]+, [0-9]+\)", bboxLine)
        listOfNumbers = re.findall(r"\d+", m.group())
        
        xmin = int(listOfNumbers[0])
        ymin = int(listOfNumbers[1])
        xmax = int(listOfNumbers[2])
        ymax = int(listOfNumbers[3])

        #pra não ler as imagens flip do txt        
        if listOfImages[i].find("flip") != -1:
            continue

        #nesse momento temos um vetor com xmin, ymin, xmax, ymax de cada imagem pos
        img = cv2.imread(path + listOfImages[i])
        img = img[ymin : ymax , xmin : xmax]
        stringImg = listOfImages[i].split("/", 1)
        cv2.imwrite(path + folder + stringImg[-1], img)

        #flip image
        if(isTrain == 1):
            flipImg = cv2.flip(img, 1)
            cv2.imwrite(rootFolder + cropTrainFolder + objFolder + "flip_" + str(i) + ".png", flipImg)
            #with open(rootFolder + trainFolder + imagesListPos, "a") as myfile:
            #    myfile.write("\nTrain/pos/flip_" + str(i) + ".png")
        else:
            flipImg = cv2.flip(img, 1)
            cv2.imwrite(rootFolder + cropTestFolder + objFolder + "flip_" + str(i) + ".png", flipImg)
            #with open(rootFolder + testFolder + imagesListPos, "a") as myfile:
            #    myfile.write("\nTest/pos/flip_" + str(i) + ".png")
        i += 1

def cropRegionOfEachNegImage(path, folder, listOfImages, isTrain):
    if(isTrain == 1):
        print("Montando base de imagens de não pedestres para treino.")
    else:
        print("Montando base de imagens de não pedestres para teste.")
    for eachImageFile in tqdm(listOfImages):
        img = cv2.imread(path + eachImageFile)
        img = img[0:heightWindow , 0:widthWindow]
        stringImg = eachImageFile.split("/", -1)
        cv2.imwrite(path + folder + bkgFolder + stringImg[2], img)
    
def setDatabase():
    #train
    vectorOfFilenameImagesPos = extractFilenamesFromFolder(rootFolder + trainFolder, imagesListPos)
    vectorOfFilenameImagesNeg = extractFilenamesFromFolder(rootFolder + trainFolder, imagesListNeg)
    vectorOfFilenameAnnotations = extractFilenamesFromFolder(rootFolder + trainFolder, annotationsList)
    cropRegionOfEachPosImage(rootFolder, cropTrainFolder, vectorOfFilenameImagesPos, vectorOfFilenameAnnotations, 1)
    cropRegionOfEachNegImage(rootFolder, cropTrainFolder, vectorOfFilenameImagesNeg, 1)

    vectorOfFilenameImagesPos = []
    vectorOfFilenameImagesNeg = []
    vectorOfFilenameAnnotations = []

    #test
    vectorOfFilenameImagesPos = extractFilenamesFromFolder(rootFolder + testFolder, imagesListPos)
    vectorOfFilenameImagesNeg = extractFilenamesFromFolder(rootFolder + testFolder, imagesListNeg)
    vectorOfFilenameAnnotations = extractFilenamesFromFolder(rootFolder + testFolder, annotationsList)
    cropRegionOfEachPosImage(rootFolder, cropTestFolder, vectorOfFilenameImagesPos, vectorOfFilenameAnnotations, 0)
    cropRegionOfEachNegImage(rootFolder, cropTestFolder, vectorOfFilenameImagesNeg, 0)

def trainSVM():
    X = np.empty(0)
    Y = np.empty(0)
    dimensionOfFeatureVector = 0
    
    print("Extraindo feature HOG da base de pedestres.")
    vectorOfFilenameImagesPos = extractFilenamesFromFolder(rootFolder + trainFolder, imagesListPos)
    for eachImage in tqdm(vectorOfFilenameImagesPos):
        eachImage = eachImage.split("/", -1)
        eachImage = rootFolder + cropTrainFolder + objFolder + eachImage[2]
        
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
            Y = np.array([1])
        else:
            Y = np.append(Y, np.array([1]))
             
    print("Extraindo feature HOG da base de não pedestres.\n")
    vectorOfFilenameImagesNeg = extractFilenamesFromFolder(rootFolder + trainFolder, imagesListNeg)
    for eachImage in tqdm(vectorOfFilenameImagesNeg):
        eachImage = eachImage.split("/", -1)
        eachImage = rootFolder + cropTrainFolder + bkgFolder + eachImage[2]

        img = cv2.imread(eachImage, 0)
        img = img[0:heightWindow , 0:widthWindow]
        H = feature.hog(img, orientations=orientationsParam, pixels_per_cell=(pixelsPerCellParam, pixelsPerCellParam), cells_per_block=(cellsPerBlockParam, cellsPerBlockParam), block_norm='L2-Hys', feature_vector = True)
        H = np.array(H)
        
        X = np.append(X, H)
        Y = np.append(Y, np.array([0]))
             

    print("Treinando o SVM.\n")
    X = np.reshape(X, (-1, dimensionOfFeatureVector))

    svm = SVC(C=1.0)
    svm.fit(X, Y)
    return svm

def testImages(svmObj):
    acc = 0.0
    total = 0.0
    font = cv2.FONT_HERSHEY_SIMPLEX
    vectorOfFilenameImagesPos = extractFilenamesFromFolder("INRIAPerson\\Test\\", "pos.lst")
    print("Classificando imagens de pedestres.")
    for eachImage in tqdm(vectorOfFilenameImagesPos):
        eachImage = eachImage.split("/", -1)
        eachImage = rootFolder + cropTestFolder + objFolder + eachImage[2]
        
        img = cv2.imread(eachImage, 0)
        imgShow = cv2.imread(eachImage, 1)
        imgShow = cv2.resize(imgShow, (400, 800))
        h, w, _ = imgShow.shape

        img = cv2.resize(img, (widthWindow, heightWindow))
        H = feature.hog(img, orientations=orientationsParam, pixels_per_cell=(pixelsPerCellParam, pixelsPerCellParam), cells_per_block=(cellsPerBlockParam, cellsPerBlockParam), block_norm='L2-Hys', feature_vector = True)
        X = np.array(H)
        X = np.reshape(X, (-1, X.shape[0]))

        if(svmObj.predict(X) == 1):
            cv2.putText(imgShow, 'Pedestre', (0, int(h * 0.05)), font, 1, (0, 0, 255), 3, cv2.LINE_AA)
            acc+=1.0
        else:
            cv2.putText(imgShow, 'Nao Pedestre', (0, int(h * 0.05)), font, 1, (255, 0, 0), 3, cv2.LINE_AA)
            #print(eachImage)

        #cv2.imshow("Resultado", imgShow)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        total += 1.0
    print("Acurácia de Pedestres = " + str(acc / total))

    acc = 0.0
    vectorOfFilenameImagesNeg = extractFilenamesFromFolder("INRIAPerson\\Test\\", "neg.lst")
    total = 0.0
    print("Classificando imagens de não pedestres.")
    for eachImage in tqdm(vectorOfFilenameImagesNeg):
        eachImage = eachImage.split("/", -1)
        eachImage = rootFolder + cropTestFolder + bkgFolder + eachImage[2]
        
        img = cv2.imread(eachImage, 0)
        imgShow = cv2.imread(eachImage, 1)
        imgShow = cv2.resize(imgShow, (400, 800))
        h, w, _ = imgShow.shape

        img = cv2.resize(img, (widthWindow, heightWindow))
        H = feature.hog(img, orientations=orientationsParam, pixels_per_cell=(pixelsPerCellParam, pixelsPerCellParam), cells_per_block=(cellsPerBlockParam, cellsPerBlockParam), block_norm='L2-Hys', feature_vector = True)
        X = np.array(H)
        X = np.reshape(X, (-1, X.shape[0]))

        if(svmObj.predict(X) == 0):
            cv2.putText(imgShow, 'Nao Pedestre', (0, int(h * 0.05)), font, 1, (255, 0, 0), 3, cv2.LINE_AA)
            acc+=1.0
        else:
            cv2.putText(imgShow, 'Pedestre', (0, int(h * 0.05)), font, 1, (0, 0, 255), 3, cv2.LINE_AA)
            #print(eachImage)

        #cv2.imshow("Resultado", imgShow)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        total += 1.0

    print("Acurácia de não pedestres = " + str(acc / total))
    
def saveSVM(obj):
    pickle.dump(obj, open(svmFilename, "wb"))    

def loadSVM():
    return pickle.load(open(svmFilename, "rb"))

def main():
    
    #constroi a base de dados
    #setDatabase()
    
    #treina o SVM
    svmObj = trainSVM()
    saveSVM(svmObj)
    
    #testa o SVM
    #svmObj = loadSVM()
    #testImages(svmObj)

if __name__ == "__main__":
    main()