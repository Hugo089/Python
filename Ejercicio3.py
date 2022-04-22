#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la 
#suma y la media de todos los números introducidos.

#Lista de los números
vNumero = []

numero = (int) (input ("Introduzca un número: "))
if numero !=0:
    vNumero.append(numero)

while numero !=0:
    numero = (int) (input ("Introduzca un número: "))
    if numero !=0:
        vNumero.append(numero)

print ("Has escrito ", len(vNumero), " y los numeros son ", vNumero)

#Suma de los números
suma = 0

for i in vNumero:
    suma = suma + i

print ("La suma de los números es: ", suma)

#Media de los números


print ("La media de los números es: ", suma/len(vNumero))
