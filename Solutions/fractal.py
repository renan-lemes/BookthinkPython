import turtle

''' 
def recurse(n, s):
    if n==0:
        print(s)
    else:
        recurse(n-1, s)

recurse(-1, 0) 
Afunção fica em loop infinito por conta de não ter um stop para casos de n < 0

'''


def draw(t, length, n):
    if n == 0 :
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

bob = turtle.Turtle()
draw(bob, 5, 10)

turtle.mainloop()

