from Level1 import funcoes1
from Itens import itens

def acao_1w():
     print('''
            Com um movimento um tanto quanto bruco, você faz um rolamento
            qque te deixade pé, mas com isso tudo fira de forma violenta.
''')

def cons_1():
    parag1 = str('''
            Você rápidamente se segura na cama.
            Ela faz um ranger de metal velho e enferrujado muito alto, mas
            continua firme enquanto se apoia para que tudo volte ao normal.
    ''')
    parag2 = str('''
            Com a cabeça no lugar, tudo começa a parar de girar e finalmente 
            você consegue se endireitar e observar, de pé, todo o lugar.
    ''')
    parag3 = str('''
            Então você percebe algo!!
    ''')
    parag4 = str('''
            Percebe que ao menos as suas pernas ainda funcionam.
    ''')
    lista_parag = [parag1, parag2, parag3, parag4]
    return lista_parag

def cons_1_2():
    parag1 = str('''
            Você cai com tudo ao chão.
    ''')
    parag2 = str('''
            Depois de um tempo tentando assimilar o que aconteceu e porque, 
            você consegue finalmente se levantar.
            Agora com mais cuidado consegue visualizar melhor o lugar.
    ''')
    lista_paragr = [parag1, parag2]
    return lista_paragr


def escrivaninha():
     input('Tecle "enter" para avançar')
     print('''
                Você então chega a uma escrivaninha velha e quebrada em várias partes.
                Contudo em meio a buracos e poeira, há uma gaveta que aparentemente resistiu
                ao efeito cruel do tempo.
     ''')
     print("Vida:", funcoes1.mostrando_vida())
     input('Tecle "enter" para avançar')
     print('''
             O QUE VOCÊ FAZ?

             a- Abrir a gaveta
             s- Sair
     ''')
     return 

def decisao_ecrivaninha():
        resp = input('Responda e aperte "enter" para continuar\n')
        if resp == 'a':
                print('''
                        Ao Abrir a gaveta, você leva um susto, pois há coisas que aparentemente não 
                        "deveriam" estar ali.
                ''')
                print("Vida:", funcoes1.mostrando_vida())
                input('Tecle "enter" para avançar')
                itens.achando_faca()
                input('Tecle "enter" para avançar')
                itens.achando_cura_1()
                input('Tecle "enter" para avançar')
                itens.achando_arma_1()
                print('''
                        Após achar e guardar os itens, você finalmente decide sair deste quarto.
                ''')
                funcoes1.movimentacao()
                print("Vida:", funcoes1.mostrando_vida())
                input('Tecle "enter" para avançar')
        elif resp == 's':
                funcoes1.movimentacao()
                print("Você saiu da sala")