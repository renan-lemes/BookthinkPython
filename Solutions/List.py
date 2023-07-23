''' 
    Testando algumas coisas vistas no capitulo
'''

lista_a = ['opa', 'bom', 'test']
lista_b = [1 ,4]
lista_c = []
num = [4, 2, 1, 6]
# num = num.sort()
print('dale' in lista_a)
print('test' in lista_a)

# métodos de listas
lista_b.append(2)

lista_c.extend(lista_a)
lista_c.extend(lista_b)

print(lista_c)
print(num) # erro sera que pode ser por conta do python 2

''' 
    Mapeamento e filtragem de lista
'''


print(sum(num))

def cap_all (t):
    # método isupper verifica se tem letra maiuscula
    res = []
    for i in t:
        res.append(i.capitalize()) # capitalize pega e deixa a primeira letra maiuscula
    return res


t = ['a', 'b', 'c']
x = t.pop(1)

#print(cap_all(lista_a))

print(x)
print(t)


print(lista_a)

lista_a.remove('opa') ## aqui o remove colocamos o value

print(lista_a)


