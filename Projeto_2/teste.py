from time import time
from typing import List
from time import sleep

lista_movimento = ['_','_','_','_','_','_','_','_','_','&']


print(lista_movimento)
paco = input('Aperte "enter" para andar')
while '&' not in lista_movimento[0]:
    lista_movimento.append('_')
    lista_movimento.pop(0)
    print(lista_movimento)
    paco = input('')