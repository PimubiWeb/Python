# Python program to print all permutations of a string

def permutar(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    else:
        perm = []
        for i in range(len(lst)):
            car = lst[i]
            resto = lst[:i] + lst[i+1:]
            for p in permutar(resto):
                perm.append([car]+p)
        return perm

#prueba del script
str = "abc"
lst_abc = list(str)
for p in permutar(lst_abc):
    print(p)