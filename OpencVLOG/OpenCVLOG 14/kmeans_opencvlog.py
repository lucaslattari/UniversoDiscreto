import numpy as np
import cv2

def computeKmeans(image):
    Z = image.reshape((-1, 3))
    Z = np.float32(Z)
    
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 40, 0.1)
    K = 256
    
    _, labels, centroides = cv2.kmeans(Z, K, None, criteria, 40, cv2.KMEANS_RANDOM_CENTERS)
    
    centroides = np.uint8(centroides)
    imagemColoridaComCentroides = centroides[labels.flatten()]
    imagemFinal = imagemColoridaComCentroides.reshape((image.shape))
    
    cv2.imshow("original", image)
    cv2.imshow("resultado kmeans", imagemFinal)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image = cv2.imread('vingadores.jpg')
    computeKmeans(image)