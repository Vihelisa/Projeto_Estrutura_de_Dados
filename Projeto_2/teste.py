import os

isa = ['i', 's', 'a', 'b', 'e', 'l', 'a']
lucy = ['l', 'u', 'c', 'y']

dano = 3
i = 0
l = 0

PATH = "Arquivos"
VIDA_BOSS_ARQ = 'vida_boss.txt'
VIDA_ARQ = "vida.txt"

caminho = os.path.join(PATH, VIDA_BOSS_ARQ)
num = 20
with open(caminho, 'w') as arq:
    while num > 0:
        arq.write(str('@\n'))
        #print(num)
        num = num -1

def lendo_vida_boss():
    lista_vida_boss = []
    caminho = os.path.join(PATH, VIDA_BOSS_ARQ)
    with open(caminho, "r") as arq:
        for linha in arq:
            lista_vida_boss.append(linha)
    return lista_vida_boss

def reescrevendo_vida_boss(lista, dano):
    caminho = os.path.join(PATH, VIDA_BOSS_ARQ)
    tam = len(lista) - dano
    while tam != len(lista):
        lista.remove('@\n')
        tam_atual = len(lista)
        if tam_atual == 0:
            break
    with open(caminho, 'w') as arq:
        for item in lista:
            arq.write(str(item))
    return tam_atual

def mostrando_vida():
    lista_pontos_vida = []
    caminho = os.path.join(PATH, VIDA_ARQ)
    with open(caminho, "r") as arq:
        for ponto in arq:
            #ponto = ponto.replace("\n", "")
            lista_pontos_vida.append(ponto)
    return lista_pontos_vida

def reescrevendo_vida(lista, dano):
    caminho = os.path.join(PATH, VIDA_ARQ)
    tam = len(lista) - dano
    while tam != len(lista):
        lista.remove('%\n')
        tam_atual = len(lista)
        if tam_atual == 0:
            break
    with open(caminho, 'w') as arq:
        for item in lista:
            arq.write(str(item)+ '\n')
    return tam_atual
        


while True:
    print(isa[i])
    resp = input("Digite as letras sem espaço \n")
    if resp == isa[i]:
        lista_vida_boss = lendo_vida_boss()
        lista_vida = mostrando_vida()
        tam_atual = reescrevendo_vida_boss(lista_vida_boss, dano)
        len_vida = {len(lista_vida)}
        len_boss = {len(lista_vida_boss)}
        print(f'''
                    =========================================================
                    =                                                       =
                    =       Você:{len_vida}                      Monstro:{len_boss}      =
                    =                                                       =
                    =========================================================
        ''')
        print(tam_atual)
        i = i+1
        if tam_atual == 0:
            print('MORTO')
            break
        if i == len(isa)-1:
            i=0
            print('Voltando')
    else:
        i = i+1
        print('ERROU')
        dano_boss = 2
        lista_vida = mostrando_vida()
        lista_vida_boss = lendo_vida_boss()
        tam_atual = reescrevendo_vida(lista_vida, dano_boss)
        len_vida = {len(lista_vida)}
        len_boss = {len(lista_vida_boss)}
        print(f'''
                    =========================================================
                    =                                                       =
                    =       Você:{len_vida}                      Monstro:{len_boss}      =
                    =                                                       =
                    =========================================================
        ''')
        #print(tam_atual)
        if len(lista_vida) == 0:
            print('MORTO')
            break
        if i == len(isa)-1:
            i=0
            print('Voltando')
        



'''
print(isa[i])
    resp = input("Digite as letras sem espaço \n")
    print(lucy[l])
    respp = input("Digite as letras sem espaço \n")
    if resp == isa[i]:
        #dano no monstro
        pass
    if respp == lucy[l]:
        print("ACERTOU")
        break
        
    else:
        print("ERROU")
        i = i+1
        j = j+1
'''