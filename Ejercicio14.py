# Ejercicio 14

# - Escribir un programa que pida al usuario dos enteros y los guarde en dos variables. Si el
#   primero de los valores fuera menor que el segundo, el programa deberá además intercambiar los
#   valores de las variables y mostrarlos de mayor a menor.

a = int(input("Ingrese el primer numero (A): "))
b = int(input("Ingrese el segundo numero (B): "))

if a < b:
    a, b = b, a
    print("A:",a,"B:",b)
else:
    print("A:",a,"B:",b)