#Programa para determinar si un numero es par

#Entrada:
#   Numero1 : Ingresar el numero que se determinara si es par

#Salida:
#   Print con el resultado que dara el algoritmo

#Proceso: PIde el numero al usuario, lo extrae de la variable dividiendo el numero entre 2 si el 
#   residuo es igual a 0 determinara que es par si el residuo es superior a 0 sera impar

#Pedir al usuario que ingrese un numero
print("Determinar si un número es negativo")

#Determinar si el numero es par o impar y dar el resutado
Numero1=int(input("Ingrese el primer numero: "))
if Numero1 % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")