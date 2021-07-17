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

DOCUMENTO_COB_5152 = str('''
            _____________________________________________________________________
            |                                                                   |
            | Doutor: Joseph Smith                      Data: 12/07/1961        |
            | Paciente: Cobaia 5152                     Quarto: 02              |
            | Local: Hospital de Reabilitação Psiquiatra Colônia                |
            | Endereço: Barbacoa,  Montes Uivantes - Brasil                     |
            |                                                                   |
            |                                                                   |
            | Relatório do paciente:                                            |
            |   Já fazem 2 meses desde o início, aparentemente a cobaia 5152    |
            |está piorando conforme os testes para reverter sua situação mental.|
            |Foram feitos diversos tratamentos que a princípio não refletiram   |
            |nenhum efeito no paciente. Contudo posso afirmar que a terapia de  |
            |choque insul[inico a acalmou e fez parar de falar do suposto filho |
            |morto pelo marido. Nas próximas semanas irão ocorrer mais sessões, |
            |esperamos que ela volte a sua sanidade e finalmente lembre da ver- |
            |dade.                                                              |
            |                                                                   |
            |OBS: Em relação as histórias que a paciente conta, que fique bem   |
            |claro que o marido afirmou que o bebê nasceu morto. Ele é um homem |
            |de boa palavra e boa índole para a sociedade, então devemos acredi-|
            |tar nele.                                                          |
            |___________________________________________________________________|
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

def achando_doc_5152():
    doc = 'Documento cobaia 5152'
    print(DOCUMENTO_COB_5152)
    funcoes1.deseja_guardar(doc)
