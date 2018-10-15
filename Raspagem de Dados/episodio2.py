# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 21:31:05 2018

@author: Lucas
"""

"""
A beautifulsoup é um módulo para a extração de informações de uma página HTML
(e é muito melhor para esse propósito do que expressões regulares). Para esse
tutorial vamos instalar a versão 4 da beautiful soup, que é instalada por meio
da pip install beautifulsoup4 (conda install beautifulsoup4). Enquanto para
instalar vc usa beautifulsoup4, na hora de importá-la você chama import bs4
"""

import bs4

"""
para esse capítulo, vamos fazer o parseamento, ou seja, analisar e identificar
partes de um arquivo HTML. Vamos usar um html de exemplo que eu também vou deixar
no github para você acompanhar, que será o exemplo.html.

Como você pode ver, mesmo um HTML simples envolve o uso de várias tags e atributos.
Para sites reais da internet a complexidade é tanta que fica difícil fazer essa análise.
Entretanto, a beautiful soup torna o processamento de HTML muito mais simplificado.
"""

import requests, bs4
res = requests.get('http://nostarch.com')
try:
    res.raise_for_status()
    objectBS = bs4.BeautifulSoup(res.text, features="lxml")
    #print(res.text)
except Exception as exc:
    print("Houve um erro: %s" % (exc))

"""
A função bs4.BeautifulSoup(res.tex) deve ser chamada com uma string contendo o HTML
a ser parseado. Essa função retorna um objeto BeautifulSoup. Teste o código acima
conectado a internet.

Esse código usa requests.get() para baixar a página principal do site nostarch.com
e então passa um atributo texto como resposta para BeautifulSoup()

O objeto BeautifulSoup fica armazenado na variável objectBS

Você também pode carregar um HTML do seu disco rígido, passando um objeto File
para bs4.BeautifulSoup().

Vamos entender isso com o código abaixo
"""

try:
    arquivoDeExemplo = open('exemplo.html')
    objSoup = bs4.BeautifulSoup(arquivoDeExemplo, features="lxml")
    #print(objSoup)
except Exception as exc:
    print("Houve um erro: %s" % (exc))
    
"""
    Você pode obter um elemento de uma página Web a partir de um objeto BeautifulSoup
por meio da execução do método select(), passando por parâmetro uma string contendo
um seletor CSS para o elemento que você está procurando. Seletores são parecidos com
expressões regulares: eles especificam um padrão a ser buscado em um arquivo HTML

Vamos entender com um exemplo. Note que no código HTML temos um <span> com id = author.
Podemos extrair esse segmento do arquivo HTML com o código abaixo
"""

try:
    arquivoDeExemplo = open('exemplo.html')
    objSoup = bs4.BeautifulSoup(arquivoDeExemplo, features="lxml")
    listAuthor = objSoup.select('#author')
     
    print("Analise das tags com id=author")
    print("Total de elementos: " + str(len(listAuthor)))
    print("Tag Completa: " + str(listAuthor[0]))
    print("Primeiro autor: " + listAuthor[0].getText())
    print("Tag Completa: " + str(listAuthor[1]))
    print("Segundo autor: " + listAuthor[1].getText())
except Exception as exc:
    print("Houve um erro: %s" % (exc))
    
"""
    Esse código extrai o elemento com id=author do HTML de exemplo. Ele retorna
uma lista com todos os elementos do arquivo que contém id=author. Invocando
getText() no elemento faz com que a gente retorne o texto no interior da tag.

Vamos agora testar algo diferente: retornar todos os parágrafos <p> do HTML 
"""

try:
    arquivoDeExemplo = open('exemplo.html')
    objSoup = bs4.BeautifulSoup(arquivoDeExemplo, features="lxml")
    listP = objSoup.select('p')
                                   
    print("\nAnalise das tags com <p>")
    print("Total de elementos: " + str(len(listP)))
    for eachP in listP:
        print(eachP.getText())
except Exception as exc:
    print("Houve um erro: %s" % (exc))

"""
Para fechar, vamos aprender a extrair o id de um determinado span
"""

try:
    arquivoDeExemplo = open('exemplo.html')
    objSoup = bs4.BeautifulSoup(arquivoDeExemplo, features="lxml")
    listSpan = objSoup.select('span')
                                   
    print("\nAnalise das tags com <span>")
    print("Total de elementos: " + str(len(listSpan)))
    firstSpan = listSpan[0]
    print("O ID desse span eh: " + firstSpan.get('id'))
except Exception as exc:
    print("Houve um erro: %s" % (exc))