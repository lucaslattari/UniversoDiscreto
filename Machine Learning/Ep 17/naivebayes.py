from classification import ClassificationModel

class NaiveBayes(ClassificationModel):
    def computeModel(XTrain, yTrain):
        from sklearn.naive_bayes import GaussianNB

        classifier = GaussianNB()
        classifier.fit(XTrain[0], yTrain)

        return classifier

    def computeExample(filename):
        XTrain, XTest, yTrain, yTest = ClassificationModel.preprocessData(filename, True)

        classifier = NaiveBayes.computeModel(XTrain, yTrain)
        yPred = ClassificationModel.predictModel(classifier, XTest, False)
        return ClassificationModel.evaluateModel(yPred, yTest)

if __name__ == "__main__":
    print(NaiveBayes.computeExample("titanic.csv"))
