import cv2
import numpy as np

tamanhoImg = 0.5

def computaFiltroRC(img):
    largura, altura, canais = img.shape
    dstImg = np.zeros((largura, altura, canais), np.uint8)
    b, g, r = cv2.split(img)
    cv2.addWeighted(b, 0.5, g, 0.5, 0, b)
    cv2.merge((b, b, r), dstImg)

    return dstImg

def computaFiltroCMV(img):
    largura, altura, canais = img.shape
    dstImg = np.zeros((largura, altura, canais), np.uint8)
    b, g, r = cv2.split(img)
    cv2.max(b, g, b)
    cv2.max(b, r, b)
    cv2.merge((b, g, r), dstImg)

    return dstImg

if __name__ == "__main__":
    
    #carregar o arquivo de imagem
    originalImg = cv2.imread("prince.jpg")
    largura, altura, _ = originalImg.shape

    #redimensiona a imagem
    largura *= tamanhoImg
    altura *= tamanhoImg
    largura = int(largura)
    altura = int(altura)
    originalImg = cv2.resize(originalImg, (altura, largura))

    #filtro RC
    rcImg = computaFiltroRC(originalImg)

    #filtro cmv
    cmvImg = computaFiltroCMV(originalImg)

    #exibir na tela
    finalImg = np.zeros((largura * 2, altura * 2, 3), np.uint8)
    finalImg[0:largura, 0:altura] = originalImg
    finalImg[0:largura, altura:altura * 2] = rcImg
    finalImg[largura:largura * 2, 0:altura] = cmvImg
 
    cv2.imshow("img", finalImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



    
