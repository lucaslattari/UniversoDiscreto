import cv2

img = cv2.imread("limiar.png", 0)

limiar, imgLimiar = cv2.threshold(img, 128, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow("Limiar", imgLimiar)
cv2.waitKey(0)
cv2.destroyAllWindows()
