lst = [1,2,3,4]
tuplalst = (lst, 'Opa')

# print('tupla antes', tuplalst)

tuplalst[0].append(3)

# print(tuplalst)

## scalters como funciona

t = (4,9)
# print(t)
# print(*t)

## exemplo de aplicação ...
# print(divmod(*t))

## Exercicio do livro ✅

def sumall(*args)-> int or float:
    '''
        Função que retorna a soma de qualquer tipo de dados que entrar na função  
    '''
    print(type(*args))
    soma = 0
    t = tuple(*args) or list(*args) or set(*args)

    for i in t:
        print(i)
        soma += i

    return soma

a = sumall((1,2,4,6))

# print(a)

## Bacana uma lista de tuplas pode ser convertido em dict e o mesmo acontece ao contrario