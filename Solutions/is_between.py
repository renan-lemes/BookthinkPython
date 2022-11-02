
import math

def factorial(n:int):
    if type(n) != int:
        print('Factorial is only definined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result


def distance_r2(x1, x2, y1,y2):
    return math.sqrt((x2-x1)**2  +  (y2-y1)**2)

def is_betwenn(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False

print(factorial(2))
print(is_betwenn(1, 1 ,4))
print(distance_r2(2,2,1,3))

