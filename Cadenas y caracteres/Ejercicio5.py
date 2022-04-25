#Si tenemos una cadena con un nombre y apellidos, realizar un programa que 
#muestre las iniciales en mayúsculas.

cadena = input("Introduzca tu nombre y apellidos: ").lower()
contador = 1
print(cadena[0].upper(), end = "")

while (contador < len(cadena)):
    if (cadena[contador] == " "):
        print(" ",cadena[contador + 1].upper(), end = "")
        contador = contador + 1
    else:
        print (cadena[contador], end = "") 

    contador = contador + 1
