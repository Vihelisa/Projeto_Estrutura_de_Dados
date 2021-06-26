from dadoscadastrados import *

def menuPrincial():
    print(
        "============= Bem vindo a Visual Studio !! ============= \n\n"
        "Escolha uma das opções abaixo: \n"
        "Tecle '1' para cadastrar um artista \n"
        "Tecle '2' para cadastrar uma música \n"
        "Tecle '3' para cadastrar um álbum \n"
        "Tecle '4' para buscar o artista \n"
        "Tecle '5' para buscar os álbuns de um artista \n"
        "Tecle '6' para editar um perfil cadastrado \n"
        "Tecle '7' para acessar o relatório dos álbuns que ainda serão lançados \n"
        "Tecle '8' para mostrar todos os aniversariantes do mês \n"
        "Tecle '9' para acessar tabela de e-mail dos empresários envolvidos \n"
        "Tecle 'X' para remover um perfil cadastrado\n"
        "Tecle '0' para sair\n\n"
    )
    insira = str (input("Insira aqui sua resposta: "))
    return insira
 
def NomesCodigos(list_dados_cadastrados):
    for dado in list_dados_cadastrados:
        nome = dado['Nome artístico']
        codigo = dado['Código do artista']
        print(codigo, nome)

def buscandoArtista(list_dados_cadastrados):
    NomesCodigos(list_dados_cadastrados)
    cod_art = int (input('Insira o código do teu artista: '))
    erro = False
    print(cod_art)
    for dado in list_dados_cadastrados:
        codigo = dado['Código do artista']
        if codigo == cod_art:
            erro = True
            print(dado) 

    if erro == False:
        print('Código inválido, tente novamente!!')

def CadastrarArtista(list_dados_cadastrados):
    cadastro = {}
    cod_cad = []
    print(
                '==================== Bem vindo ao cadástro do artísta ===================== \n'
                'Por favor, digite os dados da maneira solicitada. \n')
    while True: 
        cadastro.clear() 
        while True:
            cadastro['Código do artista'] = int(input('Insira um código de apenas dígitos numéricos: '))
            for dado in list_dados_cadastrados:
                codigo = dado['Código do artista']
                cod_cad.append(codigo)
            if cadastro['Código do artista'] not in cod_cad:
                break
            else:
                print("Este código é inválido, por favor tente novamente.")
        cadastro['Nome do artista'] = input('Insira o nome original do artista: ').capitalize()
        cadastro['Nome artístico'] = input('Insira o nome artístico: ').capitalize()
        cadastro['Data de aniversário'] = input('Insira a data de nascimento (dd/mm/aaaa): ')
        while True:
            cadastro['Banda'] = input('Participa de Banda [S/N]: ').upper()
            if cadastro['Banda'] in 'SN':
                if cadastro['Banda'] == 'S':
                    cadastro['Nome da banda'] = input('Digite o nome da Banda: ').capitalize()
                break
            else:
                print("Dado inválido, digite novamente no formato solicitado [S/N].")
        cadastro['e-mail'] = input('Insira um e-mail: ')
        cadastro['Telefone'] = input('Insira o telefone (00000-0000): ')
        cadastro['Nome do empresário'] = input('Nome do Empresario: ').capitalize()
        cadastro['e-mail do empresário'] = input('Insira o email do empresário: ')
        while True:
            cadastro['Tipo da trtabalho'] = int(input('Insira o tipo do trabalho do artísta onde: \n 1-Cantor \n 2-Compositor \n 3-ambos\n'))
            if cadastro['Tipo da trtabalho'] in [1, 2, 3]:
                break
            else: 
                print("Dado inválido, tente novamente na forma solicitada.")
        cadastro['Quantidade de álbuns lançados'] = int(input('Adicione a quantidade álbuns lançados: '))
        cadastro['Quantidade de composições'] = int(input('Adcione a quantidade de composições: '))
        cadastro['Valor mínimo do cachê'] = float(input('Valor Mínimo Cache: R$'))
        
        list_dados_cadastrados = DadosCadastrados()
        list_dados_cadastrados.append(cadastro.copy())
        op = str(input('Deseja continuar artistas? [S/N] ')).upper()
        if op == 'N':
            break
    return cadastro