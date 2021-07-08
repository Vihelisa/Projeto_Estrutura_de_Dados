import os

#Variáveis:
PATH = "Arquivos"
NOME_ARQ = "nome.txt"
VIDA_ARQ = "vida.txt"

def criando_pasta_arquivos():
    if os.path.exists(PATH):
        pass
    else:
        os.mkdir(PATH)

def cria_verifica_arq_nome():
    caminho = os.path.join(PATH, NOME_ARQ)
    if os.path.isfile(caminho):
        pass
    else:
        open(caminho, "w")

def cria_verifica_arq_vida():
    lista_vida = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    caminho = os.path.join(PATH, VIDA_ARQ)
    if os.path.isfile(caminho):
        with open(caminho, "w") as arq :
            for ponto in lista_vida:
                arq.write(str(ponto) + "\n")
    else:
        with open(caminho, "w") as arq :
            for ponto in lista_vida:
                arq.write(str(ponto) + "\n")

    