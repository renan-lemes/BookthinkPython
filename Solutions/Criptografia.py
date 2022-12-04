

letras = 'abcdefghijklmnopqrstuvxwyz'

palavra = 'palavrasenha'

cripto = []

senha = ''

base = 3

#print(letras.find('a'))

for i in range(len(palavra)):

    #if ((letras.find(palavra[i]) + 3) > 25 ):
    cripto.append(letras[letras.find(palavra[i]) + 3])

for i in range(len(cripto)):
    senha += cripto[i]

print(senha)