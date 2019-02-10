import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
import pickle

def train():
    digits = datasets.load_digits()
    #plt.matshow(digits.images[0]) 
    #plt.show()
    #print(digits.images.shape)

    # To apply a classifier on this data, we need to flatten the image, to
    # turn the data in a (samples, feature) matrix:
    n_samples = len(digits.images)
    data = digits.images.reshape((n_samples, -1))
    #print(data.shape)

    # Create a classifier: a support vector classifier
    classifier = svm.SVC(gamma = "scale")

    # We learn the digits on the first half of the digits
    classifier.fit(data[:n_samples // 2], digits.target[:n_samples // 2])

    with open('filename.joblib', 'wb') as pickleFile:
        pickle.dump(classifier, pickleFile)

def load():
    digits = datasets.load_digits()
    n_samples = len(digits.images)
    data = digits.images.reshape((n_samples, -1))
    
    with open('filename.joblib', 'rb') as pickleFile:
        classifier = pickle.load(pickleFile)

    # Now predict the value of the digit on the second half:
    expected = digits.target[n_samples // 2:]
    predicted = classifier.predict(data[n_samples // 2:])

    #print("Classification report for classifier %s:\n%s\n" % (classifier, metrics.classification_report(expected, predicted)))
    #print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

    #primeiros 4 itens do dataset
    images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted))
    for index, (image, prediction) in enumerate(images_and_predictions[:12]):
        print(index)
        plt.subplot(3, 4, index + 1)
        plt.axis('off')
        plt.imshow(image, interpolation='nearest')
        plt.title('Prediction: %i' % prediction)

    plt.show()

if __name__ == "__main__":
    load()