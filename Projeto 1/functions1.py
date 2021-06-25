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


def cadastro_de_dados():
    lista_dados = []
    print(
            '==================== Bem vindo ao cadástro do artísta ===================== \n'
            'Por favor, digite os dados da maneira solicitada. \n')
    while True:
        cogigo = int(input('Insira um código de apenas dígitos numéricos: '))
        nome_artista = input('Insira o nome original do artista: ').capitalize()
        nome_Artistico = input('Insira o nome artístico: ').capitalize()
        aniversario = input('Insira a data de nascimento (dd/mm/aaaa): ')
        while True:
            banda = input('Participa de Banda [S/N]: ').upper()
            if banda in "SN":
                if banda == "S":
                    nome_banda = input('Digite o nome da Banda: ').capitalize()    
                    break
                else:
                    nome_banda = "N"
                    break
            else:
                print("Dado inválido, digite novamente no formato solicitado [S/N].")
        email_artista = input('Insira o email do artísta: ')
        telefone_contato = input('Insira um um telefone para contato (00000-0000): ')
        while True:
            try:
                tipo_trabalho = int(input('Insira o tipo do trabalho do artísta onde: \n 1-Cantor \n 2-Compositor \n 3-ambos\n'))
                if tipo_trabalho in [1, 2, 3]:
                    break
                else:
                    print("Opição não encontrada, por favor escolha uma das alternativas indicadas.")
            except:
                print("Dado inválido, tente novamente na forma solicitada.")
        nome_empresario = input('Insira o Nome do empresário: ')
        email_empresario = input('Insira o e-mail do empresário: ')
        while True:
            try:
                quant_albuns_lancados = int(input('Adicione a quantidade álbuns lançados: '))
                quant_composicoes = int(input('Adcione a quantidade de composições: '))
                valor_min_cache = float(input('Valor Mínimo Cache: R$'))
                break
            except:
                print("Algum dado passado está inválido, por favor insira os dados novamente.")
        cadastro = lista_dados_cadastrados(cogigo, nome_artista, nome_Artistico, aniversario, banda, nome_banda, email_artista, telefone_contato, tipo_trabalho, nome_empresario, email_empresario, quant_albuns_lancados, quant_composicoes, valor_min_cache)
        lista_dados.append(cadastro)
        saida = input("Deseja cadastrar mais alguém?[S/N]").upper()
        if saida in "SN":
            if saida == "N":
                break
        else:
            print("Dado inválido, por favor tente novamente!!")
    return lista_dados

def lista_dados_cadastrados(cogigo, nome_artista, nome_Artistico, aniversario, banda, nome_banda, email_artista, telefone_contato, tipo_trabalho, nome_empresario, email_empresario, quant_albuns_lancados, quant_composicoes, valor_min_cache):
    return [
        "Codigo do artista:   ", cogigo, "\n",
        "Nome Artista:   ", nome_artista, "\n",
        "Nome artistico:   ", nome_Artistico, "\n",
        "Data de aniversario:   ", aniversario, "\n",
        "Faz parte de uma banda:   ", banda, "\n",
        "Nome da banda:   ", nome_banda, "\n",
        "E-mail do artista:   ", email_artista, "\n",
        "Telefone para contato:   ", telefone_contato, "\n",
        "Tipo do trabalho executado [1-Cantor, 2-Compositor, 3-Ambos]: ", tipo_trabalho, "\n",
        "Nome do empresario:   ", nome_empresario, "\n",
        "E-mail do empresario:   ", email_empresario, "\n",
        "Quantidade de albuns lançados:   ", quant_albuns_lancados, "\n",
        "Quantidade de composiçoes:    ", quant_composicoes, "\n",
        "Valor minimo do cache:   ", valor_min_cache, "\n"
    ]
   
