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

# print(circle)

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


# print(rect_in_circle(circle, ret))

## outro exercicio sugerido 

class Time:
    """
        Classe para representar o tempo
    """
    def print_time(self):
        return print(f"{self.hour:2d}:{self.min:2d}:{self.sec:2d}")


time1 = Time()

time1.hour = 12
time1.min = 12
time1.sec = 12

# print(time1.print_time())


time2 = Time()
time2.hour = 15
time2.min = 12
time2.sec = 0

def is_after(t1, t2)->bool :
    
    dif = (t1.hour-t2.hour)*3600 + (t1.min - t2.min)*60 + (t1.sec - t2.sec)  

    return dif>0

# print(is_after(time1, time2))


time3 = Time()

time3.hour = 10
time3.min = 60
time3.sec = 55

## Iria fazer recursivo porem python me limitou 

def increment(time, seconds):
    time.sec += seconds

    if time.sec >= 60 :
        time.sec -= 60
        time.min += 1

    if time.min >= 60:
        time.min -= 60
        time.hour += 1
    
    if time.hour >= 24:
        time.hour -=24
    
    while time.sec >= 60:
        time.min += 1
        time.sec -=60

    while time.min >= 60:
        time.hour += 1
        time.min -=60

    # houras depende por que horas vai até n     
    # while time.hour >= 24:
    #     time.hour =-24

    return time


# t = increment(time3, 120)

# print(f"{t.hour:02d}:{t.min:02d}:{t.sec:02d}")

def time_to_int(time):
    minutes = time.hour *60 + time.min
    seconds = minutes * 60 + time.sec
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.sec = divmod(seconds, 60)
    time.hour, time.min = divmod(minutes, 60)
    return time

def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


## Exercicio 16.1

time_t = Time()
time_t.hour = 2
time_t.min = 54
time_t.sec = 46

num = 4

def mul_time (time, num):
    time2 = Time()

    time2.hour = time.hour * num 
    time2.min = time.min * num
    time2.sec = time.sec * num

    div, time2.sec = divmod(time2.sec, 60)
    min_sum = (div * 60)
    time2.min = time2.min + min_sum
    div, time2.min = divmod(time2.min, 60)
    hour_sum = (div * 60)
    time2.hour = time2.hour + hour_sum

    return time2

time_t = mul_time(time_t, num)

# print(time_t.hour, time_t.min, time_t.sec)

## Exercicio 16.2

from datetime import datetime
from datetime import timedelta

def DataAtual():
    date = datetime.now()
    date = str(date).split(" ")[0]

    return date

# print(DataAtual())

def Years(happy):
    ano = happy.split("-")[0]
    mes = happy.split("-")[1]
    dia = happy.split("-")[2]
    happy = datetime(int(ano), int(mes), int(dia))
    date =  datetime.now() - happy
    
    # periodo = timedelta(days=date.days, hours=date.hours, minutes=date.minutes, seconds=date.seconds, microseconds=date.microseconds)
    anos = date.days / 365.25
    
    return int(anos)

print(Years("1996-11-19"))
