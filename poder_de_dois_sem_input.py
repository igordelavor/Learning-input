import math
def poder_de_dois(x):
    n = 1
    while n <= x:
        if x == 1:
            print("Verdadeiro")
            break
        else:
            if n == 1:
                n+=1
            n*2
            if n == x:
                print("Verdadeiro")
                break
            else:
                print("Falso")
                break
poder_de_dois(5)