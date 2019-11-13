from classification import ClassificationModel

class DecisionTree(ClassificationModel):
    def computeModel(XTrain, yTrain):
        from sklearn.tree import DecisionTreeClassifier

        classifier = DecisionTreeClassifier(criterion = 'entropy')
        classifier.fit(XTrain, yTrain)

        return classifier

    def computeExample(filename):
        XTrain, XTest, yTrain, yTest = ClassificationModel.preprocessData(filename, False)

        classifier = DecisionTree.computeModel(XTrain, yTrain)
        yPred = ClassificationModel.predictModel(classifier, XTest, True)
        return ClassificationModel.evaluateModel(yPred, yTest)

if __name__ == "__main__":
    print(DecisionTree.computeExample("titanic.csv"))
