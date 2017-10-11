import cv2

imagemCarregada = cv2.imread("exemplo.jpg", 0)

cv2.imshow("ImagemCarregada", imagemCarregada)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("imagemSalva.jpg", imagemCarregada)
