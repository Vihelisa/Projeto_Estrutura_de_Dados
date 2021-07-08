import os

#Variáveis:
PATH = "Arquivos"
NOME_ARQ = "nome.txt"

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

    