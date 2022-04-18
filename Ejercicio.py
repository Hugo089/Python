import random


intentos = 3
numAdivinar = random.randint(1,10)
numLeer = -1

while (intentos > 0):
    print("Este es el inetneto ", intentos)
    numLeer = (int) (input("Dime un número"))

    if (numLeer < numAdivinar):
        print("El número es mayor")
    elif (numLeer > numAdivinar):
        print("El número es menor")
    else:
        print ("Has acertado")
        break

if (intentos > 0):
    print("Te han sobrado ", intentos, " intentos")
else:
    print("El número que tenías que adivinar era ", numAdivinar)