# -*- coding: cp1252 -*-
from Tkinter import *
from PIL import Image
from PIL import ImageTk
import tkFileDialog
import cv2
import numpy as np

class GrabCutGUI(Frame):
    def __init__(self, master = None):
        #invoca o construtor da classe pai Frame
        Frame.__init__(self, master)

        #inicializar a interface gráfica
        self.iniciaUI()

    def iniciaUI(self):
        #preparando a janela
        self.master.title("Janela da Imagem Segmentada")
        self.pack()

        #computa ações de mouse
        self.computaAcoesDoMouse()

        #carregando a imagem do disco
        self.imagem = self.carregaImagemASerExibida()

        #criar um canvas que receberá a imagem
        self.canvas = Canvas(self.master, width = self.imagem.width(), height = self.imagem.height(), cursor = "cross")

        #desenhar a imagem que carreguei no canvas
        self.canvas.create_image(0, 0, anchor = NW, image = self.imagem)
        self.canvas.image = self.imagem #pra imagem não ser removida pelo garbage collector

        #posiciona todos os elementos no canvas
        self.canvas.pack()

    def computaAcoesDoMouse(self):
        self.startX = None
        self.startY = None
        self.rect   = None
        self.rectangleReady = None
        
        self.master.bind("<ButtonPress-1>", self.callbackBotaoPressionado)
        self.master.bind("<B1-Motion>", self.callbackBotaoPressionadoEmMovimento)
        self.master.bind("<ButtonRelease-1>", self.callbackBotaoSolto)

    def callbackBotaoSolto(self, event):
        if self.rectangleReady:
            #criar uma nova janela
            windowGrabcut = Toplevel(self.master)
            windowGrabcut.wm_title("Segmentation")
            windowGrabcut.minsize(width = self.imagem.width(), height = self.imagem.height())

            #criar canvas pra essa nova janela
            canvasGrabcut = Canvas(windowGrabcut, width = self.imagem.width(), height = self.imagem.height())
            canvasGrabcut.pack()

            #aplicar grabcut na imagem
            mask = np.zeros(self.imagemOpenCV.shape[:2], np.uint8)
            print(mask.shape)
            rectGcut = (int(self.startX), int(self.startY), int(event.x - self.startX), int(event.y - self.startY))
            fundoModel = np.zeros((1, 65), np.float64)
            objModel = np.zeros((1, 65), np.float64)

            #invocar grabcut
            cv2.grabCut(self.imagemOpenCV, mask, rectGcut, fundoModel, objModel, 5, cv2.GC_INIT_WITH_RECT)

            #preparando imagem final
            maskFinal = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
            imgFinal = self.imagemOpenCV * maskFinal[:,:,np.newaxis]
            for x in range(0, self.imagemOpenCV.shape[1]):
                for y in range(0, self.imagemOpenCV.shape[0]):
                    if(maskFinal[y][x] == 0):
                        imgFinal[y][x][0] = imgFinal[y][x][1] = imgFinal[y][x][2] = 255 

            #converter de volta do opencv pra Tkinter
            imgFinal = cv2.cvtColor(imgFinal, cv2.COLOR_BGR2RGB)
            imgFinal = Image.fromarray(imgFinal)
            imgFinal = ImageTk.PhotoImage(imgFinal)

            #inserir a imagem segmentada no canvas
            canvasGrabcut.create_image(0, 0, anchor = NW, image = imgFinal)
            canvasGrabcut.image = imgFinal          

    def callbackBotaoPressionadoEmMovimento(self, event):
        #novas posicoes de x e y
        currentX = self.canvas.canvasx(event.x)
        currentY = self.canvas.canvasy(event.y)

        #atualiza o retângulo a ser desenhado
        self.canvas.coords(self.rect, self.startX, self.startY, currentX, currentY)

        #verifica se existe retângulo desenhado
        self.rectangleReady = True

    def callbackBotaoPressionado(self, event):
        #convertendo o x do frame, pro x do canvas e copiando isso em startX
        self.startX = self.canvas.canvasx(event.x)
        self.startY = self.canvas.canvasy(event.y)

        if not self.rect:
            self.rect = self.canvas.create_rectangle(0, 0, 0, 0, outline="blue")

    def carregaImagemASerExibida(self):
        caminhoDaImagem = tkFileDialog.askopenfilename()

        #se a imagem existir, entra no if
        if(caminhoDaImagem > 0):
            self.imagemOpenCV = cv2.imread(caminhoDaImagem)

            #converte de opencv para o formato PhotoImage
            image = cv2.cvtColor(self.imagemOpenCV, cv2.COLOR_BGR2RGB)

            #converte de OpenCV pra PIL
            image = Image.fromarray(image)

            #converte de PIL pra PhotoImage
            image = ImageTk.PhotoImage(image)

            return image
            

def main():
    #inicializa a Tkinter
    root = Tk()

    #cria a aplicação
    appcut = GrabCutGUI(master = root)

    #cria o loop do programa
    appcut.mainloop()

if __name__ == "__main__":
    main()
