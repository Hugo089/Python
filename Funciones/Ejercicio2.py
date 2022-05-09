#Crea un programa que pida dos número enteros al usuario y diga si alguno de
#ellos es múltiplo del otro. Crea una función EsMultiplo que reciba los dos
#números, y devuelve si el primero es múltiplo del segundo.

def nMultiplo (numero1,numero2):
    resto = numero1%numero2
    if resto == 0:
        return True
    else:
        return False

numero1 =int (input("Intrtoduzca el primer número: "))    
numero2 =int (input("Intrtoduzca el segundo número: "))

if (nMultiplo(numero1,numero2) == True):
    print("Es multiplo")
else:
    print("No es multiplo")


