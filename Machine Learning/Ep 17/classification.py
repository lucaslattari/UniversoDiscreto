import preprocessing as pre

class ClassificationModel:
    def predictModel(classifier, X, isDecisionTree):
        if(isDecisionTree == False):
            X = X[0]
        return classifier.predict(X)

    def evaluateModel(yPred, yTest):
        from sklearn.metrics import confusion_matrix
        confusionMatrix = confusion_matrix(yTest, yPred)

        return confusionMatrix

    def preprocessData(filename, useFeatureScaling):
        X, y, csv = pre.loadDataset(filename, ",")
        X = pre.fillMissingData(X, 2, 3)

        #sex
        X = pre.computeCategorization(X)
        #embark
        X = pre.computeCategorization(X)

        XTrain, XTest, yTrain, yTest = pre.splitTrainTestSets(X, y, 0.15)

        if(useFeatureScaling == True):
            XTrain = pre.computeScaling(XTrain)
            XTest = pre.computeScaling(XTest)

        return XTrain, XTest, yTrain, yTest
