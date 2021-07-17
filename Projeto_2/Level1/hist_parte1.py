from Level1 import funcoes1
from Itens import itens
from time import sleep

parag1 = str('''
            Você abre os olhos...
''')

parag2 = str('''
            Tudo está muito escuro...
            Tão escuro que seus olhos demoram para se acostumar.
''')

parag3 = str('''
            Tua cabeça dói... 
            Dói como se um martelo estivesse pregando um prego bem no meio dela...
            Tudo gira lentamente...
            O corpo está doendo, como se algo tivesse acabado de te esmagar.
''')

parag4 = str('''
            A respiração está pesada, como se o ar estivesse rarefeito...
            "HÁ ALGO DE ERRADO" grita a sua intuição, mas você está tão ruim que quase não consegue
            pensar direto, por isso não consegue ter a menor ideia do que pode ter acontecido...
            ou do que está acontecendo.
''')

parag5 = str('''
            Você então percebe que está em uma cama...
            O colchão é velho... 
            Fino...Desconfortável.
            As pernas, ao que parace enferrujadas pelo tempo, indica um ranger insurdecedor
            a cada movimento que faz.
''')

parag6 = str('''
            O QUE É ISSO?!
''')

parag7 = str('''
            ...
''')

parag8 = str('''
            Depois de um tempo... 
            com os sentidos um pouco menos adormecidos, 
            você começa a sentir um cheiro horrível. 
            É uma mistura desagradável de mofo e poeira vindo dos seus arredores.
''')

parag9 = str('''
            Então, você consegue perceber onde está...
            É um lugar pequno, todo fechado e muito escuro.
            Aparentemente parece ser uma pequena sala...ou será um quarto??
''')


pensamento = str('''
            Um pouco melhor da dor de cabeça e com os sentidos começando a aparecer, 
            você começa a pensar um pouco melhor.\n
''')

historia_parte1 = [parag1, parag2, parag3, parag4, parag5, parag6, parag7, parag8, parag9, pensamento]


decisao = str('''
            O que você está pensando?
            
            a- "Que lugar é esse?"
            w- "Onde eu estou?"
            s- "O que aconteceu comigo?"
            d- "Como eu vim parar aqui?"
''')

parag10 = str('''
            É muito difícil de lembrar...
            Aliás você não lembra de absolutamente nada... lembra?
            Então uma pergunta começa a ecoar dentro de você...
''')

def quem_e_voce():
    lista_nome = []
    print('''
                =============================================
                =                                           =
                =                                           =
                =             "QUEM É VOCÊ????"             =
                =                                           =
                =                                           =
                =============================================
    
    ''')
    nome = input("Escreva seu nome:\n").capitalize()
    print('''
                \n
                SERÁ QUE É??!!
    ''')
    return nome


def pensando_no_nome() :
    lista_nomes = funcoes1.lendo_nome_arq()
    nome = lista_nomes[0].replace("\n", '')
    pensa = str(f'''
                Você chega a pensar em {nome}...
                mas será que esse é o seu verdadeiro nome?
                Acho que a única coisa que pode fazer agora é acreditar que 
                o primeiro nome que apareceria na cabeça de uma pessoa sem memória
                seria "O PRÓPRIO NOME".
    ''')
    return pensa

decisao_acao1 = str('''
            O que você faz?
            
            a- "Sentar-se na cama e observar melhor o lugar?"
            w- "Tentar levantar e andar um pouco?"
            s- "Deitar-se novamente e respirar um pouco antes de ver o local?"
''')

quartinho1 = str('''
            Olhando melhor agora você consegue ver como esse "quarto" é pequeno.
            Ele é um pequeno quadrado com uma cama bem velha no canto inferior direito e 
            algo que parece um armário no inferior esquerdo.
''')

perceber_cinto = str(f'''
               Ao sair da cama você percebe que estranhamente há um cinto 
               preso em suas roupas, aliás roupas que não parecem ser suas, 
               mas não dá pra ter certeza. Também há uma mochila ao lado da
               cama que poderá ser útil e que você nem pensa e logo a pega.
''')

quartinho2 = str('''
            Na parte superior há uma porta estreita bem ao meio do quarto.
            Nas extremidades algo que já foi uma escrivaninha, na direira e 
            um monte de intulho na esquerda.
''')

quartinho3 = str('''
            É tudo tão velho e sujo que não dá pra imaginar que lugar é esse!
            Ou melhor, que lugar FOI esse.
''')

