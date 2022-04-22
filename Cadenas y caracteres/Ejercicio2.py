#Realizar un programa que comprueba si una cadena leída por teclado comienza
#por una subcadena introducida por teclado.

cadena = input("Dime una cadena: ")
subcadena = input("Dime una subcadena: ")

if (subcadena == cadena [0:len(subcadena)]):
    print("La cadena leída SI comienza por la subcadena")
else:
    print("La cadena leída NO comienza por la subcadena")