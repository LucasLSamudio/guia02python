# Ejercicio 8

# - Escribir en papel un programa que tome un número entero positivo ingresado por el usuario
#   y muestre por pantalla "Usted ingresó un número de una sola cifra" o "Usted ingresó un número
#   de más de una cifra" según corresponda. Realizar 4 corridas de escritorio, escribirlo en Python
#   y luego correrlo en la computadora con los valores iniciales de las corridas y verificar que hayan
#   dado como se esperaba.

num = int(input("Ingrese un número mayor a 0: "))

if num > 0 and num < 10:
    print("Usted ingresó un número de una sola cifra.")
else:
    if num >= 10:
        print("Usted ingresó un número de más de una cifra.")
    else:
        print("Usted no ingresó un número válido.")