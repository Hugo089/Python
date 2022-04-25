#Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.


numero = 0
print("Introduzca un número del 1 al 5")

#Calcular la tabla de multiplicar
while numero != 5:
    numero = numero + 1
    for f in range (0,11):
        print(f, "x", numero, "=", numero*f)
