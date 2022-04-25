#Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio.

caracter = input("Introduzca una letra en minúscula")


#Saber si es VOCAL o NO VOCAL
if caracter := ("a","e","i","o","u"):
    print("El caracter que has introducido es una VOCAL")
else: print("El caracter que has introducido no es una VOCAL")
