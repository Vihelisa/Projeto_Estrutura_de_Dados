from Level1 import funcoes1

FACA = str('''
                =====================================
                =                 .                 =
                =                /.\    /           =
                =               /  .\    /          =
                =               |  ..\    /         =
                =               3   ..|             =
                =               3   ..|             =
                =               3   ..|             =
                =               |   ..|             =
                =             ===========           =
                =             ===========           =
                =               |    |              =
                =               |    |              =
                =               |    |              =
                =               ======              =
                =====================================
                =          FACA -> 1 DE DANO        =
                =====================================
''')


POCAO1 = str('''
                =====================================
                =                                   =
                =               _____               =
                =               |   |               =
                =              /     \              =
                =             /.......\             =
                =            /:::::::::\            =
                =           =============           =
                =====================================
                =      CURA 1 -> CURA 1 DE VIDA     = 
                =====================================   
''')


POCAO2 = str('''
                =====================================
                =                ____               =
                =                |  |               =
                =                |  |               =
                =               /    \              =
                =              /      \             =
                =             |........|            =
                =             |::::::::|            =
                =             |::::::::|            =
                =             ==========            =
                =====================================
                =     CURA 2 -> CURA 2 DE VIDA      =
                =====================================
''')

ARMA1 = str('''
                =====================================
                =                                   =
                =       __##________________        =
                =       |,,,,,,,,,,,,,,,,,,|        =
                =       |__________________|        =
                =       |:::    /_))_||             =
                =        \::   /                    =
                =        /::  /                     =
                =       |:::_/                      =
                =====================================
                =         GLOCK -> 3 DE DANO        =
                =====================================
''')

def achando_faca():
    faca = 'Faca'
    print('''           Você achou uma Faca''')
    print(FACA)
    funcoes1.escolha_onde_guardar(faca)

def achando_cura_1():
    cura1 = 'Cura-1'
    print('''           Você achou uma Cura-1''')
    print(POCAO1)
    funcoes1.escolha_onde_guardar(cura1)

def achando_cura_2():
    cura2 = 'Cura-2'
    print('''           Você achou uma Cura-2''')
    print(POCAO2)
    funcoes1.escolha_onde_guardar(cura2)

def achando_arma_1():
    arma_1 = 'Glock G42'
    print('''           Você achou uma Glock G42''')
    print(ARMA1)
    funcoes1.escolha_onde_guardar(arma_1)
