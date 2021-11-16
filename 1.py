def permute(lista, inicio, final):
    if inicio==final:
        print(''.join(lista))
    else:
        for i in range(inicio,final+1):
            lista[inicio], lista[i] = lista[i], lista[inicio]
            permute(lista, inicio+1, final)
            lista[inicio], lista[i] = lista[i], lista[inicio] # backtrack
 
# Driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
print(permute(a, 0, n-1))
