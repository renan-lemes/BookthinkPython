''' 
    Teorema de Fermat
    nao ha nenhum numero inteiro possitivo a, b, c tal que 
    a^n + b^n = c^n
    para quaisquer valores de n maiores que 2

'''
    

import math


def check_fermat(a:int , b:int, c:int, n:int):
    if n>2:
        print("Holy smokes")
        c =  (a**n + b**n)**(1/n)
        print(c)
    elif n == 2 :
        c = ((a**n + b**n)**1/n)
        print(c)
    else:
        print("No, that doesn't work")

def input_user():
    a = int(input('Digite o valor de a '))
    b = int(input('Digite o valor de b '))
    c = int(input('Digite o valor de c '))
    n = int(input('Digite o valor de n '))
    return a, b, c, n

a, b, c, n = input_user()
check_fermat(a, b, c, n)
     