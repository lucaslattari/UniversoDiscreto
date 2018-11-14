# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 13:18:46 2018

@author: Lucas
"""

#a biblioteca requests realiza acessos à páginas Web. a webbrowser abre abas contendo
#páginas web solicitadas. a bs4 faz parseamento de páginas html e xml, interpretando
#tags html e css
import requests, webbrowser, bs4

#é tipo um scanf da vida
print("Digite algo a ser buscado: ")
fraseBuscada = input()

#mensagem pro usuário
print("Googling " + fraseBuscada + "...")

#faz a requisição passando um termo ao buscador do google
res = requests.get('http://google.com/search?q=' + fraseBuscada)

#verifica erros, interrompendo a execução caso ocorra problemas
res.raise_for_status()

#bs4 analisa o html da página do google retornada
soup = bs4.BeautifulSoup(res.text, features="lxml")

#seleciono os elementos com classe r no interior de uma tag a (hyperlink)
linksList = soup.select('.r a')

#seleciono o menor número, que pode ser 5 ou o número de links retornados
numPagesOpen = min(5, len(linksList))

#print(linksList[0])
#print(linksList[0].get('href'))

#para cada link retornado da busca do google 
for i in range(numPagesOpen):
    print("Opening " + linksList[i].get('href')[7:])
    #abro uma aba pro link em questão
    webbrowser.open('http://google.com' + linksList[i].get('href'))

print("Done.")