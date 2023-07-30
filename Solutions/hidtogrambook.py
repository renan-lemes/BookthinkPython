import string

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