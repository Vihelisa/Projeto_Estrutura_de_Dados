from time import sleep

from Level_1.historia.hist1 import *
from Level_1.historia.hist_nome import *

def hist1():
    i = 0
    while True:
        print(historia_parte1[i])
        troca = input('Tecle "enter" para avançar')
        sleep(1)
        i=i+1
        if historia_parte1[i] == historia_parte1[-1]:
            print(historia_parte1[-1])
            break


def pensando():
    troca = input('Tecle "enter" para avançar')
    print(pensamento)
    sleep(1)
    print(decisao)
    resp = input('Tecle "enter" para avançar\n').lower()
    if resp == "a":
        print("""           Que lugar é esse?""")
    elif resp == "w":
        print("""           Onde eu estou?""")
    elif resp == "s":
        print("""           O que aconteceu comigo?""")
    elif resp == "d":
        print("""           Como eu vim parar aqui?""")

def dizendo_nome_primeira_vez():
    print(parag10)
    input('Tecle "enter" para avançar')
    nome = quem_e_voce()
    lista_n = lista_nomes(nome)
    pensa = pensando_no_nome(lista_n)
    sleep(1)
    print(pensa)
    