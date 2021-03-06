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
            | Local: Hospital de Reabilita????o Psiquiatra Col??nia                |
            | Endere??o: Barbacoa,  Montes Uivantes - Brasil                     |
            |                                                                   |
            |                                                                   |
            | Relat??rio do paciente:                                            |
            |   J?? fazem 2 meses desde o in??cio, aparentemente a cobaia 5152    |
            |est?? piorando conforme os testes para reverter sua situa????o mental.|
            |Foram feitos diversos tratamentos que a princ??pio n??o refletiram   |
            |nenhum efeito no paciente. Contudo posso afirmar que a terapia de  |
            |choque insul??nico a acalmou e fez parar de falar do suposto filho  |
            |morto pelo marido. Nas pr??ximas semanas ir??o ocorrer mais sess??es, |
            |esperamos que ela volte a sua sanidade e finalmente lembre da ver- |
            |dade.                                                              |
            |                                                                   |
            |OBS: Em rela????o as hist??rias que a paciente conta, que fique bem   |
            |claro que o marido afirmou que o beb?? nasceu morto. Ele ?? um homem |
            |de boa palavra e boa ??ndole para a sociedade, ent??o devemos acredi-|
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
            | Local: Hospital de Reabilita????o Psiquiatra Col??nia                |
            | Endere??o: Barbacoa,  Montes Uivantes - Brasil                     |
            |                                                                   |
            |                                                                   |
            | Relat??rio do m??s:                                                 |
            |  N??o sei o que pode estar acontecendo, j?? faz mais de um ano que  |
            |come??amos os tratamentos intensivos com m??todos vindos da europa e |
            |dos USA, mas h?? algo de errado. Algumas cobaias n??o resistiram, por|
            |isso teremos que recrutar mais delas, mas algumas est??o mudando (o |
            |que me faz pensar que estamos tendo progresso). No entanto algumas |
            |das mudan??as est??o sendo um pouco assustadoras at?? pra mim, como   |
            |sorrisos constantes e bem abertos (lembrando que n??o s??o das 15 co-|
            |baias que fizemos a cirurgia de Fake Smile) ou olhos esbugalhados e|
            |fixos com pupilas dilatadas o tempo todo (tirando 20 cobaias desse |
            |m??s que passaram por uma lobotomia). Por fim sei que estamos pro-  |
            |gredindo e isso ?? muito bom.                                       |
            |___________________________________________________________________|
''')

RELATORIO_2 = str('''
            _____________________________________________________________________
            |                                                                   |
            | Dr. Fernando Nogueira Nobrega                                     |
            | Data: 09/01/1963                                                  |
            | Local: Hospital de Reabilita????o Psiquiatra Col??nia                |
            | Endere??o: Barbacoa,  Montes Uivantes - Brasil                     |
            |                                                                   |
            |                                                                   |
            |  Dr. Joseph ainda pede pacientes para realizar os seus tratamentos|
            |alternativos, cada dia ele pede que recrutemos mais candidatos para|
            |ele. Por??m, uma coisa que acho muito estranha ?? que nunca os vejo  |
            |novamente. Eu sinto falta da senhorinha que todas as manh??s        |
            |sentava no banco, ao lado de seu dormit??rio, para comer seu p??o com|
            |caf??zinho j?? que os refeit??rios sempre est??o lotados. Ou ent??o don-|
            |zela que sempre sempre conversava comigo sobre assuntos mais s??rios|
            |e at?? um pouco estranhos as vezes. Muitas das vezes os assuntos re-|
            |lacion??vam-se a f??sica, ela sempre pareceu saber muito sobre os as-|
            |suntos que convers??vamos, mas seu marido avisou que ela era muito  |
            |manipuladora e por isso faria-nos pensar que estaria s??. Ali??s ele |
            |?? um f??sico renomado, pode ser que essa fixa????o pela ??rea seja por |
            |causa da genialidade de seu marido.                                |
            |     Bom de qualquer forma, eu vim para este hospital por ser refe-|
            |r??ncia na ??rea da psiquiatria, mas come??o a pensar que sumir com   |
            |pessoas ou fazer com que seus pacientes percam a capacidade da fala|
            |ou enxergar ou andar n??o seja um tipo de tratamento e sim tortura. |
            |Mal posso esperar pela resposta da aprova????o para trabalhar em To- |
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
            |   - = ESPA??O      % = R   [ = G   \ = V   |
            |   9 = P   & = F   } = H                   |
            |___________________________________________|
