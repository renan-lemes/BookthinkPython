
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if first(word) == last(word):
        return True
    else:
        return False



print(middle('de'))
print(middle('d'))
print(middle(''))