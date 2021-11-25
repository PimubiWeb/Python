# game mastermind

#4301
#1234
#coinciden 3
#aciertos 0

#.............
# def function(respuesta->1234,objetivo->4301) return (aciertos->0,coincidencias->3) ¡es una tupla!
#.............

from random import randint

def mastermind(aim,resp):
    coin = 0
    acier = 0
    for x in range(len(aim)):
        n_aim = aim[x]
        n_resp = resp[x]
    
        if n_aim == n_resp:
            acier +=1
        elif n_resp in aim:
                coin += 1

    return coin,acier



# def list_random(name,long):
#     name = []
    
#     for i in range(long):
        



# print(aim)

aim =  [3,1,0,7]
resp = [3,8,2,4]
a = mastermind(aim,resp)

print(a)