#Importações:
import functions
import dadoscadastrados
from time import sleep
#Variáveis:


#Escolhendo o que fazer através do menu:
while True:
    menuPrincipal = functions.menuPrincial()
    if menuPrincipal == '0':
        break

    elif menuPrincipal == '1':
        list_dados_cadastrados = dadoscadastrados.DadosCadastrados()
        cadastro = functions.CadastrarArtista(list_dados_cadastrados)
        list_dados_cadastrados.append(cadastro)
        print(list_dados_cadastrados)

    elif menuPrincipal == '4':
        while True:
            list_dados_cadastrados = dadoscadastrados.DadosCadastrados()
            busca = functions.buscandoArtista(list_dados_cadastrados)
            sleep(2)
            opcao = input('Deseja procurar mais alguém?(s/n)').upper()
            if opcao == 'N':
                break
    

