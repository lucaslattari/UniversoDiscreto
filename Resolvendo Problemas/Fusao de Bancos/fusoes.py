# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 22:39:12 2018

@author: Lucas
"""
import os
from tqdm import tqdm, trange

def computeBankFusionProblem(totalOfBanks, totalOfOperations, listOfOperations, listOf1stBank, listOf2ndBank, outputString):
    numeroDeBancos = int(totalOfBanks)
    numeroDeConsultas = int(totalOfOperations)

    codigoDeFusoes = [0] * 100000
    contadorDeFusoes = 1
    stringDeSaida = ""

    for i in tqdm(range(1, numeroDeConsultas + 1)):
        tipoDeOperacao = listOfOperations[i - 1]
        idBanco1 = int(listOf1stBank[i - 1])
        idBanco2 = int(listOf2ndBank[i - 1])
        
        if(tipoDeOperacao == 'F' or tipoDeOperacao == 'f'):
            #se os dois bancos não fizeram fusão ainda
            if(codigoDeFusoes[idBanco1] == 0 and codigoDeFusoes[idBanco2] == 0):
                codigoDeFusoes[idBanco1] = contadorDeFusoes
                codigoDeFusoes[idBanco2] = contadorDeFusoes
                contadorDeFusoes += 1
            #se um dos bancos fizeram fusão
            elif(codigoDeFusoes[idBanco1] == 0):
                codigoDeFusoes[idBanco1] = codigoDeFusoes[idBanco2]
            elif(codigoDeFusoes[idBanco2] == 0):
                codigoDeFusoes[idBanco2] = codigoDeFusoes[idBanco1]
            #se os dois bancos já fizeram fusão com códigos distintos
            elif(codigoDeFusoes[idBanco1] != 0 and codigoDeFusoes[idBanco2] != 0):
                #item comprehension que substitui os valores de fusões do banco 1 para o banco 2
                codigoDeFusoes = [x if x != codigoDeFusoes[idBanco1] else codigoDeFusoes[idBanco2] for x in codigoDeFusoes]
        elif(tipoDeOperacao == 'c' or tipoDeOperacao == 'C'):
            if(codigoDeFusoes[idBanco1] == 0 or codigoDeFusoes[idBanco2] == 0):
                stringDeSaida += "N"
            elif(codigoDeFusoes[idBanco1] == codigoDeFusoes[idBanco2]):
                stringDeSaida += "S"
            else:
                stringDeSaida += "N"

    if(stringDeSaida == outputString):
        return True
    else:
        return False

def createListOfInputAndOutputFiles():
    listOfFilesInput = []
    listOfFilesOutput = []

    for testDir in os.listdir("2010f2p1_fusoes"):
        for filename in os.listdir("2010f2p1_fusoes\\" + testDir):
            
            if "in" in filename:
                listOfFilesInput.append("2010f2p1_fusoes\\" + testDir + "\\" + filename)
            elif "out" in filename:
                listOfFilesOutput.append("2010f2p1_fusoes\\" + testDir + "\\" + filename)
               
    return listOfFilesInput, listOfFilesOutput

def parseBankFusionProblem(fileInput, fileOutput):
    iterations = 0
    totalOfBanks = 0
    totalOfOperations = 0

    listOfOperations = []
    listOf1stBank = []
    listOf2ndBank = []
    
    with open(fileInput) as fin:
        for line in fin:
            if(iterations == 0):
                totalOfBanks, totalOfOperations = [c for c in line.split() if c is not " "]
            else:
                op, bank1, bank2 = [c for c in line.split() if c is not " "]
                listOfOperations.append(op)
                listOf1stBank.append(bank1)
                listOf2ndBank.append(bank2)

            iterations += 1
            
    outputString = ""
    with open(fileOutput) as fin:
        for line in fin:
            outputString += line.rstrip("\n")

    return totalOfBanks, totalOfOperations, listOfOperations, listOf1stBank, listOf2ndBank, outputString

if __name__ == "__main__":
    listOfFilesInput, listOfFilesOutput = createListOfInputAndOutputFiles()
    
    for fileInput, fileOutput in zip(listOfFilesInput, listOfFilesOutput):
        totalOfBanks, totalOfOperations, listOfOperations, listOf1stBank, listOf2ndBank, outputString = parseBankFusionProblem(fileInput, fileOutput)
        checkError = computeBankFusionProblem(totalOfBanks, totalOfOperations, listOfOperations, listOf1stBank, listOf2ndBank, outputString)
        if(checkError == False):
            print("Encontrou um erro no arquivo " + fileInput)
            break
        
        
        
        
        