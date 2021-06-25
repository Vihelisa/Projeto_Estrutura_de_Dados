from functions_secundarias import *

def Criando_Arquivo(arq):
    try:
        a = open(arq, 'wt')
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
        
def Adicionando_Info(arq, lista_de_dados):
    linha_sep = linhas_de_separacao()
    try:
        with open(arq, "a") as a:
            for lista in lista_de_dados:
                for dados in lista:
                    a.write(str(dados))
                a.write(linha_sep)
                a.write("\n")
    except:
        print("Houve um ERRO na escrita do arquivo")


def lendo_Arquivo(arq, busca):
    try:
       with open(arq, "rt") as arquivo:
            print("\n")
            cont = 0
            for linha in arquivo:
                if busca in linha:
                    for c in range (cont, cont + 13):
                        print(arquivo.readline())
                    cont += 1
    except:
        print("Houve um erro na leitura do arquivo!")