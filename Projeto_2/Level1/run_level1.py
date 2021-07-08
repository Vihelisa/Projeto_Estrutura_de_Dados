from time import sleep

from Level1 import hist_parte1, funcoes1, dec_a, dec_d, dec_s, dec_w, mecanica


#história parte 1:
def hist1():
    i = 0
    while True:
        print(hist_parte1.historia_parte1[i])
        troca = input('Tecle "enter" para avançar')
        sleep(1)
        i=i+1
        if hist_parte1.historia_parte1[i] == hist_parte1.historia_parte1[-1]:
            print(hist_parte1.historia_parte1[-1])
            break

def pensamento1():
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
    input('Tecle "enter" para avançar')
    print(hist_parte1.parag10)
    input('Tecle "enter" para avançar')
    
def nome1():
    nome = hist_parte1.quem_e_voce()
    funcoes1.guardando_nome(nome)
    pensa = hist_parte1.pensando_no_nome()
    print(pensa)
    input('Tecle "enter" para avançar')

def movimento_1():
    print(hist_parte1.decisao_acao1)
    resp = input('Responda e tecle "enter" para avançar\n').lower()
    if resp == "a":
        dec_a.acao_1a()
    elif resp == "w":
        dec_w.acao_1w()
        mecanica.mecanica_0()
    elif resp == "s":
        print("""           O que aconteceu comigo?""")
    