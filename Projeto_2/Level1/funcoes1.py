import os
from Level1 import funcoes1

#Variáveis:
PATH = "Arquivos"
NOME_ARQ = "nome.txt"
VIDA_ARQ = "vida.txt"
NOMES_ALEATORIOS1 = ["Vitoria", "Rafael", "Jessica"]
MOCHILA_ARQ = "mochila.txt"
CINTO_ARQ = "cinto.txt"
CURA_MAX_LEVEL = 10

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

def lendo_cinto_arq(caminho):
    lista_itens_cinto = [] 
    with open(caminho, 'r') as arq:
        for linha in arq:
            linha.replace("\n", "")
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

def movimentacao():
    lista_movimento = ['_','_','_','_','_','_','_','_','_','&']
    print(lista_movimento)
    paco = input('Aperte "enter" para andar')
    while '&' not in lista_movimento[0]:
        lista_movimento.append('_')
        lista_movimento.pop(0)
        print(lista_movimento)
        paco = input('')


def escolha_onde_guardar(item):
    print('''           
                Onde deseja guardar?
    
                a- Cinto
                s- Mochila
    ''')
    resp = input('Responda e aperte "enter" para continuar\n')
    if resp == 'a':
        funcoes1.guardar_1_item_cinto(item)


def guardar_1_item_cinto(item):
    num_max_item = 4
    caminho = os.path.join(PATH, CINTO_ARQ) 
    lista_itens_cinto = lendo_cinto_arq(caminho)
    if len(lista_itens_cinto)>= num_max_item:
        print(f"Cinto cheio, coloque {item} na mochila ou remova um outro ítem")
    else:
        with open(caminho, 'a') as arq:
            arq.write(str(item) + "\n")
