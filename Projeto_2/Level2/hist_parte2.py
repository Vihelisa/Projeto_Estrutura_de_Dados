from Level2 import funcoes2
from time import sleep
from Itens import itens


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
            ==========___========___========___=====/\=       |_____
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

acao_1 = str('''
            Deseja explorar o lugar?

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

pista = str('''
            Perto da parede, antes escondido entre uma das pernas da cama, você consegue 
            achar um papel com algo nele.
''')

def sala_1():
    print(desc_quartos)
    print(funcoes2.mostrando_atributos())
    input('Tecle "enter" para avançar')
    print(desc_quartos2)
    print(funcoes2.mostrando_atributos())
    input('Tecle "enter" para avançar')
    print(acao_1)
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
            print(pista)
            itens.achando_carta()


porta_trancada = str('''
            Você mexe na maçaneta da porta e nada acontece. ESTÁ TRANCADA!
''')

S2_p1 = str('''
            Você abre a porta e vê apenas mais um dormitório, cheio de camas e colchões igual
            aos outros.
''')

boss1_p1 = str('''
            Você entra no dormitório e anda lentamente entre as camas, uma a uma.
''')

boss1_p2 = str('''
            Quando de repente a porta do quarto bate, fechando-se bem atrás de você.
''')

boss1_p3 = str('''
           "Há mais alguém com você, isso é óbvio, mas quem está aqui?" 
''')

boss1_p4 = str('''
            Pensa você enquanto olha para todos os lados.
''')

boss1_p5 = str('''
            Então você decide olhar para cima e vê algo que NUNCA PENSOU que existiria.
''')

#Significa ladrão em macedônio
boss1_p6 = str('''
            wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
            w               Kradec              w
            wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
''')

boss1_p7 = str('''
            Uma criatura horrenda e asquerosa que faz imlorar para tirar os olhos dela. MAS NÃO DÁ.
            Kadrec possui algo que te hipnotiza e te faz tremer de tanto horror. 
''')

boss1_p8 = str('''
            Ele possui um rosto estremamente fino e alongado, con trações do que um dia fora uma cabeça
            humana e hoje deformada. No topo de sua cabeça há um braco que contem uma massa asquerosa que
            solta uma espécie de gosma o tempo todo, parecendo um cérebro exposto, inchado e querendo entrar 
            em decomposição. Para proteger isso, de suas têmporas saí algo que se alonga formando uma pinsa 
            enorme q faz gotejar em você a gosma q sai da massa.
''')

boss1_p9 = str('''
            Nele não há olhos, no lugar á uma espiral formada por cicatrises e que assando bem ao meio
            dá lugar de destaque a uma rachadura. Logo abaixo do fm dessa rachadura uma boca enorme, 
            cheia de dentes pontudos e afiados formando também um espiral que te chama pra dentro dele.
''')

boss1_p10 = str('''
            A cada minuto que passa parece que Kadrec suga de ti o pouco que ainda tem, o pouco que 
            conseguiu lembrar, ou que ainda está tentando lembrar, quem é você. Até mesmo as memorias 
            que te restam desse lugar estão sendo pouco a pouco tiradas e roubadas de você, para alimentar 
            esse enorme mostro que agora parece um grande cérebro gigante.
''')

lista_boss_1 = [boss1_p1, boss1_p2, boss1_p3, boss1_p4, boss1_p5, boss1_p6, boss1_p7, boss1_p8, boss1_p9, boss1_p10]

S2_p2 = str('''
            Ao acabar a luta, olhando a criatura morta ao chão, você percebe que um papel começou a cair, planando, 
            até pousar no monstro e logo em seguida algo mais pesado cai em cima do papel.
''')

S2_p3 = str('''
            Você então chega perto e encontra...
''')


def sala_2():
    while True:
        print(porta_trancada)
        escolha = funcoes2.escolher_item()
        if escolha == 'Chave 2':
            print(S2_p1)
            print(funcoes2.mostrando_atributos())
            input('Tecle "enter" para avançar')
            print(acao_1)
            resp = input('Responda e tecle "enter" para avançar\n').lower()
            if resp == 'a':
                i = 0
                while True:
                    print(lista_boss_1[i])
                    funcoes2.mostrando_atributos()
                    input('Tecle "enter" para avançar')
                    sleep(1)
                    i=i+1
                    if lista_boss_1[i] == lista_boss_1[-1]:
                        print(lista_boss_1[-1])
                        break
                arma = funcoes2.escolher_item()
                if arma == 'Glock G42':
                    dano = 3
                    funcoes2.luta_2(dano)
                if arma == 'Faca':
                    dano = 1
                    funcoes2.luta_2(dano)
                if arma == 'Espingarda':
                    dano = 5
                    funcoes2.luta_2(dano)
                break
        else: 
            break


def drop_boss_2():
    print(S2_p2)
    print(funcoes2.mostrando_atributos())
    input('Tecle "enter" para avançar')
    print(S2_p3)
    print(funcoes2.mostrando_atributos())
    input('Tecle "enter" para avançar')
    itens.achando_chave3()
    input('Tecle "enter" para avançar')
    itens.achando_carta2()

S3_p1 = str('''
            Você está assustado, por conta das criaturas estranhas que estão aparecendo.
            Então fica relutante em relação a entrar no quarto por um momento.
''')

S3_p2 = str('''
            Entretanto o anceio por lembrar quem é você de verdade e por qual motivo está aí é 
            muito maior do que qualquer medo que possa ter neste momento.
''')

S3_p3 = str('''
            Você finalmente abre a porta e vê apenas mais um dormitório, cheio de camas e colchões igual
            aos outros.
''')

boss2_p1 = str('''
            Porém há algo muito estranho, não precisa nem entrar para perceber isto.
''')

boss2_p2 = str('''
            Da escuridão do canto direito no fundo do dormitório, algo começa a sair e a crescer.
''')
boss2_p3 = str('''
            Você sente que não adianta correr, não adianta fazer nada, porque aquilo vai vir e 
            tomar você por inteiro, até que não sobrem vestígios da sua existência.
''')

boss2_p4 = str('''
            Então aquilo que antes apenas saia das sombras, agora começa a tomar forma e luz, muita luz
            e começa vir elegantemente até você.
''')

boss2_p5 = str('''
            wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
            w              SOK ZRACI            w
            wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
''')

boss2_p6 = str('''
            Uma criatura enorme, com uma postura inigualável gritando ferossidade e poder.
            Uma silhueta bem feminina e humana aparece por trás dos raios de choque que ela emana.
''')

boss2_p7 = str('''
            Impiedosa, insaciável por energia, ela destroi tudo que está em seu caminho. O que ela toca
            automaticamente se desfaz através de seus raiois. 
''')

boss2_p8 = str('''
            Sua cabeça fina e alongada, igual as outras criaturas que apareceram, contem dois olhos puchados, 
            fudos, pretos e vazios como dois buracos que penetram cada célula, querendo até mesmo o pequeno
            campo elétrico feito pelos átodos que constituem seu corpo. 
''')

boss2_p9 = str('''
            Seus cabelos foram tomados pela energia e tranformados em raios que podem acertar algo de muito longe.
            E suas mãos com dedos longos e finos, feito lâminas ponteagudas e muito afiadas, liberam o mesmo choque
            que passa por todo seu corpo.
''')

S3_p4 =  str('''
            Foi uma luta muito difícil, mas você conseguiu vencê-la. Ao derrotar aquela criatura,
            você percebe que há algo preso em seu pescoço, que antes não era possível ver por causa
            dos infinitos raios que chamavam a atenção só para eles.
''')

S3_p5 =  str('''
            Após esperar até que todos os impulsos elétricos acabassem, você encontra...
''')

lista_boss_2 = [S3_p1, S3_p2, S3_p3, boss2_p1, boss2_p2, boss2_p3, boss2_p4, boss2_p5, boss2_p6, boss2_p7, boss2_p8, boss2_p9]

def sala_3():
    while True:
        print(porta_trancada)
        escolha = funcoes2.escolher_item()
        if escolha == 'Chave 3':
            i = 0
            while True:
                print(lista_boss_2[i])
                funcoes2.mostrando_atributos()
                input('Tecle "enter" para avançar')
                sleep(1)
                i=i+1
                if lista_boss_2[i] == lista_boss_2[-1]:
                    print(lista_boss_2[-1])
                    break
            arma = funcoes2.escolher_item()
            if arma == 'Glock G42':
                dano = 3
                funcoes2.luta_3(dano)
            if arma == 'Faca':
                dano = 1
                funcoes2.luta_3(dano)
            if arma == 'Espingarda':
                dano = 5
                funcoes2.luta_3(dano)
            break
        else: 
            break


def drop_boss_3():
    print(S3_p4)
    print(funcoes2.mostrando_atributos())
    input('Tecle "enter" para avançar')
    print(S3_p5)
    print(funcoes2.mostrando_atributos())
    input('Tecle "enter" para avançar')
    itens.achando_chave6()
    '''input('Tecle "enter" para avançar')
    itens.achando_carta2()'''


def sala_4():
    print(desc_quartos)
    print(funcoes2.mostrando_atributos())
    input('Tecle "enter" para avançar')
    print(desc_quartos2)
    print(funcoes2.mostrando_atributos())
    input('Tecle "enter" para avançar')
    print(acao_1)
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
            print(pista)
            itens.achando_tradu_carta()

S5_p1 = str('''
            Ao abrir a porta você pode ver uma espécie de escritório, provavelmente de um dos médicos
            da época que o hospital ainda estava em funcionamento.
''')

S5_p2 = str('''
            Neste escritório há uma mesa bem ao centro, uma cadeira atrás, armários e escrivaninhas quebradas
            e  quadros velhos nas paredes. Por mais incrível que pareça, esse é o lugar mais bem preservado
            até agora.
''')

S5_p3 = str('''
            Pra onde deseja ir?

            a- Escrivaninha
            w- Ver quadros nas paredes
            s- Sair do quarto
''')

S5_p4 = str('''
            Você começa a observar todos os quadros ao redor do esritório. Alguns são de anatomia, outros
            apenas belas imagens, mas há um estranho. Então ao observar esse enorme quadro centralizado na parede
            principal do escritório, uma cópia muito bem feita de "O grito", você percebe que na verdade ele é 
            um cofre.
''')

S5_p5 = str('''
            Então apenas de olhar para a escrivaninha você vê...
''')

S5_p6 = str('''
            E bem embaixo você vê...
''')

def sala_5():
    print(S5_p1)
    print(funcoes2.mostrando_atributos())
    input('Tecle "enter" para avançar')
    print(S5_p2)
    print(funcoes2.mostrando_atributos())
    input('Tecle "enter" para avançar')
    print(acao_1)
    resp = input('Responda e tecle "enter" para avançar\n').lower()
    if resp == 'a':
        i = 0
        while True:
            print(S5_p3)
            funcoes2.mostrando_atributos()
            respp = input('Responda e tecle "enter" para avançar\n').lower()
            if respp == 'a':
                print(S5_p5)
                itens.achando_chave2()
                print(funcoes2.mostrando_atributos())
                input('Tecle "enter" para avançar')
                print(S5_p6)
                itens.achando_dica() 
            if respp == 'w':
                print(S5_p4)
                print(funcoes2.mostrando_atributos())
                input('Tecle "enter" para avançar')
                itens.achando_cofre2()
            if respp == 's':
                funcoes2.movimentacao()
                break


def sala_6():
    while True:
        print(porta_trancada)
        escolha = funcoes2.escolher_item()
        if escolha == 'Chave 6':
            pass
        else: 
            break
        

def quartos(quarto):
    if quarto == 'Sala 1':
        funcoes2.movimentacao()
        sala_1()
    if quarto == 'Sala 2':
        funcoes2.movimentacao()
        sala_2()
        lista_vida = funcoes2.mostrando_vida()
        if len(lista_vida) > 0:
            drop_boss_2()
        
    if quarto == 'Sala 3':
        funcoes2.movimentacao()
        sala_3()
        lista_vida = funcoes2.mostrando_vida()
        if len(lista_vida) > 0:
            drop_boss_3()
        
    if quarto == 'Sala 4':
        funcoes2.movimentacao()
        sala_4()
        
    if quarto == 'Sala 5':
        funcoes2.movimentacao()
        sala_5()
        
    if quarto == 'Sala 6':
        funcoes2.movimentacao()
        sala_6()
        




gameover = str("""
                =========================================
                =                                       =
                =               GAME OVER               =
                =                                       =
                =========================================
        """)