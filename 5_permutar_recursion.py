
#program give all permutations of abc

def permutar(lista):
    if len(lista) == 0:
        return []
    elif len(lista) == 1:
        return lista
    else:
        perm = []
        for x in range(len(lista)):
            car = lista[x]
            resto = lista[:x] + lista[x+1:]
            reves = resto[::-1]

            perm.append([car]+resto)
            perm.append([car]+reves)

        return perm

# data
str = 'abc'
lst = list(str)

perm1 = permutar(lst)
print(perm1)