#Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y 
#devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo, 
#“Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use 
#dicha función.

def covertirEspacio (texto):
    subcadena = " "
    for i in texto:
        subcadena = subcadena + i + " "
    
    return subcadena

texto = input ("Introduce un texto: ")
print(covertirEspacio(texto))
