# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 22:48:00 2018

@author: Lucas
"""

import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")

try:
    res.raise_for_status()
    
    file = open("RomeuEJulieta.txt", "wb")
    
    for chunk in res.iter_content(100000):
        file.write(chunk)
except Exception as exc:
    print("Houve um erro: %s" % (exc))

#if(res.status_code == requests.codes.ok):
#    print("Tamanho do arquivo: " + str(len(res.text)))
#    print("Conteúdo do arquivo: " + res.text)
#else:
#    print("Erro: " + str(res.status_code))