# Exercicio 9.1 
fin = open('C:\\Users\\RenanLemes\\Desktop\\Projeto_\\BookThinkPython\\Solutions\\words.txt')

# print(fin.readline())

# line = fin.readline()
# print(line.strip())

def read20carct (fin):
    for line in fin :
        if len(line.strip()) > 20 :
            word = line.strip()
            print(word)
        pass

#read20carct(fin)

# Exercicio 9.2

def has_no_e (word):
    print(word)
    if word.find('e') == False:
        return True
    else:
        return False
    

def Procent_e (fin):
    
    value_e = 0
    value_n_e = 0
    tam = 0
    for line in fin:
        tam += 1
        # print(line)
        print()
        if (line[line.strip().find('e')]) == 'e' :
            word = line.strip()
            #print(word)
            value_e += 1
        else :
            value_n_e += 1

    porct_e = value_e/tam *100
    porct_n_e = (value_n_e)/tam *100
    print('porcentagem com E')
    print(round(porct_e, 2))
    print('porcentagem sem o E')
    print(round(porct_n_e, 2))    
    
#Procent_e(fin)

# Exercicio 9.3 9.4 e 9.5

palavras_ = []
palavras_not = []
def asvoid (word, letras):
    ''' 
        word : palavra
        letras: serie de letras input
    '''

    for i in letras:
        if word[word.find(i)] == i :
            palavras_.append(word)
        else :
            palavras_not.append(word)


def Exerc_9_3 (fin):
    letras = input("Digite as letras que deseja tirar da lista de palavras: ")
    arrayletras = []
    [arrayletras.append(i) for i in letras] 

    for line in fin : 
        word = line.strip()
        asvoid(word, arrayletras)

#Exerc_9_3 (fin)
#print('palavras com as letras', len(palavras_))
#print('palavras sem as letras', len(palavras_not))

# Exercicio 9.6
'''
    Pegar e retornar se a palavra está em ordem alfabetica ou não 
    
'''

array_txt_n_abc = []


def Exerc_9_6 (palavra):
    alfabeto = 'abcdefghijklmnopqrstuvxwyz'
    arr_most = []
    for l in palavra:
        arr_most.append(alfabeto.find(l))
        
    if all(arr_most[i] <= arr_most[i+1] for i in range(len(arr_most) -1 )) == True:
        print('Esta em ordem alfabetica')
    else:
        print('Não esta em ordem alfabetica')



# palavras exemplos em ordem alfabetica:
# amor, ceu, flor

palavra = input('Digite uma palavra: ')

Exerc_9_6(palavra)