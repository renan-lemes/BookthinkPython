import math

def distance_r2(x1, x2, y1,y2):
    return math.sqrt((x2-x1)**2  +  (y2-y1)**2)

def is_betwenn(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False


print(is_betwenn(1, 1 ,4))
print(distance_r2(2,2,1,3))

