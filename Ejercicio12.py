# Ejercicio 12

# - Un profesor clasifica las notas de sus alumnos de la siguiente manera:
#         1-3 Reprobado
#         4-6 Debe rendir examen final
#         7-10 Eximido
#   a) Escribir un programa que indique la clasificación de una nota.
#   b) Escribir un programa que pida 3 notas, calcule el promedio e indique la clasificación
#   del mismo.

n1 = int(input("Ingrese nota 1: "))
n2 = int(input("Ingrese nota 2: "))
n3 = int(input("Ingrese nota 3: "))

prom = ( n1 + n2 + n3 ) / 3

#---------------------------------------------------------
# Nota 1
if n1 <= 3:
    print("Nota 1: Reprobado.")
elif n1 >= 4 and n3 < 7:
    print("Nota 1: Debe rendir examen.")
elif n1 >= 7 and n1 <= 10:
    print("Nota 1: Eximido.")

#---------------------------------------------------------
# Nota 2
if n2 <= 3:
    print("Nota 2: Reprobado.")
elif n2 >= 4 and n2 < 7:
    print("Nota 2: Debe rendir examen.")
elif n2 >= 7 and n2 <= 10:
    print("Nota 2: Eximido.")

#---------------------------------------------------------
# Nota 3
if n3 <= 3:
    print("Nota 3: Reprobado.")
elif n3 >= 4 and n3 < 7:
    print("Nota 3: Debe rendir examen.")
elif n3 >= 7 and n3 <= 10:
    print("Nota 3: Eximido.")

#---------------------------------------------------------
# Promedio
if prom <= 3:
    print("Nota promedio final: Reprobado.")
elif prom >= 4 and n3 < 7:
    print("Nota promedio final: Debe rendir examen.")
elif prom >= 7 and n3 <= 10:
    print("Nota promedio final: Eximido.")