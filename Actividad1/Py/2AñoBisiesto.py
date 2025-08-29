#Programa para determinar si un año es bisiesto

#Entrada:
#   Year: Ingresar el año que se determinara si es bisiesto

#Salida:
# Print que mostrara si el año es bisiesto o no

#Proceso: Pide el año al usuario, lo extrae de la variable y luego dividiendolo entre 4 si el residuo es
# igual a 0 mostrara que el año es bisiesto
print("Determinar año bisiesto")

#Pedir al usuario que ingrese el año
year=int(input("Ingrese un año: "))

#Formula para determinar si el año es bisiesto
if (year % 4==0 and year % 100 != 0) or (year % 400 == 0):
    print("EL año es bisiesto")
else:
    print("El año no es bisiesto")