import os

#Variáveis:
PATH = "Arquivos"
NOME_ARQ = "nome.txt"
VIDA_ARQ = "vida.txt"
NOMES_ALEATORIOS1 = ["Vitoria", "Rafael", "Jessica"]

def guardando_nome(nome):
    caminho = os.path.join(PATH, NOME_ARQ) 
    with open(caminho, "a") as arq:
        arq.write(str(nome) + "\n")
        for nomes in NOMES_ALEATORIOS1:
            arq.write(str(nomes) + "\n")

def lendo_nome_arq():
    lista_nomes = []
    caminho = os.path.join(PATH, NOME_ARQ)
    with open(caminho, "r") as arq:
        for linha in arq:
            lista_nomes.append(linha)
    return lista_nomes

def mostrando_vida():
    lista_pontos_vida = []
    caminho = os.path.join(PATH, VIDA_ARQ)
    with open(caminho, "r") as arq:
        for ponto in arq:
            ponto = ponto.replace("\n", "")
            lista_pontos_vida.append(ponto)
    return lista_pontos_vida

def danos_vida(valor_dano):
    lista_pontos_vida = []
    caminho = os.path.join(PATH, VIDA_ARQ)
    with open(caminho, "r") as arq:
        lista_pontos_vida = []
        for ponto in arq:
            ponto = ponto.replace("\n", "")
            lista_pontos_vida.append(ponto)
    len_final = len(lista_pontos_vida) - valor_dano
    while True:
        lista_pontos_vida.remove('.')
        if len(lista_pontos_vida) == len_final:
            break
    return lista_pontos_vida

def reescrevendo_vida(lista_vida):
    caminho = os.path.join(PATH, VIDA_ARQ)
    with open(caminho, "w") as arq:
        for ponto in lista_vida:
            arq.write(str(ponto) + "\n")
        