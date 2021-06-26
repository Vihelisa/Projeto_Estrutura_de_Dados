def linhas_de_separacao(tam = 50):
    return "=" * tam


def Busca_Artistas(arq):
    print("\n ============ ESCOLHA O SEU ARTÍSTA: ============ \n")
    with open(arq, "rt") as arquivo:
            cont = 0
            for linha in arquivo:
                if "Codigo do artista:   " in linha:
                    codigo = linha
                    print(codigo, end='')
                elif  "Nome artistico:   " in linha:
                    name = linha
                    print(name)
