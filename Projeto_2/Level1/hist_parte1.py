from Level1 import funcoes1


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
    nome = input("Escreva seu nome:\n")
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

quartinho2 = str('''
            Na parte superior há uma porta bem ao meio e nas extremidades algo
            que já foi uma escrivaninha, na direira e um monte de intulho
            na esquerda.
''')

quartinho3 = str('''
            É tudo tão velho e sujo que não dá pra imaginar que lugar é esse!
            Ou melhor, que lugar FOI esse.
''')

quartinho4 = str('''
            ===========    ==========
            =####                 &&=
            =                       =
            =                       =
            =                       =
            =                       =
            =||||               [  ]=
            =========================
''')

lista_quarto = [quartinho1, quartinho2, quartinho3, quartinho4]

decisao_acao2 = str('''
            Pra onde deseja ir?
            
            a- Armário
            w- Escrivaninha
            s- Entulho
            d- Porta
''')