
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

####################################################
##             solução do Allen Downey
####################################################


from __future__ import print_function, division


def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.

    letter: single-letter string
    n: int

    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.

    word: string
    n: integer

    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res


if __name__ == '__main__':
    print(rotate_word('cheer', 7))
    print(rotate_word('melon', -10))
    print(rotate_word('sleep', 9))