from Level2 import funcoes2
from time import sleep


parag1= str('''
            Ao subir as escadas e abrir a porta, você consegue ver um corredor longo 
            que dá a uma porta grande que ao que parece dá para fora hospital.
''')

parag2= str('''
            Ao longo do corredor se vê várias portas, ao que parece são diferentes 
            salas e quartos.
''')

parag3= str('''
            Também é possível ver uma espécie de hall para receber pessoas que pro-
            vávelmente estariam trasendo novos "pacientes" ou visitar eles.
''')

parag4= str('''
            Todo o lugar parece estar deteriorado, quebrado, sujo, causas do tempo.
            Mas o lugar é bem frio e assustador, tão assustador quanto a 
            criatura que você acabou de matar.
''')

parag5= str('''
                        REPRESENTAÇÃO DO LOCAL
                                                      _______
                                                     /=\     \ 
            ==========___========__========___=====/\=       |_____
            =###            ###        U U              ##    | | | |
            =                                           ##    | | | |
            =              ###       U U U                    |_|_|_|
            =  &|=====___========___========___=====\  U  U   |
             |==|                                    \_______/
''')

historia_parte2 = [parag1, parag2, parag3, parag4, parag5]


def qual_seu_nome():
    lista_nomes = funcoes2.lendo_nome_arq()
    print(f'''
                Você acabou de lutar contra uma criatura horrenda. Como você está?
                Aliás qual era mesmo o seu nome?

                a- {lista_nomes[0]}
                w- {lista_nomes[1]}
                s- {lista_nomes[2]}
                d- {lista_nomes[3]}
    ''')
    resp = input('Responda e tecle "enter" para avançar\n').lower()
    if resp == 'a':
        nome = lista_nomes[0]
        funcoes2.guardando_nome(nome)
    if resp == 'w':
        nome = lista_nomes[1]
        funcoes2.guardando_nome(nome)
    if resp == 's':
        nome = lista_nomes[2]
        funcoes2.guardando_nome(nome)
    if resp == 'd':
        nome = lista_nomes[3]
        funcoes2.guardando_nome(nome)


decisao_acao = str('''
            Escolha o quarto que deseja ir?

            l- para ir para frente
            j- para ir para trás
            s- para ir para a escada

            Para escolher um quarto escreva o nome que aparece na tela
''')

lista_salas = ['Sala 1', 'Sala 2', 'Sala 3', 'Sala 4', 'Sala 5', 'Sala 6',]
 
desc_quartos = str('''
            Ao abrir a porta você vê uma espécie de dormitório relativamente largo e bem comprido.
            Ele possui várias camas, todas iguais a que você acordou. Velhas. Enferrujadas. Sujas.
            Pequenas e desconfortáveis.
''')

desc_quartos2 = str('''
            É possível perceber que o número de camas no ambiente chega ser exagerado. E além do mais 
            há colchões, iguais os das camas, no chão. Ao que parece muitas pessoas dormiam juntas
            e eram tantas que precisavam dormir no chão.
''')

acao_S1 = str('''
            Deseja esplorar o lugar?

            a- Entrar e explora o lugar
            s- Procura ver outra sala
''')

S1_p1 = str('''
            Você anda lentamente entre as camas que, uma a uma, deixam curiosamente seu rastro de palha pelo chão, 
            como uma assinatura, um DNA de cada uma, pois é perceptível que nenhum é igual ao outro. Encarando cada 
            leito, voce tenta entender: "O que se passava neste lugar pra precisar de tantas camas".
''')

S1_p2 = str('''
            O ar é seco, pesado, com um cheiro de poeira misturado com algo forte, indescritível,
            estranho. Tudo neste lugar é ESTRANHO.
''')

S1_p3 = str('''
            Passando o olhar por de baixo de uma das camas, você vê que há algo de estranho ali.
''')

S1_p4 = str('''
            O que você faz?

            a- Examina para ver o que pode ser 
            s- Continua a exploração
''')

lista_S1 = [S1_p1, S1_p2, S1_p3, S1_p4]

def sala_1():
    print(desc_quartos)
    print(funcoes2.mostrando_atributos())
    input('Tecle "enter" para avançar')
    print(desc_quartos2)
    print(funcoes2.mostrando_atributos())
    input('Tecle "enter" para avançar')
    print(acao_S1)
    resp = input('Responda e tecle "enter" para avançar\n').lower()
    if resp == 'a':
        i = 0
        while True:
            print(lista_S1[i])
            funcoes2.mostrando_atributos()
            input('Tecle "enter" para avançar')
            sleep(1)
            i=i+1
            if lista_S1[i] == lista_S1[-1]:
                print(lista_S1[-1])
                break
        respp = input('Responda e tecle "enter" para avançar\n').lower()
        if respp == 'a':
            pass

def quartos(quarto):
    if quarto == 'Sala 1':
        funcoes2.movimentacao()
        sala_1()
    if quarto == 'Sala 2':
        funcoes2.movimentacao()
        
    if quarto == 'Sala 3':
        funcoes2.movimentacao()
        
    if quarto == 'Sala 4':
        funcoes2.movimentacao()
        
    if quarto == 'Sala 5':
        funcoes2.movimentacao()
        
    if quarto == 'Sala 6':
        funcoes2.movimentacao()
        




gameover = str("""
                =========================================
                =                                       =
                =               GAME OVER               =
                =                                       =
                =========================================
        """)