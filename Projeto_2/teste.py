import os

PATH = "Arquivos"
MOCHILA_ARQ = "mochila.txt"

def lendo_mochila_arq():
    caminho = os.path.join(PATH, MOCHILA_ARQ)
    lista_itens_mochila = [] 
    with open(caminho, 'r') as arq:
        for linha in arq:
            linha.replace("\n", "")
            lista_itens_mochila.append(linha)
    return lista_itens_mochila

lista_itens_mochila = lendo_mochila_arq()
print(lista_itens_mochila)

for itens in lista_itens_mochila[::-1]:
    print(itens)

escolher = input("Escreva, da forma mostrada na tela, o item que deseja escolher:\n")
print(escolher)

for coisa in lista_itens_mochila[::-1]:
    if escolher in coisa:
        print(coisa)
        break
    else:
        lista_itens_mochila.remove(coisa)
        print(lista_itens_mochila)

print(lista_itens_mochila)