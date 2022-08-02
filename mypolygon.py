
import turtle
import math

bob = turtle.Turtle()

def square(bob, length):
    for i in range(9):
        bob.fd(length)
        bob.lt(length)

def poligon(bob,length, n):
    n = int(360/n)
    for i in range(n):
        bob.fd(length)
        bob.lt(length)        

def circle(bob, length, n, r):
    circumference = 2*math.pi *r
    angle = 360/n 
    length = circumference/n
    for i in range(n):
        bob.fd(length)
        bob.lt(angle)




""" 
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)

bob.fd(100) """

#square(bob, 199)
#poligon(bob, 100, 6)
#circle(bob, 100, 80, 30)




turtle.mainloop()