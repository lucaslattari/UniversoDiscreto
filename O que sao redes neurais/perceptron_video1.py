# -*- coding: cp1252 -*-
import numpy as np
from random import *

def escolheValoresRandomicos():

    x1 = randint(0, 1) #fator dinheiro
    x2 = randint(0, 1) #fator amigos/namorado(a)
    x3 = randint(0, 1) #fator distância

    #quanto maior o valor, mais se motiva a ir com $$$
    w1 = randint(0, 8)
    #quanto maior o valor, mais se motiva a ir com amigos
    w2 = randint(0, 8)
    #quanto maior o valor, mais se motiva a ir se for perto
    w3 = randint(0, 8)

    #quanto maior o valor, mais rígido é pra ir ao show
    limiar = randint(0, 11)

    return x1, w1, x2, w2, x3, w3, limiar

def perceptron(x1, w1, x2, w2, x3, w3, limiar):

    #fator dinheiro
    if(w1 >= 0 and w1 < 3): #se cair aqui, significa que o fã não se motiva a ir pelo dinheiro
        print("Você não se motiva com dinheiro pra ir ao show da Anitta")
    elif(w1 >= 3 and w1 < 6):
        print("Você se motiva um pouco com $$$ pra ir no show da Anitta")
    elif(w1 >= 6 and w1 < 9):
        print("Você se motiva fácil a ir ao show se tiver dinheiro!")

    #fator amigos
    if(w2 >= 0 and w2 < 3):
        print("Nem seus amigos conseguem te empurrar pra ver o show")
    elif(w2 >= 3 and w2 < 6):
        print("Seus amigos empurram um pouquinho, vai, pra ver a Anitta")
    elif(w2 >= 6 and w2 < 9):
        print("Com os seus amigos topando, é alta a probabilidade de você ir ao show")

    #fator distancia
    if(w3 >= 0 and w3 < 3):
        print("Seja longo ou perto, a distância pouco te motiva")
    elif(w3 >= 3 and w3 < 6):
        print("Se o show for perto, isso te dá um empurrãozinho pra ir ao show")
    elif(w3 >= 6 and w3 < 9):
        print("É perto e isso te dá um empurrãozão pra ir ao show da Anitta")

    print("\n")

    #imprimindo as variáveis x
    if(x1 == 0):
        print("Fator dinheiro está desligado")
    elif(x1 == 1):
        print("Fator dinheiro está ligado")
        
    if(x2 == 0):
        print("Fator amigos está desligado")
    elif(x2 == 1):
        print("Fator amigos está ligado")

    if(x3 == 0):
        print("Fator distância está desligado")
    elif(x3 == 1):
        print("Fator distância está ligado")

    print("\n")
    
    #imprimindo o limiar
    if(limiar >= 0 and limiar < 4):
        print("O limiar escolhido está frouxo")
    elif(limiar >= 4 and limiar < 8):
        print("O limiar escolhido está flexível")
    elif(limiar >= 8 and limiar < 12):
        print("O limiar escolhido está rigoroso")

    output = w1 * x1 + w2 * x2 + w3 * x3

    return output


def main():
    x1, w1, x2, w2, x3, w3, limiar = escolheValoresRandomicos()
    output = perceptron(x1, w1, x2, w2, x3, w3, limiar)

    if(output >= limiar):
        print("Matheus vai ao show da Anitta! =)")
    else:
        print("Matheus desistiu de ir na Anitta! =(")

if __name__ == "__main__":
    main()
