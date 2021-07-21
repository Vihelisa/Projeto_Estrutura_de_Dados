import os

# Variáveis:
PATH = "Arquivos"
NOME_ARQ = "nome.txt"
VIDA_ARQ = "vida.txt"
MOCHILA_ARQ = "mochila.txt"
CINTO_ARQ = "cinto.txt"
VIDA_BOSS_ARQ = 'vida_boss.txt'


def removendo_arquivos():
    path = PATH
    if os.path.exists(PATH):
        dir = os.listdir(path)
        for file in dir:
            os.remove('{}/{}'.format(path, file))


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
    lista_vida = ["%", "%", "%", "%", "%", "%", "%", "%", "%", "%"]
    caminho = os.path.join(PATH, VIDA_ARQ)
    if os.path.isfile(caminho):
        with open(caminho, "w") as arq:
            for ponto in lista_vida:
                arq.write(str(ponto) + "\n")
    else:
        with open(caminho, "w") as arq:
            for ponto in lista_vida:
                arq.write(str(ponto) + "\n")


def cria_verifica_arq_mochila():
    caminho = os.path.join(PATH, MOCHILA_ARQ)
    if os.path.isfile(caminho):
        pass
    else:
        open(caminho, "w")


def cria_verifica_arq_cinto():
    caminho = os.path.join(PATH, CINTO_ARQ)
    if os.path.isfile(caminho):
        pass
    else:
        open(caminho, "w")


def cria_verifica_vida_boss():
    caminho = os.path.join(PATH, VIDA_BOSS_ARQ)
    if os.path.isfile(caminho):
        pass
    else:
        open(caminho, "w")
