#Programa para determinar que tipo de triangulo se ingreso

#Entrada:
#   Lado1: Ingresar el primer lado del triangulo
#   Lado2: Ingresar el segundo lado del triangulo
#   Lado3: Ingresar el tercer lado del triangulo

#Salida
#   Print: Mostrara el tipo de triangulo

#Proceso: se le pedira al usuario que Ingrese los tres lados el triangulo y dependiendo de la cantidad de lados que sean iguales del triangulo determianra de que tipo es.
print("Determinar si un triángulo es equilátero, isósceles o escaleno")

#Se le pide al usuario que ingrese los lados del triangulo
Lado1=int(input("Ingrese el primer lado: "))
Lado2=int(input("Ingrese el segundo lado: "))
Lado3=int(input("Ingrese el tercer lado: "))

#Revision del tipo de triangulo dependiendo de cuantos lados sean iguales y mostrar el resultado
if Lado1==Lado2==Lado3:
    print("Es un triangulo equilatero")
elif Lado1==Lado2 or Lado2==Lado3 or Lado1==Lado3:
    print("Es un triangulo isoseles")
else:
    print("Es un triangulo escaleno")