import cv2
import numpy as np

imagemJogador = cv2.imread("soccer.jpg")
print imagemJogador.shape
print imagemJogador.item(0, 0, 2), imagemJogador.item(0, 0, 1), imagemJogador.item(0, 0, 0)

imagemJogador.itemset((0, 0, 2), 255)
imagemJogador.itemset((0, 0, 1), 0)
imagemJogador.itemset((0, 0, 0), 0)

bola = imagemJogador[180:250, 250:315]
cv2.imwrite("bola.jpg", bola)
imagemJogador[130:200, 200:265] = bola

cv2.imwrite("soccer3.jpg", imagemJogador)
