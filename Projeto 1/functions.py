import dadoscadastrados

def menuPrincial():
    print(
        "============= Bem vindo a Visual Studio !! ============= \n\n"
        "Escolha uma das opções abaixo: \n"
        "Tecle '1' para cadastras o artista \n"
        "Tecle '2' para cadastrar a música \n"
        "Tecle '3' para cadastrar álbum \n"
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
        nome = dado['Nome artísco']
        codigo = dado['Código do artista']
        print(codigo, nome)

def buscandoArtista(list_dados_cadastrados):
    nome_cod = NomesCodigos(list_dados_cadastrados)
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

            