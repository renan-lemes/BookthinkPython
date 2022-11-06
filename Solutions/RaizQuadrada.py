from math import sqrt as raiz 

def RaizQuadrada(x, a):
    epsilon = 0.0000001
    while True:
        y = (x + a/x) / 2           # y-x é epsilon donde vem o X^2 -2xepsilon + epsilon^2
        if abs(y - x) < epsilon :
            return(x)
            break
        x = y

def RaizCorreta(a):
    return(raiz(a))  

def test_square_root():
    
    for i in range(1,9):
        r = RaizQuadrada(1, i)
        r_real = RaizCorreta(i)
        dif = abs(r - r_real)
        print('      mysqrt(a) ------------------- math.sqrt(a) ------------------- diff')
        print(f'      {r} | {r_real} | {dif}')

test_square_root()
#print(RaizQuadrada(20, 4))
#print(raiz(4))