#Importações:
from time import sleep

import verificando_arq
import menu
from Level1 import run_level1

#Criando e verificando se arquivo e pasta existem:
def verificando_arquivos():
    verificando_arq.criando_pasta_arquivos()
    verificando_arq.cria_verifica_arq_nome()
    verificando_arq.cria_verifica_arq_vida()
    verificando_arq.cria_verifica_arq_cinto()
    verificando_arq.cria_verifica_arq_mochila()
    verificando_arq.cria_verifica_vida_boss()


#Menu para começar o jogo:
def Menu():
    menu.entrando_no_jogo()
    sleep(1)
    print("""           ...""")
    sleep(1)

#História LEVEL 1:
def level_1():
    run_level1.hist1()
    run_level1.pensamento1()
    run_level1.nome1()
    run_level1.movimento_1()
    run_level1.quartinho()
    run_level1.movimento_2()
    run_level1.descricao_corredor()
    gameover = run_level1.explorando_quartos()

    return gameover
    
