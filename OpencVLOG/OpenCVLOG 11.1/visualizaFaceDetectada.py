# -*- coding: cp1252 -*-
import numpy as np
import cv2

def main():
    #carrega um classificador de um arquivo
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    #carrega um vídeo
    cap = cv2.VideoCapture("nilce.mp4")

    while(True):
        #carrega o frame de vídeo
        frameExiste, frame = cap.read()

        #chegou ao último frame ou houve erro? então sair!
        if(frameExiste == False):
            cap.release()
            return

        #somente funciona com tons de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #detecta faces de diferentes tamanhos no frame de vídeo
        #primeiro parâmetro: a imagem

        #segundo parâmetro: especifica o quanto a imagem reduz
        #de tamanho durante a verificação

        #terceiro parâmetro: especifica quantos vizinhos
        #cada candidato a retângulo retêm
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        #para cada face detectada
        for (x, y, w, h) in faces:
            #desenhe um retângulo (imagem, posição inicial, final, cor, espessura)
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)

        cv2.imshow("deteccao", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()
