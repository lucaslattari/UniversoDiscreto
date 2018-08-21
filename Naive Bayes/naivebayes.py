# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 19:07:07 2018

@author: Lucas
"""

#natural language toolkit, usada pra construir programas que trabalham com dados
#de linguagem natural (humana)
import nltk
#módulo para trabalhar com stopwords, que são palavras que podem ser filtradas
#do texto, como "the", "is", "are"
from nltk.corpus import stopwords
#funções que trabalham com operações envolvendo cadeias de palavras
import string
#biblioteca de alta performance contendo estruturas de dados e ferramentas de
#análise de dados
import pandas as pd

#scikit-learn: bibliotecas com funções para aprendizado de máquina no python
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report,confusion_matrix

def processaTexto(texto):
    #remove pontuação caractere a caractere
    nopunc = [char for char in texto if char not in string.punctuation]
    #junta os caracteres em palavras novamente
    nopunc = ''.join(nopunc)
    
    #nopunc.split() separa cada frase em palavras, retirando as que estão dentro de stopwords
    #word.lower() torna todas as letras minúsculas
    #essa linha remove as stopwords, retornando apenas as palavras relevantes para a análise
    cleanWords = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
        
    return cleanWords

#precisa disso na primeira vez
#nltk.download()

#lê o arquivo csv
messages = pd.read_csv('spam.csv', encoding='latin-1')

#remove colunas do dataframe do pandas (estrutura tabular bidimensional com eixos 
#rotulados)
#remove coluna (axis = 1), inplace=true faz a operação no próprio objeto, 
#sem retornar coisa alguma
messages.drop(['Unnamed: 2','Unnamed: 3','Unnamed: 4'], axis=1, inplace=True)

#renomeia colunas
messages = messages.rename(columns={'v1': 'tipo','v2': 'mensagem'})

#imprime tudo
#print(messages.to_string())

#imprimir primeiras linhas
#print(messages.head().to_string())

#imprime primeira linha
#print(messages.iloc[0])

#imprime segunda coluna
#print(messages.iloc[:,1])

#selecionando mensagens com SPAM
#messages.set_index("tipo", inplace=True)
#print(messages.loc['spam'])

#gera estatísticas descritivas sobre o dataset analisado
#exibe count (total de mensagens ham), quantas são únicas (ou seja, tem valores repetidos)
#top (a mensagem que mais se repete) e freq (quantas vezes a mensagem top repete)
#print(messages.groupby('tipo').describe().iloc[0])
#print(messages.groupby('tipo').describe().iloc[1])

#aproximadamente 13,4% é spam e temos muitas mensagens duplicadas

#aplica a função len em cada mensagem de texto analisada
messages['length'] = messages['mensagem'].apply(len)

#imprime a coluna nova que foi criada no dataframe, mostrando o tamanho de cada
#mensagem de texto
#print(messages.iloc[:,2])

#desenha um gráfico do número de mensagens pelo tamanho
#podemos ver pela figura que as mensagens não spam (ham) possuem mensagens com menos de
#200 caracteres (em média 100 para ser preciso), já as mensagens SPAM tendem a ser
#maiores do que 100, oscilando entre 130 e 140
#messages.hist(column='length',by='tipo',bins=70, figsize=(15,6))

#print(messages.iloc[:,1])

#messages['mensagem'].apply(processaTexto)

#mostrar as stopwords (palavras muito comuns que motores de busca tendem a ignorar.
#elas tomam espaço na base de dados ou tempo precioso de processamento)
#print(stopwords.words('english'))

#print(messages.iloc[:,1].head())

#divide os conjuntos em treinamento e teste
#msg_train e msg_test são os conjuntos de treinamento e teste da base de dados de mensagens
#class_train e class_test são, respectivamente, os rótulos dos sets de teste e treinamento 
#por parâmetro são passados os conjuntos de mensagens e o conjunto de rótulos (tipo), bem como o tamanho da base de teste
msg_train, msg_test, class_train, class_test = train_test_split(messages['mensagem'], messages['tipo'], test_size=0.1)

#pipeline de transformação com estimador. sequencialmente aplica uma lista de transformações
#a primeira converte documentos de texto em uma matriz com contagem de tokens, ou seja, conta a ocorrência de cada palavra no vocabulário
#a segunda normaliza a contagem (term frequency times inverse document frequency)
#este escala para baixo o impacto de tokens que ocorrem frequentemente e que sejam
#empiricamente menos informativos do que features que ocorrem em uma pequena fração do treinamento
#a última linha treina esses vetores no classificador naive bayes
pipeline = Pipeline([
    ('bow',CountVectorizer(analyzer=processaTexto)), # converts strings to integer counts
    ('tfidf',TfidfTransformer()), # converts integer counts to weighted TF-IDF scores
    ('classifier',MultinomialNB()) # train on TF-IDF vectors with Naive Bayes classifier
])
 
#testa um exemplo
#msg_test.iloc[0] = "Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's"

#treina o modelo
pipeline.fit(msg_train,class_train)

#testa o modelo
predictions = pipeline.predict(msg_test)

#resultado do teste de exemplo acima
#print(predictions[0])

#mostra os resultados
#print(classification_report(class_test,predictions))