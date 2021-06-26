#IMPORTAÇÕES:
from time import sleep
from functions1 import *
from functions_arq import *

#Variáveis Fixas:
arq = "Dados_Cadastrados.txt"


#Abrindo arquivos:
if not Arquivo_Existe(arq):
    Criando_Arquivo(arq)
    
#Apresentando as opções do menu:
while True:
    MenuPrincipal = menuPrincial()
    if MenuPrincipal == "0":
        print("Obrigado pelo acesso!!")
        break
    if MenuPrincipal == "1":
        lista_de_dados = cadastro_de_dados()
        Adicionando_Info(arq, lista_de_dados)
    if MenuPrincipal == "5":
        Busca_Artistas(arq)
        busca = (input('Digite o codigo do artista que quer ver: '))
        lendo_Arquivo(arq, busca)
        sleep(3)
        
                