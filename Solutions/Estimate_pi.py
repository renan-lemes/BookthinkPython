from math import sqrt as raiz
from math import factorial as fac
from math import pi

def factorial(n):
    """Computes factorial of n recursively."""
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result
    

def estimate_pi():
    """
        Computes an estimate of pi.
        Algorithm due to Srinivasa Ramanujan, from 
        http://en.wikipedia.org/wiki/Pi
    """
    total = 0
    k = 0
    factor = 2 * raiz(2) / 9801
    while True:
        num = factorial(4*k) * (1103 + 26390*k)
        den = factorial(k)**4 * 396**(4*k)
        
        total += num / den
        term = factor * num/den
        
        if abs(term) < 1e-15:
            break
        k += 1
    
    return 1 / (factor * total)


def Estimate_pi():
    solution = float(0)
    k = 0
    s = (2*raiz(2)) / 9801
    while True:
        
        solution +=  s * fac(4*k) * (1103 + 26390*k) / fac(k)**4*396**4*k

        k +=1 
        #if k == 10:
        print(k)
        print(solution)
        #   break  




print(estimate_pi())
print(pi)