''')


DICA = str('''
            _____________________________________________
            |                                           |
            |         Os 3 primeiros se repetem         |
            |           e o quarto ?? singular,          |
            |         para quem tenta se comunicar.     |
            |                                           |
            |___________________________________________|
''')

CARTA2 = str('''
            _________________________________________________________
            |                                                       |
            |   Eu n??o sei o que que pode estar acontecendo comigo, |
            |   ?? como se eu n??o tivesse mais controle sobre mim.   |
            |   Eu tenho pesadelos o tempo todo, at?? mesmo durante  |
            |   o dia. EU N??O TENHO MAIS CONTROLE DOS MEUS pEnSaR   |
            |   Eu preciso de AJUDA, mas n??o desse lugar.           |
            |                                                       |
            |   Fizeram uma cirurgia no meu c??rebro, agora sinto que|
            |   estou MaIs inteliGenTE DO QUE NUNCA, mas Ele N??O VAI|
            |   PEGAAARRRR, ?? MEU, TUDO MEU.                        |
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
            |   - Trepana????o;                                       |
            |   - Choque insul??nico;                                |
            |   - Lobotomia;                                        |
            |   - Mesmer??smo;                                       |
            |   - Fake Smile;                                       |
            |                                                       |
            |                                                       |
            |   Estas foram algumas das cirurgias que consegui en-  |
            |contrar vest??gios e provas neste lugar que nunca imagi-|
            |nei ter que voltar. V??rias das criaturas que est??o pre-|
            |sas aqui, tiveram sua origem por causa de v??rias dessas|
            |cirurgias experimentais, onde algumas eam feiras e n??o |
            |se tem nem registro, at?? porqu?? sairam da cabe??a daque-|
            |le doutor fajuto que nos torturou por anos, eu ainda ti|
            |ve sorte de ter sido dos ??ltimos a chegar neste inferno|
            |_______________________________________________________|
''')

DOCUMENTO2 = str('''
            _____________________________________________________
            |                                                   |
            |   O rolchinol est?? aqui, n??o sei que momento ele  |
            |   ir?? acordar mas espero que fique t??o indignado  |
            |   quanto n??s que vivemos este lugar. Ele precisa  |
            |   descobrir que foi o pai dele quem fez isso      | 
            |   conosco. Aquele monstro, depois que foi tudo    |
            |   descoberto, trancou o laborat??rio da tortura    | 
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
    print('''           Voc?? achou uma Faca''')
    print(FACA)
    funcoes1.deseja_guardar(faca)


def achando_cura_1():
    cura1 = 'Cura-1'
    print('''           Voc?? achou uma Cura-1''')
    print(POCAO1)
    funcoes1.deseja_guardar(cura1)


def achando_cura_2():
    cura2 = 'Cura-2'
    print('''           Voc?? achou uma Cura-2''')
    print(POCAO2)
    funcoes1.deseja_guardar(cura2)


def achando_arma_1():
    arma_1 = 'Glock G42'
    print('''           Voc?? achou uma Glock G42''')
    print(ARMA1)
    funcoes1.deseja_guardar(arma_1)


def achando_arma_2():
    arma_2 = 'Espingarda'
    print('''           Voc?? achou uma Espingarda''')
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
    input('Tecle "enter" para avan??ar')
    while True:
        print('''
                    QUAL A SENHA DO COFRE??

                    s- para sair das tentativas
        ''')
        resp = input('Responda e tecle "enter" para avan??ar\n')
        if resp == '5152':
            achando_arma_1()
            input('Tecle "enter" para avan??ar')
            achando_chave2()
            input('Tecle "enter" para avan??ar')
            achando_relatorio()
            break
        elif resp == 's':
            break
        else: 
            print('Senha incorreta!! tente novamente.')


def achando_cofre2():
    print(COFRE)
    print(funcoes1.mostrando_atributos())
    input('Tecle "enter" para avan??ar')
    funcoes2.escolher_item()
    print(COFRE)
    print(funcoes1.mostrando_atributos())
    input('Tecle "enter" para avan??ar')
    while True:
        print('''
                    QUAL A SENHA DO COFRE??

                    s- para sair das tentativas
        ''')
        resp = input('Responda e tecle "enter" para avan??ar\n')
        if resp == '3063':
            achando_arma_2()
            input('Tecle "enter" para avan??ar')
            achando_chave2()
            input('Tecle "enter" para avan??ar')
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
    tradu_carta = 'Tradu????o da Carta'
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
