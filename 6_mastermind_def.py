# game mastermind

#4301
#1234
#coinciden 3
#aciertos 0

#.............

# def function(respuesta->1234,objetivo->4301) return (aciertos->0,coincidencias->3) ¡es una tupla!

#.............
from random import randint






def mastermind(aim, resp):
    aim = [randint(0,9) for x in range(4)]
    coin = []
    acier = []
    for x in range(len(aim)):
        n_aim = aim[x]
        n_resp = resp[x]
        if n_aim == n_resp:
            acier.append(n_aim)

        if n_resp in aim:
            coin.append(n_resp)
    
    coincidencias = len(coin) - len(acier)
    respuestas = len(acier)

    return coincidencias,respuestas


resp = [1,3,2,4]
a = mastermind(resp)

print(a)

