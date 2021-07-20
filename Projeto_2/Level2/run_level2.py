from Level2 import hist_parte2, funcoes2
from time import sleep



def hist2():
    i = 0
    while True:
        print(hist_parte2.historia_parte2[i])
        funcoes2.mostrando_atributos()
        input('Tecle "enter" para avançar')
        sleep(1)
        i=i+1
        if hist_parte2.historia_parte2[i] == hist_parte2.historia_parte2[-1]:
            print(hist_parte2.historia_parte2[-1])
            input('Tecle "enter" para avançar')
            break
    funcoes2.mostrando_atributos()
    hist_parte2.qual_seu_nome()


def exploracao():
    pos = 1
    gameover = False
    while True:
        lista_vida = funcoes2.mostrando_vida()
        if len(lista_vida) == 0:
            print(hist_parte2.gameover)
            gameover = True
            break
        print(f'''

             ====================================================
                
                {hist_parte2.lista_salas[pos-1]}            {hist_parte2.lista_salas[pos]}            {hist_parte2.lista_salas[pos+1]}

             ====================================================
        ''')
        #sleep(1.25)
        print(hist_parte2.decisao_acao)
        funcoes2.mostrando_atributos()
        resp = input('Responda e tecle "enter" para avançar\n')
        if resp in hist_parte2.lista_salas:
            hist_parte2.quartos(resp)
        if resp in 'lL':
            pos = pos+1
        if resp in 'jJ':
            pos = pos-1
        if resp in 'sS':
            print("Saindo")
            funcoes2.movimentacao()
            break
    return gameover
    
