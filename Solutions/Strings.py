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
    print(word)
    if word.find('e') == False:
        return True
    else:
        return False
    

def test (fin):
    
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
    
test(fin)