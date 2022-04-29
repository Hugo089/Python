#Realizar un programa que compruebe si una cadena contiene una subcadena. 
#Las dos cadenas se introducen por teclado.

cadena = input("Introduzca una cadena: ")
subcadena = input("Introduzca una subcadena: ")

if cadena.find(subcadena)!=-1:
    print("La subcadena esta dentro de la cadena")
else:
    print("La subcadena no esta dentro de la cadena")