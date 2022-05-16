from random import randint, random


import random
import time


def numaleatorio(numero):
    lista = []
    i = 0
    while i<numero:
        lista.append(random.randint(0,10))
        time.sleep(0.5)
        i = i+1
        
    return lista

bandera = True
while bandera == True:
    try:
        numero = (int)(input("Introduce el número que quieras: "))
        print(numaleatorio(numero))
        bandera = False
    except:
        print("Te has equivocado")
    






    
