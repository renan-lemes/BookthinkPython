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
        Função que retorna a soma de qualquer tipo de dados
    '''
    print(type(*args))
    soma = 0
    t = tuple(*args) or list(*args) or set(*args)

    for i in t:
        print(i)
        soma += i

    return soma

# a = sumall((1,2,4,6))

# print(a)

## Bacana uma lista de tuplas pode ser convertido em dict e o mesmo acontece ao contrario

## Exercicio 12.1 ✅ ## precisei da ajuda do autor aqui 

def most_freq(s:str):
    hist = histogram(s)

    t = []
    for x, freq in hist.items():
        t.append((freq,x))

    t.sort(reverse=True)

    res = list()
    for freq,x in t:
        res.append(x)

    return res 


def histogram(s:str)->dict:
    hist = dict()
    for x in s:
        hist[x] = hist.get(x, 0) +1
    
    return hist


def read_file(filename):
    with open(filename, 'r') as arquivo:
        arq = arquivo.read()

    return arq    

words = read_file('Solutions\\words.txt')

# print(words) ## temos todas as palacras do words.txt

# print(histogram(words))
# print(most_freq(words))

## Exericio 13.5 ✅  

def prob_hist(s:dict)->dict:
    total = 0
    prob_d = {}
    total = sum([x[1] for x in s.items()])
    
    for key, value in s.items():
        prob_d[key] = value / total
    return prob_d

print(prob_hist(histogram(['a', 'a', 'b'])))



