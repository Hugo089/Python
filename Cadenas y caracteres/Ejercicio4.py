#Suponiendo que hemos introducido una cadena por teclado que representa una 
#frase (palabras separadas por espacios), realiza un programa que cuente 
#cuantas palabras tiene.

frase = input("Introduce un frase")
contador = 1

for i in frase:
    if i == " ":
        contador = contador +1
    
print ("La frase introducida tiene ", contador, " palabras")


