from Level1.funcoes1 import lendo_nome_arq
import os

PATH = "Arquivos"
VIDA_ARQ = "vida.txt"
valor_dano = 2


caminho = os.path.join(PATH, VIDA_ARQ)
with open(caminho, "r") as arq:
    lista_pontos_vida = []
    for ponto in arq:
        ponto = ponto.replace("\n", "")
        lista_pontos_vida.append(ponto)
len_final = len(lista_pontos_vida) - 2
while True:
    lista_pontos_vida.remove('.')
    if len(lista_pontos_vida) == len_final:
        break
print(lista_pontos_vida)

    
'''while remover == valor_dano:
print(lista_pontos_vida)
remover = remover + 1
lista_pontos_vida.remove('.')
print(lista_pontos_vida)
remover = remover+1
lista_pontos_vida'''

