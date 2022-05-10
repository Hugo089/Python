#Crea una función “calcularMaxMin” que recibe una arreglo con valores numérico 
#y devuelve el valor máximo y el mínimo. Crea un programa que pida números 
#por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

def calcularMaxMin(vector):
    min = vector[0]
    max = vector[0]
    vminmax=[]
    for i in vector:
        if min>i:
            min = i
        if max<i:
            max = i
    vminmax.append(min)
    vminmax.append(max)
    return vminmax




vector=[]
cant =(int)(input("¿Cuántos números vas a introducir?"))
for i in range (cant):
    numeros = (int)(input("Introduce el número que tu quieras: "))
    vector.append(numeros)

print (calcularMaxMin(vector))


