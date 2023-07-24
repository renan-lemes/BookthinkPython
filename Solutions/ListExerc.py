
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


print(cumsum(t))



