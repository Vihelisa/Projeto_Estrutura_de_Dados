MOCHILA_ARQ = "mochila.txt"
CINTO_ARQ = "cinto.txt"
PATH = "Arquivos"


carac_quartos = {
    "Quarto 1": "       O quarto em que você acordou não parece ter nada de errado ou algo a mais para ver.",
    "Quarto 2": "Este é o quarto 2",
    "Quarto 3": "Este é o quarto 3",
    "Quarto 4": "       Há uma pilha de móveis barrando a passagem e a porta está fechada também, não dá pra passar",
    "Quarto 5": 'quarto_5',
    "Quarto 6": "Este é o quarto 6",
    "Quarto 7": "Este é o quarto 7",
    "Quarto 8": "Este é o quarto 8",
}

resp = input('Diga')
if resp in carac_quartos:
    print(carac_quartos[resp])