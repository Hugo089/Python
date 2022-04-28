#Procedimiento que pinte un menú

def pintaMenu():
    print ("1- Ejercicio 1") 
    print ("2- Ejercicio 2") 
    print ("3- Salir") 

def seleccionOpcion():
    pintaMenu()
    opcion = 0
    while (opcion < 1 or opcion > 3):
        opcion =(int) (input("Dime una opción: "))
    return opcion

seleccionOpcion()

print("**** Ejercicios funciones ****")

opc = 0
while (opc != 3):
    opc = seleccionOpcion()
    match opc:
        case 1:
            print("Ejercicio 1")
        case 2:
            print("Ejercicio 2")
        case _:
            print("Vete al carajo")
    
