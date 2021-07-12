from Level1 import funcoes1
from Itens import itens

escolha_gavetas_arm = str('''
               Olhando, você percebe 3 gavetas. O QUE VC FAZ?

               a- Abre a primeira
               w- Abre a segunda
               d- Abre a terceira
               s- Sair
          ''')


escolha_continua = str('''
               Quer olhar outra gaveta?

               a- Abre a primeira
               w- Abre a segunda
               d- Abre a terceira
               s- Sair
          ''')


def acao_1a():
     print('''
               Ao sentar, você sente que tudo gira de forma leve, mas ainda te
               deixa enjoado. Você então coloca as mãos no rosto e esfrega os olhos
               enquanto respira fundo, tentando recobrar a conciencia por completo
               enquanto observa o local.
     ''')


def armario():
     input('Tecle "enter" para avançar')
     print('''
            Ao chegar ao armário consegue-se perceber que ele é bem velho, 
            bem alto, porém estranhamente estreito, bem empoeirado, quebrado
            e com mofo. Há duas portas.
     ''')
     print("Vida:", funcoes1.mostrando_vida())
     input('Tecle "enter" para avançar')
     print('''
             O QUE VOCÊ FAZ?

             a- Abrir a porta
             s- Sair
     ''')
     return 


def decisao_armario():
     resp = input('Responda e aperte "enter" para continuar\n')
     if resp == 'a':
          print('''
               Ao abrir o armário uma das portas se soltam, te dando um susto.
               Por mais velho que este móvel seja, ele é muito mais pesado do que parece, 
               te fazendo soltar a porta que cai com tudo ao chão.
          ''')
          print("Vida:", funcoes1.mostrando_vida())
          input('Tecle "enter" para avançar')
          print(escolha_gavetas_arm)
          print("Vida:", funcoes1.mostrando_vida())
          respost = input('Responda e aperte "enter" para continuar\n').lower()
          escolha_gaveta_arm(respost)
     elif resp == 's':
          funcoes1.movimentacao()
          print("Você saiu da sala")


def escolha_gaveta_arm(respost):
     while True:
          if respost == 'a':
               print('''           Ao abrir a gaveta, não há nada nela.''')
          elif respost == 'w':
               itens.achando_faca()
          elif respost == 'd':
               itens.achando_cura_2()
          elif respost == 's':
               funcoes1.movimentacao()
               print("Você saiu do quarto")
               break
          print(escolha_continua)
          respost = input('Responda e aperte "enter" para continuar\n').lower()

