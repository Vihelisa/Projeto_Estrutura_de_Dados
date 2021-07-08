from time import sleep

from Level1 import dec_w


def mecanica_0():
    vai = "v"
    print('''           PENSA RÁPIDO!!''')
    while True:
        print(vai)
        resp = input("Digite as letras sem espaço \n")
        if resp == vai:
            lista_parag = dec_w.cons_1()
            num = 0
            while True:
                print(lista_parag[num])
                troca = input('Tecle "enter" para avançar')
                sleep(1)
                num=num+1
                if lista_parag[num] == lista_parag[-1]:
                    print(lista_parag[-1])
                    break
            
        else:
            print('''
                        =================================
                        =                               =
                        =           BOOM!!!!            =
                        =                               =
                        =================================
            ''')
            lista_paragr = dec_w.cons_1_2()
            numb = 0
            while True:
                print(lista_paragr[numb])
                troca = input('Tecle "enter" para avançar')
                sleep(1)
                numb=numb+1
                if lista_paragr[numb] == lista_paragr[-1]:
                    print(lista_paragr[-1])
                break
            print("           Você tem menos 1 de vida")
        break
            

def mecanica_1():
    segure = ["s", "e", "g", "u", "r", "e"]

    i = 0
    j = 2

    while True:
        print(segure[i])
        resp = input("Digite as letras sem espaço \n")
        print(segure[j])
        respp = input("Digite as letras sem espaço \n")
        if resp == segure[i]:
            pass
        if respp == segure[j]:
            print("ACERTOU")
            break
            
        else:
            print("ERROU")
            i = i+1
            j = j+1