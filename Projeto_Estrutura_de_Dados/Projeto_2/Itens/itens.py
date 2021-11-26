from time import sleep
from Level1 import funcoes1
from Level2 import funcoes2

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

ARMA2 = str('''
                =============================================================
                =                                                           =
                =          __________________________________________       =
                =         /_________|_______________________________|       =
                =        /__________|______|::::::::|_____________|         =
                =        |::: /_))_//      |________|                       =
                =        \:: /                                              =
                =        /:: \                                              =
                =        |::_/                                              =
                =============================================================
                =                  ESPINGARDA -> 5 DE DANO                  =
                =============================================================
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
            =             / ___  \              =
            =            |   __|  |             =
            =            |  |___  |             =
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

CHAVE_3 = str('''
            =====================================
            =              ______               =
            =             / ___  \              =
            =            |  |__   |             =
            =            |  |__   |             =
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

CHAVE_6 = str('''
            =====================================
            =            __________             =
            =           /::::/\::::\            =
            =        /::::/ /  \ \::::\         =
            =       /::::/        \::::\        =
            =           |   ====   |            =
            =           |   |___   |            =
            =            \  |___| /             =
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
            = Chave de metal cravado o numero 6 =
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

RELATORIO_2 = str('''
            _____________________________________________________________________
            |                                                                   |
            | Dr. Fernando Nogueira Nobrega                                     |
            | Data: 09/01/1963                                                  |
            | Local: Hospital de Reabilitação Psiquiatra Colônia                |
            | Endereço: Barbacoa,  Montes Uivantes - Brasil                     |
            |                                                                   |
            |                                                                   |
            |  Dr. Joseph ainda pede pacientes para realizar os seus tratamentos|
            |alternativos, cada dia ele pede que recrutemos mais candidatos para|
            |ele. Porém, uma coisa que acho muito estranha é que nunca os vejo  |
            |novamente. Eu sinto falta da senhorinha que todas as manhãs        |
            |sentava no banco, ao lado de seu dormitório, para comer seu pão com|
            |cafézinho já que os refeitórios sempre estão lotados. Ou então don-|
            |zela que sempre sempre conversava comigo sobre assuntos mais sérios|
            |e até um pouco estranhos as vezes. Muitas das vezes os assuntos re-|
            |lacionávam-se a física, ela sempre pareceu saber muito sobre os as-|
            |suntos que conversávamos, mas seu marido avisou que ela era muito  |
            |manipuladora e por isso faria-nos pensar que estaria sã. Aliás ele |
            |é um físico renomado, pode ser que essa fixação pela área seja por |
            |causa da genialidade de seu marido.                                |
            |     Bom de qualquer forma, eu vim para este hospital por ser refe-|
            |rência na área da psiquiatria, mas começo a pensar que sumir com   |
            |pessoas ou fazer com que seus pacientes percam a capacidade da fala|
            |ou enxergar ou andar não seja um tipo de tratamento e sim tortura. |
            |Mal posso esperar pela resposta da aprovação para trabalhar em To- |
            |ledo e poder finalmente sair daqui. Por onde passo sinto arrepios. |
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


DICA = str('''
            _____________________________________________
            |                                           |
            |         Os 3 primeiros se repetem         |
            |           e o quarto é singular,          |
            |         para quem tenta se comunicar.     |
            |                                           |
            |___________________________________________|
''')

CARTA2 = str('''
            _________________________________________________________
            |                                                       |
            |   Eu não sei o que que pode estar acontecendo comigo, |
            |   é como se eu não tivesse mais controle sobre mim.   |
            |   Eu tenho pesadelos o tempo todo, até mesmo durante  |
            |   o dia. EU NÃO TENHO MAIS CONTROLE DOS MEUS pEnSaR   |
            |   Eu preciso de AJUDA, mas não desse lugar.           |
            |                                                       |
            |   Fizeram uma cirurgia no meu cérebro, agora sinto que|
            |   estou MaIs inteliGenTE DO QUE NUNCA, mas Ele NÃO VAI|
            |   PEGAAARRRR, É MEU, TUDO MEU.                        |
            |                                                       |
            |           Preciso respirar, antes que eu me perca de  |
            |           vez, mas acho que cheguei a resposta        |
            |                                7%394^4548             |
            |_______________________________________________________|
''')

DOCUMENTO = str('''
            _________________________________________________________
            |                                                       |
            |   Cirurgias aplicadas:                                |
            |                                                       |
            |   - Trepanação;                                       |
            |   - Choque insulínico;                                |
            |   - Lobotomia;                                        |
            |   - Mesmerísmo;                                       |
            |   - Fake Smile;                                       |
            |                                                       |
            |                                                       |
            |   Estas foram algumas das cirurgias que consegui en-  |
            |contrar vestígios e provas neste lugar que nunca imagi-|
            |nei ter que voltar. Várias das criaturas que estão pre-|
            |sas aqui, tiveram sua origem por causa de várias dessas|
            |cirurgias experimentais, onde algumas eam feiras e não |
            |se tem nem registro, até porquê sairam da cabeça daque-|
            |le doutor fajuto que nos torturou por anos, eu ainda ti|
            |ve sorte de ter sido dos últimos a chegar neste inferno|
            |_______________________________________________________|
''')

DOCUMENTO2 = str('''
            _____________________________________________________
            |                                                   |
            |   O rolchinol está aqui, não sei que momento ele  |
            |   irá acordar mas espero que fique tão indignado  |
            |   quanto nós que vivemos este lugar. Ele precisa  |
            |   descobrir que foi o pai dele quem fez isso      | 
            |   conosco. Aquele monstro, depois que foi tudo    |
            |   descoberto, trancou o laboratório da tortura    | 
            |   dele e conseguiu esconder as pessoas que ele    |
            |   chamava de cobaias, ELE AS DEIXOU VIVAS AQUI    |
            |   COM AS CIRURGIAS FEITAS OU POR TERMINAR, ELE    |
            |   SUMIU E DEIOU ELAS PRA MORREREM. Mas por algum  |
            |   motivo elas sobreviveram e se tornaramm monstros|
            |   o rolchinol precina nos ajudar, ELE PRECISA     |
            |    MOSTRAR PARA O MUNDO O MONSTRO QUE SEU PAI FOI.|
            |___________________________________________________|
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


def achando_arma_2():
    arma_2 = 'Espingarda'
    print('''           Você achou uma Espingarda''')
    print(ARMA2)
    funcoes1.deseja_guardar(arma_2)


def achando_relatorio():
    relatorio = 'Relatorio 1'
    print(RELATORIO)
    funcoes1.deseja_guardar(relatorio)


def achando_relatorio2():
    relatorio = 'Relatorio 2'
    print(RELATORIO_2)
    funcoes1.deseja_guardar(relatorio)


def achando_doc_5152():
    doc = 'Documento cobaia 5152'
    print(DOCUMENTO_COB_5152)
    #funcoes1.deseja_guardar(doc)


def achando_chave2():
    chave = 'Chave 2'
    print(CHAVE_2)
    funcoes1.deseja_guardar(chave)


def achando_chave3():
    chave = 'Chave 3'
    print(CHAVE_3)
    funcoes1.deseja_guardar(chave)


def achando_chave6():
    chave = 'Chave 6'
    print(CHAVE_6)
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


def achando_cofre2():
    print(COFRE)
    print(funcoes1.mostrando_atributos())
    input('Tecle "enter" para avançar')
    funcoes2.escolher_item()
    print(COFRE)
    print(funcoes1.mostrando_atributos())
    input('Tecle "enter" para avançar')
    while True:
        print('''
                    QUAL A SENHA DO COFRE??

                    s- para sair das tentativas
        ''')
        resp = input('Responda e tecle "enter" para avançar\n')
        if resp == '3063':
            achando_arma_2()
            input('Tecle "enter" para avançar')
            achando_chave2()
            input('Tecle "enter" para avançar')
            achando_relatorio2()
            break
        elif resp == 's':
            break
        else: 
            print('Senha incorreta!! tente novamente.')
            funcoes2.escolher_item()

def achando_carta():
    carta = 'Carta'
    print(CARTA)
    funcoes2.deseja_guardar(carta)

def achando_carta2():
    carta = 'Carta 2'
    print(CARTA2)
    funcoes2.deseja_guardar(carta)

def achando_tradu_carta():
    tradu_carta = 'Tradução da Carta'
    print(TRADU_CARTA)
    funcoes2.deseja_guardar(tradu_carta)

def achando_dica():
    dica = 'Dica'
    print(DICA)
    funcoes2.deseja_guardar(dica)

def achando_documento():
    doc = 'Documento'
    print(DOCUMENTO)
    funcoes2.deseja_guardar(doc)

def achando_documento2():
    doc = 'Documento 2'
    print(DOCUMENTO2)
    funcoes2.deseja_guardar(doc)
