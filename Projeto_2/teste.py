from Level1 import funcoes1


MOCHILA_ARQ = "mochila.txt"
CINTO_ARQ = "cinto.txt"
PATH = "Arquivos"


lista_Q2_parte1 = ['Q2_p1', 'Q2_p2', 'Q2_p3']


lista_itens_mochila = funcoes1.lendo_mochila_arq()
lista_itens_cinto = funcoes1.lendo_cinto_arq()
if 'Documento cobaia 5152' in lista_itens_cinto or 'Documento cobaia 5152' in lista_itens_mochila:
    print('ACHEI')
else:
    i=0
    while True:
        print(lista_Q2_parte1[i])
        #print(funcoes1.mostrando_atributos())
        input('Tecle "enter" para avançar')
        #sleep(1)
        i=i+1
        if lista_Q2_parte1[i] == lista_Q2_parte1[-1]:
            print(lista_Q2_parte1[-1])
            break

    resp = input('Responda e tecle "enter" para avançar\n').lower()