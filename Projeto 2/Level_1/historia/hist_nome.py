def quem_e_voce():
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

def lista_nomes(nome): #Criar um arquivo para guardar os nomes do jogador e fazer a brincadeira dele ir lembrando o nome durante o jogo
    list_names = []
    list_names.append(nome)
    return list_names