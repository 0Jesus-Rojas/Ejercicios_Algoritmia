#Programa para verificar si una persona puede votar dependiendo de su edad y nacionalidad

#Entradas:
#   Edad: Ingresa la edad del usuario
#   Nacionalidad: Ingresa la nacionalidad de la persona

#Salida:
#   Print: Mostrara el resultado determinando si puede votar o no

#Proceso: Pide la edad y la nacionalidad, la extrae y dependiendo de si es mayor a 17 años y si es colombiano podra votar, de lo contrario no podra
print("Verificar si una persona puede votar (edad >= 18 y nacionalidad = Colombiana)")

#Se le pide al usuario que ingrese su edad y nacionalidad
edad=int(input("Ingrese su edad: "))
nacionalidad=str(input("Ingrese su nacionalidad (Colombiana/Extranjera): "))

#Revision de edad y nacionalidad y mostrar si puede votar o no
if (edad >= 18) & (nacionalidad==("Colombiana")):
    print ("Usted puede votar")
else:
    print("Usted no puede votar")
