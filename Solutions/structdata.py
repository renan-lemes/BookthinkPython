## Exercicio 13.8 Analise de markov ✅
from hitogrambook import *

import random

from random import choice
# 1
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
    
    # print(prefix)
    # print(unfix)
    
    return dict_str, prefix, unfix


# read_file('Solutions\\book.txt')


## Parte 2

def frase_aleatoria()->str:
    dc_text ,prefix, sufix = read_file('Solutions\\text.txt')
    
    # print(dc_text)
    _frs = ""
    for i in range(7):
        word = choice(list(dc_text.keys()))
        del dc_text[word]

        num_ram = random.randint(0,2)
        if num_ram == 0 :
            pr = choice(list(prefix))
            del prefix[pr]
            _frs += " " + word+pr +" "
        elif num_ram == 1:
            ix = choice(list(sufix))
            del sufix[ix]
            _frs += " " + word+ix +" "
        else :
            _frs += "" + word +" "
            
    return _frs

    # print(choice(list(dc_text.keys())))




print(frase_aleatoria())