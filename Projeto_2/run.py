import runing_level


def run():
    while True:
        runing_level.verificando_arquivos()
        runing_level.Menu()
        gameover = runing_level.level_1()
        if gameover == True:
            break
        else:
            game_over = runing_level.level_2()
            if game_over == True:
                break

run()