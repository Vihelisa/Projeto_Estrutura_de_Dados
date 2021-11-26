from Level1 import funcoes1
from Itens import itens

parag1 = str('''
            Você olha para o teto, ele parece querer cair. 
            Há uma grande quantidade de mofo e parece estar descascando também.
            No entando a única coisa que você consgue pensar é em descansar 
            um pouco, já sua cabeça parece está prestes a explodir. 
''')
parag2 = str('''
            Depois de um breve momento de descanso, você se sente melhor
            e então cria coragem para se levantar calmamente e explorar o lugar.
''')


def entulho():
    input('Tecle "enter" para avançar')
    print('''
            Você chega ao que parece uma pilha de caixas quebradas, rasgadas, amaçadas, 
            de todos os tipos de formas, tamanhos e materiais. Junto a essas cixas há 
            uma variação enorme de restos de coisas que foram jogadas ao lixo, como
            restos de comida embolorada, luvas, seringas, garrafas e até mesmo fezes velhas.
    ''')
    print("Vida:", funcoes1.mostrando_vida())
    input('Tecle "enter" para avançar')
    print('''
            O cheiro é ainda mais horrível neste canto da sala. Contido algo em meio a todo 
            este lixo chama a tua atenção.
    ''')
    print("Vida:", funcoes1.mostrando_vida())
    input('Tecle "enter" para avançar')
    print('''
            O QUE VOCÊ FAZ?

            a- Mexer no lixo e pegar isso
            s- Sair daí
    ''')
    return 

def decisao_entulho():
        resp = input('Responda e aperte "enter" para continuar\n')
        if resp == 'a':
                print('''
                        Por mais nojento que seja, você decide colocar a mão e pegar o que
                        seja isto, pois pode ser importante para você mais a frente.
                ''')
                print("Vida:", funcoes1.mostrando_vida())
                input('Tecle "enter" para avançar')
                itens.achando_faca()
                input('Tecle "enter" para avançar')
                print('''
                        Pegando a faca, você a limpa nas suas roupas que já estão sujas e 
                        finalmente decide sair deste quarto.
                ''')
                funcoes1.movimentacao()
                print("Vida:", funcoes1.mostrando_vida())
                input('Tecle "enter" para avançar')
        elif resp == 's':
                funcoes1.movimentacao()
                print("Você saiu da sala")