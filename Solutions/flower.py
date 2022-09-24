

import math 
import turtle

bob = turtle.Turtle()

def petalas3(bob, length, n, angle, larg, rot):
    ''' 
        bob: é o objeto turtle
        Length: tamanho das petalas desenhadas
        n: quantidade de passo pro turtle
        angle: angulo em que o turtle se move
        larg: largura da petala
        rot: rotaçao do turtle
    '''
    for j in range(3):
        bob.lt(angle/2)
        for i in range(n):
            bob.fd(length)
            bob.lt(larg)

        for i in range(n):
            bob.lt(rot)
                #bob.fd(angle/5)
            
        for i in range(n):
            bob.fd(length)
            bob.lt(larg)

def Rotation(bob, n, rot, k):
    ''' 
        bob: é o objeto turtle
        n: quantidade de movimentos
        rot: rotacao do turtle
        k: é a quantidade de vezes que vai ser feito os semi-circulo 
    '''
    if k == 0:
        for i in range(n):
            bob.lt(rot/3)
    if k == 1:
        for i in range(n):
            bob.lt(rot/4)
    if k == 2:
        for i in range(n):
            bob.lt(rot/5)

def flower2(bob, length, n, r):
    ''' 
        bob: é o objeto turtle
        length: tamanho
        n: quantidade de passos do turtle
        r: o raio do semi-circulo
    '''
    circumference = 2*math.pi *r
    angle = 360/n 
    rot = angle/3
    length = circumference/n
    larg = angle/6
    k=0
    while k < 3:
        petalas3(bob, length, n, angle=angle, larg=larg, rot=rot)    
        Rotation(bob, n, rot=rot, k=k)
        k+=1

def flower(bob, length, n, r):
    ''' 
        bob: é o objeto turtle
        length: é o tamanho 
        n: a quantidade de passos do turtle
        r: o raio da esfera
    '''
    circumference = 2*math.pi *r
    angle = 360/n 
    rot = angle/4
    length = circumference/n
    while True:
        for i in range(n):
            bob.fd(length)
            bob.lt(angle/5)

        for i in range(n):
            bob.lt(rot)
            #bob.fd(angle/5)
        
        for i in range(n):
            bob.fd(length)
            bob.lt(angle/5)


flower2(bob, 50, 80, 25)
#flower(bob, 50, 80, 25)



turtle.mainloop()

