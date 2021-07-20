from time import sleep

from Level1 import hist_parte1, funcoes1, dec_a, dec_d, dec_s, dec_w, mecanica


#história parte 1:
def hist1():
    i = 0
    while True:
        print(hist_parte1.historia_parte1[i])
        print("Vida:", funcoes1.mostrando_vida())
        input('Tecle "enter" para avançar')
        sleep(1)
        i=i+1
        if hist_parte1.historia_parte1[i] == hist_parte1.historia_parte1[-1]:
            print(hist_parte1.historia_parte1[-1])
            break

def pensamento1():
    print("Vida:", funcoes1.mostrando_vida())
    input('Tecle "enter" para avançar')
    print(hist_parte1.decisao)
    resp = input('Responda e tecle "enter" para avançar\n').lower()
    if resp == "a":
        print("""           Que lugar é esse?""")
    elif resp == "w":
        print("""           Onde eu estou?""")
    elif resp == "s":
        print("""           O que aconteceu comigo?""")
    elif resp == "d":
        print("""           Como eu vim parar aqui?""")
    print("Vida:", funcoes1.mostrando_vida())
    input('Tecle "enter" para avançar')
    print(hist_parte1.parag10)
    print("Vida:", funcoes1.mostrando_vida())
    input('Tecle "enter" para avançar')
    
def nome1():
    nome = hist_parte1.quem_e_voce()
    funcoes1.guardando_nome(nome)
    input('Tecle "enter" para avançar')
    pensa = hist_parte1.pensando_no_nome()
    print(pensa)
    input('Tecle "enter" para avançar')

def movimento_1():
    print(hist_parte1.decisao_acao1)
    resp = input('Responda e tecle "enter" para avançar\n').lower()
    if resp == "a":
        dec_a.acao_1a()
        print("Vida:", funcoes1.mostrando_vida())
        input('Tecle "enter" para avançar')
    elif resp == "w":
        dec_w.acao_1w()
        mecanica.mecanica_0()
    elif resp == "s":
        print(dec_s.parag1)
        print("Vida:", funcoes1.mostrando_vida())
        input('Tecle "enter" para avançar')
        print(dec_s.parag2)
        print("Vida:", funcoes1.mostrando_vida())
        input('Tecle "enter" para avançar')

def quartinho():
    i = 0
    while True:
        print(hist_parte1.lista_quarto[i])
        print("Vida:", funcoes1.mostrando_vida())
        input('Tecle "enter" para avançar')
        sleep(1)
        i=i+1
        if hist_parte1.lista_quarto[i] == hist_parte1.lista_quarto[-1]:
            print(hist_parte1.lista_quarto[-1])
            break

def movimento_2():
    input('Tecle "enter" para avançar')
    print(hist_parte1.decisao_acao2)
    resp = input('Responda e tecle "enter" para avançar\n').lower()
    if resp == "a":
        funcoes1.movimentacao()
        dec_a.armario()
        dec_a.decisao_armario()
    elif resp == "w":
        funcoes1.movimentacao()
        dec_w.escrivaninha()
        dec_w.decisao_ecrivaninha()
    elif resp == "s":
        funcoes1.movimentacao()
        dec_s.entulho()
        dec_s.decisao_entulho()
    elif resp == "d":
        dec_d.saindo
        print("Vida:", funcoes1.mostrando_vida())
        input('Tecle "enter" para avançar')
        funcoes1.movimentacao()

#Saiu do quarto:
def  descricao_corredor():
    i = 0
    while True:
        print(hist_parte1.lista_corredor[i])
        funcoes1.mostrando_atributos()
        input('Tecle "enter" para avançar')
        sleep(1)
        i=i+1
        if hist_parte1.lista_corredor[i] == hist_parte1.lista_corredor[-1]:
            print(hist_parte1.lista_corredor[-1])
            break

def explorando_quartos():
    pos = 1
    gameover = False
    while True:
        lista_vida = funcoes1.mostrando_vida()
        if len(lista_vida) == 0:
            print(hist_parte1.gameover)
            gameover = True
            break
        print(f'''
                 ====================================================

                    {hist_parte1.lista_quartos[pos-1]} {hist_parte1.lista_quartos[pos]} {hist_parte1.lista_quartos[pos+1]}

                 ====================================================
        ''')
        sleep(1.25)
        print(hist_parte1.decisao_acao3)
        funcoes1.mostrando_atributos()
        resp = input('Responda e tecle "enter" para avançar\n')
        if resp in hist_parte1.lista_quartos:
            hist_parte1.quartos(resp)
        if resp in 'lL':
            pos = pos+1
        if resp in 'jJ':
            pos = pos-1
        if resp in 'sS':
            print("Saindo")
            funcoes1.movimentacao()
            break
    return gameover
    


