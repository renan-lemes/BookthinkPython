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

ls = [1, 2, 4, 2,6,8]
lsList = ls

del ls[0]
print(ls)

del lsList[1:6] ## nunca exclui o ultimo elemento ...
print(lsList)

st = 'spawn'

print(list(st))

def tail (t):
    return t[1:]

print(tail(st))

ls = [4, 5, 12,  1, 0]

ls.sort()
print(ls)

''' 
    t.append(x)
    t = t + [x]
    t += [x]

    Errado !!!!
    t.append([x])
    t = t.append(x)
    t + [x]
    t = t + x

'''
#   sorted() retorna uma lista reordenada 

