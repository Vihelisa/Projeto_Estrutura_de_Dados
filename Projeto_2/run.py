import runing_level


def run():
    while True:
        runing_level.verificando_arquivos()
        runing_level.Menu()
        gameover = runing_level.level_1()
        if gameover == True:
            break
        else:
            print('Conseguiu')
        

run()