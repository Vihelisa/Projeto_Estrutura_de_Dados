from os import read


arq = "Arquivo_teste"
dado = "eu sou a vi"

def Criando_Arquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print("Houve um ERRO ao criar o arquivo!!")
    else:
        print(f"Arquivo {arq} criado com sucesso!!")

def Arquivo_Existe(arq):
    try:
        a = open(arq, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        print("Arquivo já existe!!")
        return True
        
def Adicionando_Info(arq, dado=0):
    try:
        a = open(arq, "at")
    except:
        print("Houve um ERRO na abertura do arquivo!!")
    else:
        try:
            a.write(dado)
        except:
            print("Houve um ERRO na escrita do arquivo")
try:
    Criando_Arquivo(arq)
except:
    Arquivo_Existe(arq)

Adicionando_Info(arq, dado)
with open(arq, "r") as f:
    for linha in f:
        print(type (linha))