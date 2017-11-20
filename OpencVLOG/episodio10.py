# -*- coding: cp1252 -*-
import cv2
import numpy as np

def redimensionaImagem(imagem, tamanho):
    altura, largura, _ = imagem.shape
    return cv2.resize(imagem, (int(largura * tamanho), int(altura * tamanho)))

#carregar o logo do opencv
logo = cv2.imread("opencv.png")
logo = redimensionaImagem(logo, 0.25)

#carregar a imagem da lena
lena = cv2.imread("lena_maior.jpg")
lena = redimensionaImagem(lena, 0.8)

#local em que o logo será inserido
alturaLogo, larguraLogo, _ = logo.shape
regiaoOndeFicaraOLogo = lena[0:alturaLogo, 0:larguraLogo]

#converte para preto e branco
logoPretoEBranco = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
#limiarização/binarização do logo
_, logoBinarizado = cv2.threshold(logoPretoEBranco, 150, 255, cv2.THRESH_BINARY_INV)

logoInvertido = cv2.bitwise_not(logoBinarizado)

fundoNaImagemFinal = cv2.bitwise_and(regiaoOndeFicaraOLogo, regiaoOndeFicaraOLogo, mask = logoInvertido)
logoNaImagemFinal = cv2.bitwise_and(logo, logo, mask = logoBinarizado)

segmentoFinal = cv2.add(logoNaImagemFinal, fundoNaImagemFinal)
lena[0:alturaLogo, 0: larguraLogo] = segmentoFinal

##cv2.imshow("original", logo)
##cv2.imshow("regiao", regiaoOndeFicaraOLogo)
##cv2.imshow("binarizacao", logoBinarizado)
##cv2.imshow("bitwise not", logoInvertido)
##cv2.imshow("fundo na imagem final", fundoNaImagemFinal)
##cv2.imshow("logo na imagem final", logoNaImagemFinal)
##cv2.imshow("segmento final", segmentoFinal)
cv2.imshow("Lena", lena)

cv2.waitKey(0)
cv2.destroyAllWindows()











                      
