#Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100.
#A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,
#a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta 
#el número (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado.



import random
numero= (random.randint(0,100))
num = -1
intentos = 10

#Número aleatorio
while num != numero:
    num=(int(input("Me puedes decir un número entre el 0 y el 100")))

    if (num < numero):
        print("El número es mayor")
        intentos = intentos + 1
    if (num > numero):
        print("El número es menor")
        intentos = intentos + 1
    if (num == numero):
        break


if (num == numero):
    intentos = str(intentos)
    print("El número lo has adivinado en", intentos, "intentos")

if (num != numero):
    numero = str(numero)
    print("El número era ", numero)