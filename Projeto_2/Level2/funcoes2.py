#Importações:
import os
from time import sleep


#Variáveis:
PATH = "Arquivos"
NOME_ARQ = "nome.txt"
VIDA_ARQ = "vida.txt"
VIDA_BOSS_ARQ = 'vida_boss.txt'
NOMES_ALEATORIOS1 = ["Vitoria", "Rafael", "Jessica"]
MOCHILA_ARQ = "mochila.txt"
CINTO_ARQ = "cinto.txt"



def lendo_mochila_arq():
    caminho = os.path.join(PATH, MOCHILA_ARQ)
    lista_itens_mochila = [] 
    with open(caminho, 'r') as arq:
        for linha in arq:
            linha.replace("\n", "")
            lista_itens_mochila.append(linha)
    return lista_itens_mochila


def lendo_cinto_arq():
    lista_itens_cinto = [] 
    caminho = os.path.join(PATH, CINTO_ARQ)
    with open(caminho, 'r') as arq:
        for linha in arq:
            linha = linha.replace("\n", "")
            lista_itens_cinto.append(linha)
    return lista_itens_cinto


def mostrando_vida():
    lista_pontos_vida = []
    caminho = os.path.join(PATH, VIDA_ARQ)
    with open(caminho, "r") as arq:
        for ponto in arq:
            ponto = ponto.replace("\n", "")
            lista_pontos_vida.append(ponto)
    return lista_pontos_vida


def mostrando_atributos():
    lista_itens_cinto = lendo_cinto_arq()
    quant_cinto = len(lista_itens_cinto)
    lista_itens_mochi = lendo_mochila_arq()
    if len(lista_itens_mochi) == 0:
        last_item = None
    else:
        last_item = lista_itens_mochi[-1]
    
    print(f'\nQuantidade de ítes no cinto: {quant_cinto}\nUltimo ítem da mochila: {last_item}\n{mostrando_vida()}')
    input('Tecle "enter" para avançar')