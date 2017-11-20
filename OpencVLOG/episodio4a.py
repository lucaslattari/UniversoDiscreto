import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("soccer.jpg", 0)
plt.hist(img.ravel(), 256, [0, 256])
cv2.imshow("Imagem Original", img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
