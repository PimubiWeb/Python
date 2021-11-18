# game mastermind

#4301
#1234
#coinciden 3
#aciertos 0

#.............

# def function(respuesta->1234,objetivo->4301) return (aciertos->0,coincidencias->3) ¡es una tupla!

#.............

aim = [4,3,0,1]

#resp = [1,3,2,9]
resp = [4,3,0,1]

coin = []
acier = []
for x in range(len(aim)):
    n_aim = aim[x]
    n_resp = resp[x]
    if n_aim == n_resp:
        acier.append(n_aim)

    for i in range(len(resp)):
        n_resp = resp[i]
        if n_aim == n_resp:
            coin.append(n_resp)
    
coincidencias = len(coin) - len(acier)
respuestas = len(acier)


print(coin)
print(acier)
print()
print(coincidencias)
print(respuestas)

# acier = []
# for i in range(len(aim)):
#     n_aim = aim[i]
#     n_resp = resp[i]

#     if n_aim == n_resp:
#         acier.append(n_aim)

# print(acier)

