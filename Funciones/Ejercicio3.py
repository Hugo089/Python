#Crear una función que calcule la temperatura media de un día a partir de la
#temperatura máxima y mínima. Crear un programa principal, que utilizando la
#función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y
#vaya mostrando la media. El programa pedirá el número de días que se van a
#introducir.

def temperatura (tmaxima,tminima):
    total = (tmaxima + tminima)/2
    return total

    





ndias = input ("Introduzca el número de días: ")
tmaxima = int (input ("Introduzca la temperatura máxima: "))
tminima = int (input ("Introduzca la temperatura mínima: "))
print (temperatura(tmaxima,tminima))