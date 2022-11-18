''' 
    Alguns métodos Matemáticos Interesantes.

'''
x = 2
y = 4
z = 0.4213

b = 2.0

c = complex(x,y)

c_conj = c.conjugate()

mod_d = divmod(x,y)

e = pow(x, y)

e2 = x**y

modl = abs(x)

flo = round(z, 2)

f = z.is_integer() ## verifica se tem um numero inteiro ou não 

print(f)

''' 
    Alguns Métodos de objetos
'''

def P_I(n = 0):
    p_i = 0
    while True:
        p_i += ((-1)**n) / (2*n + 1)
        if n > 900:
            break
        n += 1
    return  4* p_i

print(P_I(n=0))

''' 
    Métoodos de Conjuntos
'''
A = set({1, 2,4})
B = set({1,8,4})

t = A == B

i = A.intersection(B)
u = A.union(B)
d = A.difference(B)
d_ = A.symmetric_difference(B)

print(i)
print(u)
print(d)
print(d_)


''' 
    Alguns Métodos de strings 
'''

