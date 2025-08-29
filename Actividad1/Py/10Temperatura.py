#Programa para determinar si la temperatura es adecuada para la congelacion

#Entrada
#   temperatura: Ingresar la temperatura

#Salida:
#   Print: Se le mostrara al usuario si la temperatura es adecuada para la congelacion

#Proceso: se le pedira al usuario que ingrese la temperatura, se extraera y dependiendo de la temperatura ingresada se mostrara si es adecuada o no para la congelacion
print("Verificar si la temperatura ingresada es adecuada para congelación (<= 0°C)")

#Se le pide al usuario que ingrese la temperatura
temperatura=int(input("Ingrese la temperatura"))

#Se calculara si la temperatura es adecuada para la congelacion y se mostrara el resultado
if temperatura <=0:
    print("La temperatura es adecuada para la congelacion")
else:
    print("La temperatura no es adecuada para la congelacion")