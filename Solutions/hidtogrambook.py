import string
import random
''' 
    O codigo faz um histograma com palavra de um livro adicionando um contador para cada palavra falada
    Interesando para modelos NLP. 
'''

def process_line (line:str, hist:dict):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1


def preocess_file (filename:str) -> dict:
    hist = {}
    fp = open(filename)
    for line in fp:
        process_line(line, hist)

    return hist

print(preocess_file('Solutions\\words.txt'))

def most_common(hist):
    t = []
    for key, value in hist.items():
        t.append((value, key))
    t.sort(reverse=True)
    return t

def print_most_common(hist, num = 10):
    t = most_common(hist)
    print('As palavras com mais frequencia sao')
    for freq, word in t[:num]:
        print(word, freq)

def substract (d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

def ramdom_hist (hist:dict) ->list:
    ''' 
        Função para retornar uma lista aleatoria de de palavras em um dicionario 
    '''
    t = []
    for word, freq in hist.items():
        t.extend([word] * freq) ## extend de uma lista é um tipo de concat também 
    return random.choice(t)

