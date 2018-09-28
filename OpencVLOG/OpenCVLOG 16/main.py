# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 19:19:40 2018

@author: Lucas
"""
#PASSO 1
#instala a biblioteca do tesseract no windows
#https://excellmedia.dl.sourceforge.net/project/tesseract-ocr-alt/tesseract-ocr-setup-3.02.02.exe

#PASSO 2
#invoca o comando pip3 install pytesseract no cmd do windows

#PASSO 3
#inclui o executável da biblioteca do tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

from PIL import Image
import pytesseract as pyt
import cv2
import os

if __name__ == "__main__":
    
    #carrega a imagem colorida
    imagem = cv2.imread("texto.png")
    
    #salva a imagem em um arquivo temporário do Windows para aplicar OCR
    filenameImagem = "{}.png".format(os.getpid())
    cv2.imwrite(filenameImagem, imagem)
    
    #carrega a imagem usando a biblioteca PIL/Pillow e aplica OCR
    texto = pyt.image_to_string(Image.open(filenameImagem))

    #deleta arquivo temporário
    os.remove(filenameImagem)
    
    print("Texto: " + texto)

    #redimensiona só pra ser exibido ao final
    imagem = cv2.resize(imagem,None,fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)

    #exibe a imagem
    cv2.imshow("imagem contendo o texto", imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()