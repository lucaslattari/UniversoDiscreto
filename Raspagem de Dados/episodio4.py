# encoding: utf-8
"""
Created on Thu Nov  8 13:18:46 2018

@author: Lucas

Para funcionar você deve instalar:
  pip install requests
  pip install bs4
  pip install pyttsx3
  pip install SpeechRecognition
  pip install pyaudio
  pip install lxml
  pip install pypiwin32‑224+dummy‑py2.py3‑none‑any.whl
  python.exe Scripts/pywin32_postinstall.py -install
"""

#a biblioteca requests realiza acessos à páginas Web. a webbrowser abre abas contendo
#páginas web solicitadas. a bs4 faz parseamento de páginas html e xml, interpretando
#tags html e css
import requests, webbrowser, bs4, re, unicodedata, pyttsx3
from unicodedata import normalize
import speech_recognition as sr

def removeColcheteEParentese(text):
  return re.sub("[\(\[].*?[\)\]]", "", text)

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def executaIAsmim():
  microfone = sr.Recognizer()
  with sr.Microphone() as source:

    #Chama a funcao de reducao de ruido disponivel na speech_recognition
    microfone.adjust_for_ambient_noise(source)
    
    #Avisa ao usuario que esta pronto para ouvir
    print("Diga alguma coisa: ")

    #Armazena a informacao de audio na variavel
    audio = microfone.listen(source)

  try:
    #Passa o audio para o reconhecedor de padroes do speech_recognition
    fraseBuscada = microfone.recognize_google(audio,language='pt-BR')

    #Após alguns segundos, retorna a frase falada
    print("Voce disse: " + fraseBuscada)

    if fraseBuscada == "Quem te criou":
      engine = pyttsx3.init()
      engine.say("Meu nome é IAsmim e fui criada pelo genial Lucas Grassano Lattari")
      engine.say("Só um gênio da programação como o Lucas seria capaz de criar algo incrivel como eu")
      engine.say("Se inscreva no canal Universo Discreto e acompanhe as novidades que estão por vir. São sensacionais!")
      engine.runAndWait()
    else:

      #faz a requisição passando um termo ao buscador do google
      page = requests.get('https://pt.wikipedia.org/wiki/' + fraseBuscada)

      #verifica erros, interrompendo a execução caso ocorra problemas
      page.raise_for_status()

      #bs4 analisa o html da página do google retornada
      soup = bs4.BeautifulSoup(page.content, features="lxml")

      allText = ''

      #procure por tags html do tipo div
      data = soup.find('div', class_='mw-parser-output')

      #para todo paragrafo (<p>) lido
      for paragraph in data.find_all('p'):

          #extraia o texto e faça conversão para formato UNICODE
          allText += ''.join(ch for ch in unicodedata.normalize('NFKD', cleanhtml(str(paragraph)))
              if not unicodedata.combining(ch))

      allText = removeColcheteEParentese(allText)

      #motor que transforma texto em áudio
      engine = pyttsx3.init()
      engine.say(allText)
      engine.runAndWait()

    print("Done.")

  #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
  except sr.UnknownValueError:
    print("Não entendi")

executaIAsmim()
