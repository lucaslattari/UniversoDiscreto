from os import listdir

def geraArquivoDeGabarito(pasta):
    arquivos = [arq for arq in listdir(pasta)]
    novalista = []
    
    for arq in arquivos:
        novalista.append(pasta + arq + "\n")
        
    return novalista

if __name__ == "__main__":
    arq = open('gabarito.txt', 'w')
    
    lista1 = geraArquivoDeGabarito("gabarito/1/")
    lista2 = geraArquivoDeGabarito("gabarito/2/")
    lista3 = geraArquivoDeGabarito("gabarito/3/")
    lista4 = geraArquivoDeGabarito("gabarito/4/")
    
    lista = lista1 + lista2 + lista3 + lista4
    
    arq.writelines(lista)        
    arq.close()    