
## Exercicio 10.1 ✅
l = [[1,2], [3], [4,5,6]]

def nested_sum (l:list) -> int: 
    num = 0
    for i in l:
        num += sum(i)
    return num

# print(nested_sum(l))


## Exercicio 10.2 ✅

t  = [1,2,3] ## para tres elesmentos deu certo 
def cumsum (l:list) -> list:
    num = 0
    arr = []
    for i in range(len(l)) :
        num += l[i]
        arr.append(num) 
    return arr


# print(cumsum(t))

## Exercicio 10.3 ✅

def meddle (l:list) ->list :
    del l[0]
    del l[-1]
    return l

# print(meddle([1,2,3,4]))

## Exercicio 10.4 mesma coisa que o exercicio 10.3


## Exercicio 10.5 ✅
def is_sorted (l:list) -> bool:
    if (l == sorted(l)):
        return True
    else :
        return False

# print(is_sorted([1,3,2,4]))



## Exercicio 10.6 ✅

def anagram (palavra1:str , palavra2: str)-> bool:
    l = sorted(palavra1)
    l2 = sorted(palavra2)
    print(l)
    print(l2)

    if l == l2:
        return True
    else :
        return False


# print(anagram('amor', 'roma'))

## Exercicio 10.7 ✅

def has_duplicate(l:list) -> bool:
    
    conj = set() 
    for i in range(len(l)):
        
        if (l[i] in conj):
            return True
        conj.add(l[i])
    
    return False
        
        
arr1 = [1,2,3,4,5]
arr2 = [1,2,4,3,4]

# print(has_duplicate(arr1))
# print(has_duplicate(arr2))

## Exercicio 10.8 paradoxo do aniversario ✅

from random import randint as rand_int
def Paradox_birth(num_pes:int,simulation:int) -> float:
    count_birth = 0 # crio um contador 
    
    for i in range(simulation):
        birth = [rand_int(1,365) for _ in range(num_pes)]  # uma lista com os dias de 23 pessoas com a o dia do aniversario
        # print(birth) # exibo na tela
        if (len(birth) != len(set(birth))): # verifico se existe uma pessoa com o mesmo aniversario usando set
            count_birth += 1 ## contador recebendo +1

    proba = count_birth / simulation
    return proba    
    


# print(Paradox_birth(23, 10))
# Método in pega e pesquisa os elementos em ordem 


