def start_game():
    print('''
                =============================================
                =                                           =
                =                                           =
                =             Seja Bem Vindo!!              =
                =                                           =
                =             Aperte "e" para               =
                =                 começar                   =
                =                                           =
                =                                           =
                =============================================
    ''')

def entrando_no_jogo():
    start_game()
    start = input("").lower()
    while start != "e":
        start_game()
        start = input("").lower()
    