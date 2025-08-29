#Programar para determinar si un estudiante aprobo o reprobo

#Entrada:
#   Calificacion: Ingresa la calificacion del estudiante

#Salida
#   Print: mostrara el resultado sobre si el estudiante aprobo o reprobo

#Proceso: Pide la calificacion al estudiante, la extrae de la variable y si la calificaion ingresada es igual o mayor a 60 aprobo de lo contrario reprobo
print("Identificar si un estudiante aprobó o reprobó (nota >= 60)")

#Pedir al usuario que ingrese la calificacion
calificacion=float(input("Ingrese su calificacion entre 0 y 100: "))

#Revision de la calificaicon para determinar si aprobo o reprobo
if calificacion >= 60:
    print("Aprobaste")
else:
    print("Reprobaste")
