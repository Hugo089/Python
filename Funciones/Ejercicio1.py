#Crea un procedimiento EscribirCentrado, que reciba como parámetro un texto y
#lo escriba centrado en pantalla (suponiendo una anchura de 80 columnas; pista:
#deberás escribir 40 - longitud/2 espacios antes del texto). Además subraya el
#mensaje utilizando el carácter =.

def escribirCentrado(texto):
    mitad =(int) (110-(len(texto)/2))
    textoCentrado = " "
    for i in range(0,mitad):
        textoCentrado = textoCentrado + " "
    print(textoCentrado + texto)


texto = input("Introduce un texto: ")
escribirCentrado(texto)
