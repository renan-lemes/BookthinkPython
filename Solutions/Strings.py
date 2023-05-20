# Exercicio 9.1 
fin = open('C:\\Users\\RenanLemes\\Desktop\\Projeto_\\BookThinkPython\\Solutions\\words.txt')

# print(fin.readline())

# line = fin.readline()
# print(line.strip())

def read20carct(fin):
    for line in fin :
        if len(line.strip()) > 20 :
            word = line.strip()
            print(word)
        pass

#read20carct(fin)

# Exercicio 9.2

def has_no_e(word):
    if word.find('e') == False:
        return True
    else:
        return False
    


def test (fin):
    tam = len(fin.readlines())
    print(tam)
    value_e = 0
    for line in fin:
        if has_no_e(line.strip()) == True :
            word = line.strip()
            print(word)
            value_e += 1

    porct_e = value_e/tam *100
    porct_n_e = (tam - value_e)/tam *100
    print('porcentagem com E')
    print(porct_e)
    print('porcentagem sem o E')
    print(porct_n_e)    
    
test(fin)