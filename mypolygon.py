
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

# solução do livro 
def arc(t,r,angle):
    arc_lenght = 2*math.pi*angle/360
    n = int(arc_lenght/3)+1
    step_length = arc_lenght/n
    step_angle = angle/n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def polyline(t, n, lenght, angle):
    for i in range(n):
        t.fd(lenght)
        t.lt(angle)



def arc2(t,r,angle):
    arc_length = 2*math.pi*r*angle/360
    n = int(arc_length/3)+1
    step_length = arc_length/n
    step_angle = float(angle)/n
    polyline(t,n,step_length, step_angle)

def cicle2(t,r):
    arc2(t,r,360)

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
circle(bob, 100, 80, 30)
#arc(bob, 100, 120)
#cicle2(bob, 30)



turtle.mainloop()