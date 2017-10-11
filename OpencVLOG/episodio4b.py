import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("soccer.jpg")
color = ('b', 'g', 'r')

for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color = col)
    plt.xlim([0, 256])
cv2.imshow("Imagem Original", img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
