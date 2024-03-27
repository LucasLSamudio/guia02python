# Ejercicio 9

# - Se tiene la siguiente lista con DNIs de personas.
#       30612453
#       23763290
#       21448503
#       34582048
#       15364857
#   Dado otro número de DNI cualquiera, se desea construir un programa que determine si es alguno
#   de los existentes en el listado. Escribir el programa en papel y luego pasarlo a Python.

# Variables
dniEx1 = 15364857
dniEx2 = 34582048
dniEx3 = 21448503
dniEx4 = 23763290
dniEx5 = 30612453
dniInex = int(input("Ingrese su DNI sin puntos ni comas: "))

if dniInex == dniEx1 or dniInex == dniEx2 or dniInex == dniEx3 or dniInex == dniEx4 or dniInex == dniEx5:
    print("DNI existente en el listado.")
else:
    print("DNI inexistente en el listado.")