## Exercicio 13.8 Analise de markov ✅
from hitogrambook import *

def Markov (dict_txt:dict):
    prefix = {}
    unfix = {}
    for word in dict_txt:
        for idx in range(1, len(word)):
            pre = word[:idx]
            fix = word[-idx:]

            prefix[pre] = prefix.get(pre,0) + 1
            unfix[fix] = unfix.get(fix, 0) + 1
    return prefix, unfix

    
def read_file (name:str)-> dict:
    dict_str =  preocess_file(name)
    prefix, unfix = Markov(dict_str)
    print(prefix)
    print(unfix)


read_file('Solutions\\book.txt')
