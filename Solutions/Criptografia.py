
def rotate_word(palavra, num):
    alfabeto = 'abcdefghijklmnopqrstuvxwyz'
    cripto = list()
    for i in range(len(palavra)):
        if alfabeto.find(palavra[i])+num > len(alfabeto):
            resto = alfabeto.find(palavra[i])+num - len(alfabeto)
            cripto.append(alfabeto[resto])
        else:
            cripto.append(alfabeto[alfabeto.find(palavra[i])+num])
    p = ''
    for k in cripto:
        p += f'{k}'
    
    return p



print(rotate_word('dale', 25))

# palavra = 'palavrasenha'
# #palavra :  


# cripto = []

# senha = ''

# base = 3

# #print(letras.find('a'))

# for i in range(len(palavra)):

#     # if ((letras.find(palavra[i]) + 3) > 25 ):
#     cripto.append(letras[letras.find(palavra[i]) + 3])

# for i in range(len(cripto)):
#     senha += cripto[i]

# print(senha)