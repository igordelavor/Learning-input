import math
def poder_de_dois():
    n = 1
    numero = int(input("Digite um numero: "))
    while n <= numero:
        if numero == 1:
            print("Verdadeiro")
            break
        else:
            if n == 1:
                n+=1
            n = n * 2
            if n == numero:
                print("Verdadeiro")
                break
            if n > numero:
                print("Falso")
                break
poder_de_dois()