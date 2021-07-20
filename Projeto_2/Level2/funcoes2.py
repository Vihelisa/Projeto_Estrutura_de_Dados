#Importações:
import os
from time import sleep
from Itens import utilizando, itens


#Variáveis:
PATH = "Arquivos"
NOME_ARQ = "nome.txt"
VIDA_ARQ = "vida.txt"
VIDA_BOSS_ARQ = 'vida_boss.txt'
NOMES_ALEATORIOS2 = ["Gabriel", "Isabela", "João"]
MOCHILA_ARQ = "mochila.txt"
CINTO_ARQ = "cinto.txt"




def guardando_nome(nome):
    caminho = os.path.join(PATH, NOME_ARQ) 
    with open(caminho, "w") as arq:
        arq.write(str(nome))
    
    with open(caminho, 'a') as arqui:
        for nomes in NOMES_ALEATORIOS2:
            arqui.write(str(nomes) + "\n")


def lendo_nome_arq():
    lista_nomes = []
    caminho = os.path.join(PATH, NOME_ARQ)
    with open(caminho, "r") as arq:
        for linha in arq:
            lista_nomes.append(linha)
    return lista_nomes


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


def reescrevendo_itens_cinto(lista_itens_novos):
    caminho = os.path.join(PATH, CINTO_ARQ) 
    with open(caminho, 'w') as arq:
        for item in lista_itens_novos:
            arq.write(str(item) + "\n")


def reescrevendo_itens_mochila(lista_itens_novos):
    caminho = os.path.join(PATH, MOCHILA_ARQ) 
    with open(caminho, 'w') as arq:
        for item in lista_itens_novos:
            arq.write(str(item))


def mostrando_atributos():
    lista_itens_cinto = lendo_cinto_arq()
    quant_cinto = len(lista_itens_cinto)
    lista_itens_mochi = lendo_mochila_arq()
    if len(lista_itens_mochi) == 0:
        last_item = None
    else:
        last_item = lista_itens_mochi[-1]
    
    print(f'\nQuantidade de ítes no cinto: {quant_cinto}\nUltimo ítem da mochila: {last_item}\n{mostrando_vida()}')
    

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
        guardar_1_item_cinto(item)
    if resp == 's':
        guardar_1_item_mochila(item)


def deseja_guardar(item):
    print('''           
                Deseja guardar este ítem?
    
                a- Sim
                s- Não
    ''')
    resp = input('Responda e aperte "enter" para continuar\n')
    if resp == 'a':
        escolha_onde_guardar(item)
    if resp == 's':
        print(F'{item} foi descartado')  


def guardar_1_item_cinto(item):
    num_max_item = 4
    caminho = os.path.join(PATH, CINTO_ARQ) 
    lista_itens_cinto = lendo_cinto_arq()
    if len(lista_itens_cinto)>= num_max_item:
        print(f"Cinto cheio, coloque {item} na mochila ou remova um outro ítem")
        guardar_mochila_ou_remover(item)
    else:
        with open(caminho, 'a') as arq:
            arq.write(str(item) + "\n")
        print("Item adicionado ao cinto")  


def guardar_1_item_mochila(item):
    caminho = os.path.join(PATH, MOCHILA_ARQ) 
    with open(caminho, 'a') as arq:
        arq.write(str(item) + "\n")
    print("Item adicionado a mochila")


def guardar_mochila_ou_remover(item):
    print(f'''           
                Onde deseja fazer?
    
                a- Guardar {item} na mochila
                s- Remover um item da mochila para guardar {item}
    ''')
    resp = input('Responda e aperte "enter" para continuar\n')
    if resp == 'a':
        guardar_1_item_mochila(item)
        print("Item adicionado a mochila")
    if resp == 's':
        remover_item_cinto()
        guardar_1_item_cinto(item)


def remover_item_cinto():
    while True:
        lista_itens_cinto = lendo_cinto_arq()
        for item in lista_itens_cinto:
            print(item)
        remover = input("Escreva, da forma mostrada na tela, o item que deseja remover:\n")
        lista_itens_cinto.remove(remover)
        print('''
                    Deseja remover mais algum item?

                    a- Sim
                    s- Não
        ''')
        reescrevendo_itens_cinto(lista_itens_cinto)
        resp = input('Responda e aperte "enter" para continuar')
        if resp == 's':
            break


def usar_item():
    print('''
                    Deseja utilizar algum item?

                    a- Sim
                    s- Não
        ''')
    resp = input('Responda e aperte "enter" para continuar\n')
    return resp


def cinto_ou_mochila():
    print('''           
                Onde deseja acessar?
    
                a- Cinto
                s- Mochila
    ''')
    resp = input('Responda e aperte "enter" para continuar\n')
    if resp == 'a':
        cinto = 'cinto'
        return cinto
    if resp == 's':
        mochila = 'mochila'
        return mochila


def pegar_item_cinto():
    lista_itens_cinto = lendo_cinto_arq()
    for item in lista_itens_cinto:
        print(item)
    escolher = input("Escreva, da forma mostrada na tela, o item que deseja escolher:\n")
    if 'Cura-1' in escolher:
        utilizando.usando_cura(escolher)
        lista_itens_cinto.remove('Cura-1')
        reescrevendo_itens_cinto(lista_itens_cinto)
    if 'Cura-2' in escolher:
        utilizando.usando_cura(escolher)
        lista_itens_cinto.remove('Cura-2')
        reescrevendo_itens_cinto(lista_itens_cinto)
    if 'Chave 2' in escolher:
        lista_itens_cinto.remove('Chave 2')
        reescrevendo_itens_cinto(lista_itens_cinto)
    if 'Carta' in escolher:
        print(itens.CARTA)
    return escolher


def pegar_item_mochila():
    lista_itens_mochila = lendo_mochila_arq()
    for item in lista_itens_mochila[::-1]:
        print(item)
    escolher = input("Escreva, da forma mostrada na tela, o item que deseja escolher:\n")
    for coisa in lista_itens_mochila[::-1]:
        if coisa in escolher:
            if 'Cura-1' in escolher:
                utilizando.usando_cura(escolher)
                lista_itens_mochila.remove('Cura-1\n')
                reescrevendo_itens_mochila(lista_itens_mochila)
            if 'Cura-2' in escolher:
                utilizando.usando_cura(escolher)
                lista_itens_mochila.remove('Cura-2\n')
                reescrevendo_itens_mochila(lista_itens_mochila)
            if 'Chave 2' in escolher:
                lista_itens_mochila.remove('Chave 2\n')
                reescrevendo_itens_mochila(lista_itens_mochila)
            if 'Chave 8' in escolher:
                lista_itens_mochila.remove('Chave 8\n')
                reescrevendo_itens_mochila(lista_itens_mochila)
            if 'Carta' in escolher:
                print(itens.CARTA)
            if 'Tradução da Carta' in escolher:
                print(itens.TRADU_CARTA)
        else:
            lista_itens_mochila.remove(coisa)
    return escolher


def escolher_item():
    resp = usar_item()
    if resp == 'a':
        lugar = cinto_ou_mochila()
        if lugar == 'cinto':
            escolha = pegar_item_cinto()
        if lugar == 'mochila':
            escolha = pegar_item_mochila()
    if resp == 's':
        escolha = None
    return escolha

