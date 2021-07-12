import os
from typing import ChainMap
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

def lendo_mochila_arq(caminho):
    lista_itens_mochila = [] 
    with open(caminho, 'r') as arq:
        for linha in arq:
            linha.replace("\n", "")
            lista_itens_mochila.append(linha)
    return lista_itens_mochila

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
        lista_pontos_vida.remove("%")
        if len(lista_pontos_vida) == len_final:
            break
    return lista_pontos_vida

def reescrevendo_vida(lista_vida):
    caminho = os.path.join(PATH, VIDA_ARQ)
    with open(caminho, "w") as arq:
        for ponto in lista_vida:
            arq.write(str(ponto) + "\n")

def reescrevendo_itens_cinto(lista_itens_novos):
    caminho = os.path.join(PATH, CINTO_ARQ) 
    with open(caminho, 'w') as arq:
        for item in lista_itens_novos:
            arq.write(str(item) + "\n")

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
    if resp == 's':
        funcoes1.guardar_1_item_mochila(item)
        

def guardar_mochila_ou_remover(item):
    print(f'''           
                Onde deseja fazer?
    
                a- Guardar {item} na mochila
                s- Remover um item do cinto para guardas {item}
    ''')
    resp = input('Responda e aperte "enter" para continuar\n')
    if resp == 'a':
        funcoes1.guardar_1_item_mochila(item)
        print("Item adicionado a mochila")
    if resp == 's':
        remover_item_cinto()
        guardar_1_item_cinto(item)


def guardar_cinto_ou_remover(item):
    print(f'''           
                Onde deseja fazer?
    
                a- Guardar {item} na cinto
                s- Remover um item do mochila para guardas {item}
    ''')
    resp = input('Responda e aperte "enter" para continuar\n')
    if resp == 'a':
        funcoes1.guardar_1_item_mochila(item)
        print("Item adicionado a mochila")
    if resp == 's':
        remover_item_cinto()
        

def guardar_1_item_cinto(item):
    num_max_item = 4
    caminho = os.path.join(PATH, CINTO_ARQ) 
    lista_itens_cinto = lendo_cinto_arq(caminho)
    if len(lista_itens_cinto)>= num_max_item:
        print(f"Cinto cheio, coloque {item} na mochila ou remova um outro ítem")
        guardar_mochila_ou_remover(item)
    else:
        with open(caminho, 'a') as arq:
            arq.write(str(item) + "\n")


def guardar_1_item_mochila(item):
    num_max_item = 10
    caminho = os.path.join(PATH, MOCHILA_ARQ) 
    lista_itens_cinto = lendo_mochila_arq(caminho)
    if len(lista_itens_cinto)>= num_max_item:
        print(f"Cinto cheio, coloque {item} na mochila ou remova um outro ítem")
    else:
        with open(caminho, 'a') as arq:
            arq.write(str(item) + "\n")

def remover_item_cinto():
    while True:
        lista_itens_cinto = lendo_cinto_arq()
        print(f'''
                    Itens da lista:

                    a- {lista_itens_cinto[0]}
                    s- {lista_itens_cinto[1]}
                    w- {lista_itens_cinto[2]}
                    d- {lista_itens_cinto[3]}

                    Qual item deseja remover?
        ''')
        item_remover = input('Responda e aperte "enter" para remover o item')
        if item_remover == 'a':
            lista_itens_cinto.remove(lista_itens_cinto[0])
        if item_remover == 's':
            lista_itens_cinto.remove(lista_itens_cinto[1])
        if item_remover == 'w':
            lista_itens_cinto.remove(lista_itens_cinto[2])
        if item_remover == 'd':
            lista_itens_cinto.remove(lista_itens_cinto[3])
        print('''
                    Deseja remover mais algum item?

                    a- Sim
                    s- Não
        ''')
        reescrevendo_itens_cinto(lista_itens_cinto)
        resp = input('Responda e aperte "enter" para continuar')
        if resp == 's':
            break

