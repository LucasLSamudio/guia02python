# Ejercicio 7

# - Escribir en papel un programa que pida al usuario dos números de punto flotante y muestre
#   su promedio. Además, si el promedio es mayor que 7 el programa debe mostrar en pantalla
#   "Aprobado" y si no, debe mostrar "Desaprobado". Después de hacerlo en papel, pasarlo a Python.

n1 = float(input("Ingrese num 1: "))
n2 = float(input("Ingrese num 2: "))

# prom = ( n1 + n2 ) / 2
prom = round(( n1 + n2 ) / 2, 2) # Muestra 2 decimales

print("Su promedio es",prom)
if prom > 7:
    print("Aprobado.")
else:
    print("Desaprobado.")