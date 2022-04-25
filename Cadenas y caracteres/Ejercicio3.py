#Pide una cadena y un carácter por teclado (valida que sea un carácter) y 
#muestra cuantas veces aparece el carácter en la cadena.

cadena = input("Dime una cadena: ")
cont = 0

caracter = input("Dime un caracter: ").upper()
caracter = ord(caracter)


if (caracter >= 65 and caracter <= 90):
    print("Es un caracter válido")
    for aux in cadena:
        if (ord(aux.upper()) == caracter):
            cont = cont + 1

print("El carcter se repite: ",cont, " veces")