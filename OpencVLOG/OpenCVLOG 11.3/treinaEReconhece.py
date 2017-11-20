# -*- coding: cp1252 -*-
import numpy as np
import cv2
import os

def criaArquivoDeRotulo(pasta):
    label = 0
    f = open("TRAIN", "w+")
    for dirPrincipal, nomeDirs, nomeArqs in os.walk(pasta):
        for subDir in nomeDirs:
            caminhoPasta = os.path.join(dirPrincipal, subDir)
            for filename in os.listdir(caminhoPasta):
                caminhoAbs = caminhoPasta + "\\" + filename
                f.write(caminhoAbs + ";" + str(label) + "\n")
            label = label + 1
    f.close()

def criaDicionarioDeImagens(fPoint):
    lines = fPoint.readlines()

    dicionarioDeFotos = {}
    for line in lines:
        filename, label = line.rstrip().split(';')
        if dicionarioDeFotos.has_key(int(label)):
            current_files = dicionarioDeFotos.get(label)
            np.append(current_files, cv2.imread(filename, 0))
        else:
            dicionarioDeFotos[int(label)] = cv2.imread(filename, 0)

    #ao final, cria um dicionário que na posição 0 (rótulo
    #referente a camila, por exemplo, tem-se uma lista contendo
    #todas as fotos da camila que estão na base de teste

    #na posição 1 do dicionário, teremos uma lista com todas as
    #fotos do pirula
    return dicionarioDeFotos
    
def treinaModelo(dicionarioDeYoutubers):
    #cria treina as autofaces
    model = cv2.face.EigenFaceRecognizer_create()
    model.train(dicionarioDeYoutubers.values(), np.array(dicionarioDeYoutubers.keys()))
    return model

def reconheceVideo(modelo, arquivo):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(arquivo) #inicia captura da câmera
    counterFrames = 0;
    while(counterFrames < 1000): #quando chegar ao milésimo frame, para
        ret, img = cap.read()

        #frame não pode ser obtido? entao sair
        if(ret == False):
            cap.release()
            return

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        #se nenhuma face for achada, continue
        if not np.any(faces):
            continue

        rostos = []
        #achou uma face? recorte ela (crop)
        for (x, y, w, h) in faces:
            rosto = img[y:y+h, x:x+w]
            #esse rosto é grande o bastante pra ser levado
            #em conta
            if(((x + w) - x) > 100 and ((y + h) - y) > 100):

                #modifica o tamanho dele pra se ajustar ao
                #treinamento e pinte pra tons de cinza
                rosto = cv2.resize(rosto, (255, 255))
                rosto = cv2.cvtColor(rosto, cv2.COLOR_BGR2GRAY)

                #aqui ele recebe a foto e diz qual rótulo
                #pertence (ou seja, quem é)
                label = modelo.predict(rosto)
                font = cv2.FONT_HERSHEY_SIMPLEX
                if(label[0] == 0): #é o Leon?
                    #então bota um texto em cima da caixinha
                    cv2.putText(img,'Leon',(x - 20,y + h + 60), font, 3,(255,0,0),5,cv2.LINE_AA)
                    #pinte um retângulo ao redor do rosto do leon
                    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                if(label[0] == 1): #é a Nilce?
                    #então bota um texto em cima da caixinha
                    cv2.putText(img,'Nilce',(x - 20,y + h + 60), font, 3,(0,0,255),5,cv2.LINE_AA)
                    #pinte um retângulo ao redor do rosto da nilce
                    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

        #redimensione só pra ficar bonito na tela
        img = cv2.resize(img, (int(0.75 * img.shape[1]), int(0.75 * img.shape[0])))

        #exibir na tela!
        cv2.imshow("reconhecimento", img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def main():
    #cria um arquivo que indica que aquela foto pertence
    #a tal pessoa
    criaArquivoDeRotulo("data")

    #carrega o arquivo
    fPoint = open("TRAIN", "r")

    #constrói um dicionário dos dados lidos no texto
    dicionarioDeFotos = criaDicionarioDeImagens(fPoint)
    modelo = treinaModelo(dicionarioDeFotos)

    #DO THE F* MAGIC DUDE
    reconheceVideo(modelo, "nilce_leon.mp4")
    
if __name__ == "__main__":
    main()
