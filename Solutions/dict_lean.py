
palavra = 'hipopotamo'

def histogram(palavra: str)-> dict:
    dc = dict()
    for i in palavra:
        if i not in dc:
            dc[i] = 1
        else:
            dc[i] += 1
    return dc

c = histogram(palavra)


## print(c.get('b',0)) função para pegar o valor da chave


# for i in c:
#     print(i,c[i]) ## chave e valor 
        

## Busca reversa que se trata em achar a chave pelo valor da chave o problema existe que podemos ter duas chaves....
## com isso temos que tomar alguns cuidados mediante ao problema


def reverse_search(d:dict(), key):
    ''' 
        Função para retornar a chave expecifica de um dicionario.
    '''
    for i in d:
        if (d[i] == key):
            return i
    raise LookupError() ## lookuperror é uma classe de error expecifico de para tratar nos loops


def inverse_dict(d:dict)-> dict:
    inverse = dict()
    for i in d:
        val = d[i]
        if val not in inverse :
            inverse[val] = [i]
        else :
            inverse[val].append(i)
    return inverse

# print('histogram', histogram(palavra))
# print('inverse histogram', inverse_dict(histogram(palavra))) ## interesante
 
a = True

print('valor de a antes',a)

def test_global():
    global a 
    a = False

test_global()

# print('valor de a depois',a)


## ------------------------------------------------------------------------------ ##
## Exercicios
# 










