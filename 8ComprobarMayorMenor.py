#Programa para determinar si un numero es mayor a 100 o menor a -100

#Entrada
#   Numero: Ingresar el numero a analizar

#salida:
#   Print: Mostrara el numero en que rango esta

#Proceso: Se le pedira al usuario que ingrese un numero, se extraera y dependiendo de si es menor a -100 mayor a mayor a 100 o si esta entre esos dos numeros mostrar el resultado correspondiente
print("Comprobar si un número es mayor a 100 o menor a -100")

#Se le pide al usuario que ingrese el numero
Numero=int(input("Ingrese un numero: "))

#se calculara en que rango esta el numero y mostrara el resulatdo
if Numero >100:
    print("El numero es mayor a 100")
elif Numero < -100:
    print("EL numero es menor a -100")
else:
    print("EL numero esta entre -100 y 100")