### Exercicio 15.1 ✅
class Point:
    ''' 
        Um ponto 2-D x e y 
    '''
    x = 0
    y = 0
    pass


class Circle:
    center = Point()
    radius = 0

class Rectangle:
    ''' 
        Class Retangle 
    '''
    cod = Point()
    largura = 0
    altura = 0


circle = Circle()

circle.x = 150
circle.y = 100
circle.radius = 75

print(circle)

def point_in_cirlce(cir, p):

    dist = ((p.x - cir.x)**2 + (p.y - cir.y)**2)**(1/2) ## Distancia euclidiana 
    print(dist)
    if (dist <= cir.radius):
        return True
    else :
        return False

p = Point()
p.x = 120
p.y = 100

# print(point_in_cirlce(circle, p))

### Segunda parte

ret = Rectangle()
ret.altura = 76
ret.largura = 100
ret.x = 60
ret.y = 78

def rect_in_circle (cir, rec):

    al_2 = rec.altura/2
    lar_2 = rec.largura/2

    ## calcular todos os vertices onde cada ponto deles se encontram 
    vert = [
        (rec.x - lar_2, rec.y - al_2),
        (rec.x - lar_2, rec.y + al_2),
        (rec.x + lar_2, rec.y - al_2),
        (rec.x + lar_2, rec.y + al_2),
    ]

    for x, y in vert:
        dist = ((cir.x - x)**2 + (cir.y - y)**2 )**(1/2) ## distancia em relação ao circulo
        if (dist <= cir.radius):
            return True
        else :
            return False


print(rect_in_circle(circle, ret))