quartinho4 = str('''
             REPRESENTAÇÃO DO QUARTO
             
            ===========    ==========
            =####                 &&=
            =                       =
            =                       =
            =                       =
            =                       =
            =||||               [  ]=
            =========================
''')

lista_quarto = [quartinho1, perceber_cinto, quartinho2, quartinho3, quartinho4]

decisao_acao2 = str('''
            Pra onde deseja ir?
            
            a- Armário
            w- Escrivaninha
            s- Entulho
            d- Porta
''')

esperimento1 = str('''
            Saindo do quarto você percebe que está em um corredor largo,
            com várias portas, algumas arrombadas, outras com partes quebradas
            e outras intáctas. Por algum motivo estranho este lugar te dá
            calafrios.
''')

esperimento2 = str('''
            Então cai a fixa de que o lugar onde acordou é apenas um de, o que parce
            ser, um total de 8 quartos como o teu. 
''')

esperimento3 = str('''
                      REPRESENTAÇÃO DO LUGAR
            ___
            |!|=======___====   ====   ====___========
            |=|\             ###                 ####=
            |=|               ;#$|                   =
            |=\                                    //=
            ======  &|=====   ====_ _====  |===========
''')

esperimento4 = str('''
            Você então consegue ver que há um pouco mais de iluminação
            neste ambiente devido a buracos nas pareces que deixam a luz
            entrar um pouco mais.
''')

esperimento5 = str('''
            Esta tudo quebrado, cheio de entulho.
            Em alguns lugares o espaço é até bloqueado por madeira, móveis
            quebrados e lixo. 
''')

esperimento6 = str('''
            QUE LUGAR É ESSE?
''')

lista_corredor = [esperimento1, esperimento2, esperimento3, esperimento4, esperimento5, esperimento6]

decisao_acao3 = str('''
            Escolha o quarto que deseja ir?

            l- para ir para frente
            j- para ir para trás
            s- para ir para a escada

            Para escolher um quarto escreva o nome que aparece na tela
''')

lista_quartos = ["Quarto 1", "Quarto 2", "Quarto 3", "Quarto 4", "Quarto 5", "Quarto 6", "Quarto 7", "Quarto 8"]

quarto_5 = str('''
            A porta está trancada, mas há um grtande buraco no meio da porta.
            Não é possível passar, mas dá pra pereber que é um quarto todo quebrado, 
            apenas dá pra ver lixo, madeira e nada mais.
            Não parece ter nada de importante.
''')

Q2_p1 = str('''
            Você mexe na maçaneta da porta e nada acontece. ESTÁ TRANCADA!
''')

Q2_p2 = str('''
            Você olha para um papel que está encaixado num campo preso a porta.
''')

Q2_p3 = str('''
            Você pega esse papel?

            a- Sim
            s- Não
''')

lista_Q2_parte1 = [Q2_p1, Q2_p2, Q2_p3]

def quarto_2():
    lista_itens_mochila = funcoes1.lendo_mochila_arq()
    lista_itens_cinto = funcoes1.lendo_cinto_arq()
    if 'Documento cobaia 5152' in lista_itens_cinto or 'Documento cobaia 5152' in lista_itens_mochila:
        print(Q2_p1)
    i = 0
    while True:
        print(lista_Q2_parte1[i])
        print(funcoes1.mostrando_atributos())
        input('Tecle "enter" para avançar')
        sleep(1)
        i=i+1
        if lista_Q2_parte1[i] == lista_Q2_parte1[-1]:
            print(lista_Q2_parte1[-1])
            break
    resp = input('Responda e tecle "enter" para avançar\n').lower()
    if resp == 'a':
        itens.achando_doc_5152()
    

def quartos(quarto):
    if quarto == 'Quarto 1':
        print("       O quarto em que você acordou não parece ter nada de errado ou algo a mais para ver.")
    if quarto == 'Quarto 2':
        quarto_2()
    if quarto == 'Quarto 3':
        print("       Este é o quarto 3")
    if quarto == 'Quarto 4':
        print("       Há uma pilha de móveis barrando a passagem e a porta está fechada também, não dá pra passar")
    if quarto == 'Quarto 5':
        print(quarto_5)
    if quarto == 'Quarto 6':
        print("       Este é o quarto 3")
    if quarto == 'Quarto 7':
        print("       Este é o quarto 3")
    if quarto == 'Quarto 8':
        print("       Este é o quarto 3")
    