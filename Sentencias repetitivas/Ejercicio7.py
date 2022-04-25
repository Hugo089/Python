#Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

numero = (int) (input("Introduzca el número que desees"))
print("La tabla del número introducido es: ")

#Calcular la tabla de multiplicar
for f in range (0,11):
    multiplicacion = 7 * f
    print(f'7 x {f} = {multiplicacion}')

    