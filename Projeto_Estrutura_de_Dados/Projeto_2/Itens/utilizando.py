from Itens import itens
from Level1 import funcoes1

def cura1():
    lista_pontos_vida = funcoes1.mostrando_vida()
    print(len(lista_pontos_vida))
    if len(lista_pontos_vida) <= 10:
        lista_pontos_vida.append('%')
        funcoes1.reescrevendo_vida(lista_pontos_vida)
        print('''
                    =====================================
                    =                                   =
                    =   Você ganhou 1 ponto de vida     =
                    =                                   =
                    =====================================
        ''')
    else:
        print('''
                    =====================================
                    =                                   =
                    =  Você não precisa curar sua vida  =
                    =                                   =
                    =====================================
        ''')


def cura2():
    lista_pontos_vida = funcoes1.mostrando_vida()
    if len(lista_pontos_vida) < 10:
        lista_pontos_vida.append('%')
        lista_pontos_vida.append('%')
        funcoes1.reescrevendo_vida(lista_pontos_vida)
        print('''
                    =====================================
                    =                                   =
                    =   Você ganhou 2 ponto de vida     =
                    =                                   =
                    =====================================
        ''')
    else:
        print('''
                    =====================================
                    =                                   =
                    =  Você não precisa curar sua vida  =
                    =                                   =
                    =====================================
        ''')


