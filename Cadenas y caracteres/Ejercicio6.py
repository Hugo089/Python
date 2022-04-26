#Realizar un programa que dada una cadena de caracteres por caracteres, 
#genere otra cadena resultado de invertir la primera.

cadena = input("Introduzca una cadena de caracteres: ")

longitud = len(cadena) - 1

while (longitud>=0):
    print(cadena[longitud], end = "")
    longitud = longitud - 1


    