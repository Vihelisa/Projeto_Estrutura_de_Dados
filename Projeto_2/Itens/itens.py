from time import sleep
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
            | Doutor: Joseph Smith                      Data: 23/05/1961        |
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
            |choque insulínico a acalmou e fez parar de falar do suposto filho  |
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

COFRE = str('''
            =============================================
            =                                           =
            =       _____________________________       =
            =       |                           |       =
            =       |     _____________________ |       =
            =       |     |       ___________ | |       =
            =       |     |       | * * * * | | |       =
            =       |     |       |  . . .  | | |       =
            =       |     |       |  : : :  | | |       =
            =       |     |       |_________| | |       =
            =       |     |                   | |       =
            =       |     |___________________| |       =
            =       |                           |       =
            =       |___________________________|       =
            =============================================
            =     COFRE -> Contem senha de 4 digitos    =
            =============================================
''')

CHAVE_2 = str('''
            =====================================
            =              ______               =
            =             /  __  \              =
            =            |  / /   |             =
            =            |   /__  |             =
            =             \______/              =
            =               |  |                =
            =               |  |                =
            =               |  |                =
            =               |  |                =
            =               |  |__              =
            =               |  ___|             =
            =               |  |___             =
            =               |_____|             =
            =====================================
            = Chave de metal cravado o numero 2 =
            =====================================           
''')

CHAVE_8 = str('''
            =====================================
            =            ____WW____             =
            =           /::::/\::::\            =
            =          /::::/  \::::\           =
            =         /::::/    \::::\          =
            =        |::::/ .... \ :::|         =
            =         \__|  :..:  |__/          =
            =            |  :..:  |             =
            =             \______/              =
            =               |  |                =
            =               |  |                =
            =               |  |                =
            =               |  |                =
            =               |  |__              =
            =               |  ___|             =
            =               |  |___             =
            =               |_____|             =
            =====================================
            = Chave de metal cravado o numero 8 =
            =====================================           
''')

CHAVE_5 = str('''
            =====================================
            =            __________             =
            =           /::::/\::::\            =
            =        /::::/ /  \ \::::\         =
            =       /::::/        \::::\        =
            =           |   =====  |            =
            =           |   |___   |            =
            =            \   ___| /             =
            =             \______/              =
            =               |  |                =
            =               |  |                =
            =               |  |                =
            =               |  |                =
            =               |  |__              =
            =               |  ___|             =
            =               |  |___             =
            =               |_____|             =
            =====================================
            = Chave de metal cravado o numero 5 =
            =====================================           
''')

RELATORIO = str('''
            _____________________________________________________________________
            |                                                                   |
            | Doutor: Joseph Smith                                              |
            | Data: 20/07/1962                                                  |
            | Local: Hospital de Reabilitação Psiquiatra Colônia                |
            | Endereço: Barbacoa,  Montes Uivantes - Brasil                     |
            |                                                                   |
            |                                                                   |
            | Relatório do mês:                                                 |
            |  Não sei o que pode estar acontecendo, já faz mais de um ano que  |
            |começamos os tratamentos intensivos com métodos vindos da europa e |
            |dos USA, mas há algo de errado. Algumas cobaias não resistiram, por|
            |isso teremos que recrutar mais delas, mas algumas estão mudando (o |
            |que me faz pensar que estamos tendo progresso). No entanto algumas |
            |das mudanças estão sendo um pouco assustadoras até pra mim, como   |
            |sorrisos constantes e bem abertos (lembrando que não são das 15 co-|
            |baias que fizemos a cirurgia de Fake Smile) ou olhos esbugalhados e|
            |fixos com pupilas dilatadas o tempo todo (tirando 20 cobaias desse |
            |mês que passaram por uma lobotomia). Por fim sei que estamos pro-  |
            |gredindo e isso é muito bom.                                       |
            |___________________________________________________________________|
''')


CARTA = str('''
            _____________________________________________________
            |                                                   |
            |   30-!4%[031-7068-3-4[8%4-32780-4@01-4-100-!042*  |
            |   30-^48-93%73^28-4-3223-!0[4%*                   |
            |   30-3274\4-9%8^74-94%4-73%-+30-^8+3-^82-!1\%82   |
            |   63-&12154-@04^7154*                             |
            |   ^853-+3-982-4@01-?9%4-30-^48-73%-4-5}4^53-63    |
            |   +064%-8-+0^68-3-41^64-630-4-3!4-8-+30-!0[4%-^4  |
            |   285136463*                                      |
            |   "30-9%35128-241%-64@01"*                        |
            |___________________________________________________|
''')

TRADU_CARTA = str('''
            _____________________________________________
            |                                           |
            |   3 = E   0 = U   4 = A   8 = O   ! = L   |
            |   2 = S   7 = T   5 = C   @ = Q   + = M   |
            |   ? = ,   6 = D   * = .   ^ = N   1 = I   |
            |   - = ESPAÇO      % = R   [ = G   \ = V   |
            |   9 = P   & = F   } = H                   |
            |___________________________________________|
''')


def achando_faca():
    faca = 'Faca'
    print('''           Você achou uma Faca''')
    print(FACA)
    funcoes1.deseja_guardar(faca)


def achando_cura_1():
    cura1 = 'Cura-1'
    print('''           Você achou uma Cura-1''')
    print(POCAO1)
    funcoes1.deseja_guardar(cura1)


def achando_cura_2():
    cura2 = 'Cura-2'
    print('''           Você achou uma Cura-2''')
    print(POCAO2)
    funcoes1.deseja_guardar(cura2)


def achando_arma_1():
    arma_1 = 'Glock G42'
    print('''           Você achou uma Glock G42''')
    print(ARMA1)
    funcoes1.deseja_guardar(arma_1)


def achando_relatorio():
    relatorio = 'Relatorio 1'
    print(RELATORIO)
    funcoes1.deseja_guardar(relatorio)


def achando_doc_5152():
    doc = 'Documento cobaia 5152'
    print(DOCUMENTO_COB_5152)
    #funcoes1.deseja_guardar(doc)


def achando_chave2():
    chave = 'Chave 2'
    print(CHAVE_2)
    funcoes1.deseja_guardar(chave)


def achando_chave8():
    chave = 'Chave 8'
    print(CHAVE_8)
    funcoes1.deseja_guardar(chave)


def achando_cofre():
    print(COFRE)
    print(funcoes1.mostrando_atributos())
    input('Tecle "enter" para avançar')
    while True:
        print('''
                    QUAL A SENHA DO COFRE??

                    s- para sair das tentativas
        ''')
        resp = input('Responda e tecle "enter" para avançar\n')
        if resp == '5152':
            achando_arma_1()
            input('Tecle "enter" para avançar')
            achando_chave2()
            input('Tecle "enter" para avançar')
            achando_relatorio()
            break
        elif resp == 's':
            break
        else: 
            print('Senha incorreta!! tente novamente.')
