from Level2 import hist_parte2, funcoes2
from time import sleep



def hist2():
    i = 0
    while True:
        print(hist_parte2.historia_parte2[i])
        print("Vida:", funcoes2.mostrando_vida())
        input('Tecle "enter" para avançar')
        sleep(1)
        i=i+1
        if hist_parte2.historia_parte2[i] == hist_parte2.historia_parte2[-1]:
            print(hist_parte2.historia_parte2[-1])
            break
