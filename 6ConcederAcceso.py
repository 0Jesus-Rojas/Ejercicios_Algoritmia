#Programa para verificar si una cadena ingresada es admin

#Entrada:
#   Usuario: Ingresa su usuario

#salida
#   Print: Mostrara si el acceso es concedido

#proceso: SE le pedira al usuario que ingrese su usuario y dependiendo de lo que ingrese se le dara acceso o se le negara
print("Validar si una cadena ingresada es admin para conceder acceso")

#Se le pide al usuario que ingrese su usuario
usuario=str(input("Ingrese su usuario (admin/user): "))

#Revision del usuario y determinar si se dara acceso o no
if usuario ==("admin"):
    print("Acceso concedido")
else:
    print("Acceso denegado")