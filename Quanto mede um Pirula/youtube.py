api_key="AIzaSyCQcYk7Hwdcwi1FFIh4L3yGrVBA4e8GfHQ" #minha API

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import json
import urllib
import re
import operator

#id do canal do pirula
channel_id="UCdGpd0gNn38UKwoncZd9rmA" 

#link para API do Google que fornece informações do Youtube
base_video_url = 'https://www.youtube.com/watch?v='
base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=50'.format(api_key, channel_id)
url = first_url

#minhas medições
horasTotal = 0
minutosTotal = 0
segundosTotal = 0
totalDeVideos = 0

videosMaisCurtidos = {}
videosMaisDescurtidos = {}

while True:
    #informações são solicitadas aqui
    inp = urllib.urlopen(url)
    resp = json.load(inp)

    #para cada informação recebida
    for i in resp['items']:
        #é vídeo do youtube? Se sim, entra aqui!
        if i['id']['kind'] == "youtube#video":

            #"pede" para a API do Youtube detalhes sobre
            #conteúdo do vídeo
            searchUrl="https://www.googleapis.com/youtube/v3/videos?id="+i['id']['videoId']+"&key="+api_key+"&part=contentDetails"
            response = urllib.urlopen(searchUrl).read()
            data = json.loads(response)
            all_data=data['items']
            contentDetails=all_data[0]['contentDetails']

            #pede aqui a duração de cada vídeo
            duration=contentDetails['duration']
            print(i['snippet']['title'])
            print(duration)

            #expressão regular para extrair as horas, minutos
            #e segundos
            result = re.search('PT(.*)H', duration)
            if(result == None):
                result = re.search('PT(.*)M', duration)
                if(result == None):
                    result = re.search('PT(.*)S', duration)
                    segundosTotal += int(result.group(1))
                else:
                    minutosTotal += int(result.group(1))
            else:
                horasTotal += int(result.group(1))

                result = re.search('H(.*)M', duration)
                minutosTotal += int(result.group(1))

            result = re.search('M(.*)S', duration)
            if(result != None):
                segundosTotal += int(result.group(1))

            #peço agora pra API do Youtube detalhes sobre
            #as estatísticas do vídeo
            searchUrl="https://www.googleapis.com/youtube/v3/videos?id="+i['id']['videoId']+"&key="+api_key+"&part=statistics"
            response = urllib.urlopen(searchUrl).read()
            data = json.loads(response)
            video = data["items"]

            #esse vídeo contém likes e dislikes? Se sim,
            #entra aqui
            if("likeCount" in video[0]["statistics"]):
                #constrói um dicionário relacionando o nome do vídeo
                #e seu número de likes e dislikes
                videosMaisCurtidos.update({i['snippet']['title']: int(video[0]["statistics"]["likeCount"])})
                videosMaisDescurtidos.update({i['snippet']['title']: int(video[0]["statistics"]["dislikeCount"])})

            totalDeVideos += 1
    try:
        #A API "repassa" blocos de 50 vídeos por vez
        #assim, eu peço aqui o bloco contendo os
        #próximos 50 vídeos
        next_page_token = resp['nextPageToken']
        url = first_url + '&pageToken={}'.format(next_page_token)
    except:
        break

#gambiarras para aparentemente "corrigir" a API do Youtube
totalDeVideos += 12
minutosTotal += 14 + 15 + 3 + 10 + 11 + 12 + 12 + 6 + 16 + 16 + 10 + 31
segundosTotal += 50 + 28 + 39 + 7 + 23 + 30 + 16 + 5 + 12 + 11 + 19 + 20

#calcula o tempo total da "discografia" do Pirula
segundosTotal = horasTotal * 60 * 60 + minutosTotal * 60
mediaSegundos = segundosTotal / totalDeVideos
print("Total de Segundos: " + str(segundosTotal))
print("Total de Vídeos: " + str(totalDeVideos))

minutosTotal = segundosTotal / 60
segundosTotal = segundosTotal % 60
horasTotal = minutosTotal / 60
minutosTotal = minutosTotal % 60
diasTotal = horasTotal / 24
horasTotal = horasTotal % 24

#mede aqui quanto é "um pirula" por meio da média
mediaMinutos = mediaSegundos / 60
mediaSegundos = mediaSegundos % 60
mediaHoras = mediaMinutos / 60
mediaMinutos = mediaMinutos % 60

print("Tempo Total:" + str(diasTotal) + "D" + str(horasTotal) + "H" + str(minutosTotal) + "M" + str(segundosTotal) + "S")
print("Media Total:" + str(mediaHoras) + "H" + str(mediaMinutos) + "M" + str(mediaSegundos) + "S")

print("\n---------------------------\n5 videos mais curtidos:\n")

#ordena os 5 primeiros vídeos em número de curtidas
i = 0
for w in sorted(videosMaisCurtidos, key=videosMaisCurtidos.get, reverse=True):
  print w, videosMaisCurtidos[w]
  i += 1
  if(i == 5):
      break

print("\n---------------------------\n5 videos mais descurtidos:\n")

#ordena os 5 primeiros vídeos em número de descurtidas
i = 0  
for w in sorted(videosMaisDescurtidos, key=videosMaisDescurtidos.get, reverse=True):
  print w, videosMaisDescurtidos[w]
  i += 1
  if(i == 5):
      break
    
