#Programa para obtener iniciales en mayuscula

#Entradas: 
#   Nombre, ingresar el nombre de la persona, 
#   Apellido, Ingresar el apellido de la persona

#Salidas:
#   iniciales, la primera letras del nombre y apellido

#Proceso: Pide el nombre de la persona, extrae la primer letra del nombre y el apellido de la persona e imprimer en mayusculas las iniciales

#Pedir nombre y apellido
nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))

#Tomar la primera letra de cada uno y ponerla en mayuscula
iniciales = nombre[0].upper() + apellido[0].upper()

#Mostrar resultado
print("Tus iniciales son:", iniciales)