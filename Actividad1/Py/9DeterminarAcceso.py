#Programa para determinar si un usuario tiene acceso ingresando la contraseña

#Entrada
#   Password: Ingresar la contraseña

#Salida:
#   Print: Se mostrara si la contraseña es correcta y si se concedio el acceso

#Proceso: Se le pedira al usuario que ingrese la contraseña y si es correcta se le dara acceso, de no serlo se le negara.
print("Determinar si un usuario tiene permisos de administrador ingresando un código")

#Se le pide al usuario que ingrese la contraseña
Password=str(input("Ingrese su clave: "))

#Se determinara si la contraseña ingresada es correcta y mostrara si se concedio el acceso o no
if Password==("Admin123"):
    print("Acceso concedido")
else:
    print("Acceso denegado")