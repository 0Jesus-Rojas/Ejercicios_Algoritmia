#Programa para verificar Si un numero es multiplo de 5

#Entrada:
#   Numero: Ingresa un numero

#Salida
#   print: Mostrara si el numero es multiplo de 5

#Proceso: Pide que el user ingrese un numero, lo extrae y dividiendolo por 5 si el residuo es igual a 0 determinara si es multiplo de 5 si el residuo no es 0 se determinara que no es multiplo de 5
print("Determinar si un número es múltiplo de 5")

#Se le pide al user que ingrese el numero
Numero=int(input("Ingrese un numero: "))

#Revision del numero y mostrar el resultado
if Numero%5==0:
    print("El numero es multiplo de 5")
else:
    print("EL numero no es multiplo de 5")