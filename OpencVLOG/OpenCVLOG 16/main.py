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
import numpy as np

if __name__ == "__main__":
    
    #carrega a imagem em preto e branco
    imagemPlaca = cv2.imread("texto2.png")
    
    #salva a imagem contendo a placa em um arquivo temporário do Windows para aplicar OCR
    filenameImagemPlaca = "{}.png".format(os.getpid())
    cv2.imwrite(filenameImagemPlaca, imagemPlaca)
    
    #carrega a imagem usando a biblioteca PIL/Pillow e aplica OCR
    textoPlaca = pyt.image_to_string(Image.open(filenameImagemPlaca))

    #deleta arquivo temporário
    os.remove(filenameImagemPlaca)
    
    print("Texto: " + textoPlaca)

    imagemPlaca = cv2.resize(imagemPlaca,None,fx=1, fy=1, interpolation = cv2.INTER_CUBIC)

    cv2.imshow("imagem contendo o texto", imagemPlaca)
    cv2.waitKey(0)
    cv2.destroyAllWindows()