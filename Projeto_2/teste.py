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