import numpy as np
import cv2

#abre a captura de vídeo. parâmetro 0 = webcam
cap = cv2.VideoCapture(0)

while (True):
    #lê cada quadro e carrega na variável frame
    _, frame = cap.read()

    #transforma a imagem de RGB para HSV
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #intervalo de vermelho mínimo e rosa máximo
    lowerRed = np.array([25, 50, 0])
    upperRed = np.array([50, 255, 255])

    #identificação da área da embalagem
    mask = cv2.inRange(hsvImage, lowerRed, upperRed)
    #bitwise_and(primeira matriz a ser operada, segunda matriz a ser operada, 
    #especifica elementos da saida que devem ser alterados)
    #
    #dst(I) = src1(I) and src2(I) se mask(i) != 0
    result = cv2.bitwise_and(frame, frame, mask = mask)
    
    #converte para tons de cinza
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    #converte pra preto e branco usando o método de otsu
    #parametros: imagem, valor do limiar, valor do pixel transformado, atribui o método de otsu
    _,gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    #encontra a curva interligando pontos contínuos (ao longo do contorno)
    #útil para análise de formas e reconhecimento
    #funciona melhor com imagens binárias
    #primeiro parâmetro é a imagem, segundo parâmetro é o modo de retornar os contornos 
    #(RETR_TREE retorna todos os contornos, reconstruindo-os hierarquicamente)
    #
    #o terceiro parâmetro é a forma de aproximar os contornos. CHAIN_APPROX_SIMPLE aproxima
    #os pontos permitindo grande economia de memória
    #contours é uma lista com todos os contornos da imagem, hierarchy é um array que relaciona
    #cada contorno com seu grau de parentesco (filho, pai, avô)
    _, contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #se existir contornos    
    if contours:
        #retorna a área em pixels de um determinado contorno
        maxArea = cv2.contourArea(contours[0])
        contourId = 0
        i = 0
        for cnt in contours:
            if maxArea < cv2.contourArea(cnt):
                maxArea = cv2.contourArea(cnt)
                contourId = i
            i += 1
        #em cnt obtemos o contorno de maior área do conjunto de possíveis contornos
        cnt = contours[contourId]
        #retorna um retângulo que envolve o contorno em questão
        x,y,w,h = cv2.boundingRect(cnt)
        if(maxArea > 100.0):
            #desenha o retângulo vermelho com espessura 3
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)     
    
    cv2.imshow('frame', frame)
    cv2.imshow('result', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()