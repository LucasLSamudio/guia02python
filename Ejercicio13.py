# Ejercicio 13

# Escribir un programa que pida al usuario dos enteros y que luego muestre si el primero es
# mayor que el segundo o viceversa.

n1 = int(input("Ingrese primer numero: "))
n2 = int(input("Ingrese segundo numero: "))

if n1 > n2:
    print("El primero es mayor que el segundo.")
elif n2 > n1:
    print("El segundo es mayor que el primero.")
else:
    print("Ambos numeros son iguales.")