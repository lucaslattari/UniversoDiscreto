# -*- coding: cp1252 -*-
import cv2
import numpy as np

#carregamos as duas imagens
bolsa = cv2.imread("bolsa.png")
molusco = cv2.imread("lula.png")

#garantir que a foto do molusco tenha as mesmas
#dimensões do bolsa
alturaBolsa, larguraBolsa, _ = bolsa.shape
molusco = cv2.resize(molusco, (larguraBolsa, alturaBolsa))

#criei um monstro
bolsula = cv2.addWeighted(molusco, 0.5, bolsa, 0.5, 0)

#reduzir o tamanho da imagem do bolsula
alturaBolsula, larguraBolsula, _ = bolsula.shape
bolsula = cv2.resize(bolsula, (int(larguraBolsula * 0.25), int(alturaBolsula * 0.25)))

#recortar a face
cropBolsula = bolsula[20:240, 130:340]

#aumentar tamanho do bolsula
alturaBolsula, larguraBolsula,_ = cropBolsula.shape
cropBolsula = cv2.resize(cropBolsula, (int(larguraBolsula * 2.5), int(alturaBolsula * 2.5)))

#ver a criatura
cv2.imshow("Bolsula 2018", cropBolsula)
cv2.waitKey(0)
cv2.destroyAllWindows()
