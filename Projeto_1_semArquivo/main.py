#Importações:
from functioins import *
from dadoscadastrados import *
from time import sleep

#Variáveis:


#Escolhendo o que fazer através do menu:
while True:
    menuPrincipal = menuPrincial()
    if menuPrincipal == '0':
        break

    elif menuPrincipal == '1':
        list_dados_cadastrados = DadosCadastrados()
        cadastro = CadastrarArtista(list_dados_cadastrados)
        list_dados_cadastrados.append(cadastro)
        print(list_dados_cadastrados)

    elif menuPrincipal == '4':
        while True:
            list_dados_cadastrados = DadosCadastrados()
            busca = buscandoArtista(list_dados_cadastrados)
            sleep(2)
            opcao = input('Deseja procurar mais alguém?(s/n)').upper()
            if opcao == 'N':
                break
    

