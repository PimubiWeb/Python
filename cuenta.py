#def cuenta


from random import randint


def cuenta(lista):
    #dic vacio
    d = {}

    #recorro la lista
    for x in lista:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
        
    return d

        


lista1 = [randint(1,10) for x in range(100)]

res = cuenta(lista1)

print(res)

#hacer un porcentaje de eso

