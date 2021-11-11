"combinacion de todas las posbiles letras"

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def combinacion(word):
    l_word = list(word)
    for w in range(l_word):
        
