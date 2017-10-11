# -*- coding: cp1252 -*-
#espaço de cor RC
import cv2
import numpy as np

def inicializaImagem(altura, largura, canais):
    return np.zeros((altura, largura, canais), np.uint8)

def computaFiltroRC(img):
    larg, alt, _ = img.shape
    dst = inicializaImagem(larg, alt, 3)
    b, g, r = cv2.split(img)
    cv2.addWeighted(b, 0.5, g, 0.5, 0, b)
    cv2.merge((b, b, r), dst)

    return dst

def computaFiltroCGA(img):
    larg, alt, _ = img.shape
    dst = inicializaImagem(larg, alt, 3)

    b, g, r = cv2.split(img)
    cv2.max(b, g, b)
    cv2.max(b, r, b)
    cv2.merge((b, g, r), dst)

    return dst

#função main
if __name__ == "__main__":
    cap = cv2.VideoCapture('serenata.mp4')

    while(cap.isOpened()):
        ret, frame = cap.read()

        larguraImg, alturaImg,_  = frame.shape
        originalImg = cv2.resize(frame, (int(alturaImg * 0.4), int(larguraImg * 0.4)))
        alturaImg   *= 0.4
        larguraImg  *= 0.4
        rcImg       = computaFiltroRC(originalImg)
        cgaImg      = computaFiltroCGA(originalImg)

        finalImg = inicializaImagem(larguraImg * 2, alturaImg * 2, 3)
        finalImg[0:larguraImg, 0:alturaImg] = originalImg
        finalImg[0:larguraImg, alturaImg:alturaImg*2] = rcImg
        finalImg[larguraImg: larguraImg * 2, 0:alturaImg] = cgaImg

        cv2.imshow("final", finalImg)

        if cv2.waitKey(40) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
