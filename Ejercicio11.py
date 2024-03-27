# Ejercicio 11

# - Se desea escribir un programa que pida al usuario tres números y luego muestre el mayor de
#   ellos. Escribir el programa en papel, realizar 3 pruebas de escritorio y luego pasarlo a Python y
#   verificar los resutlados.

n1 = int(input("Ingrese primer número: "))
n2 = int(input("Ingrese segundo número: "))
n3 = int(input("Ingrese tercer número: "))

if n1 > n2 and n1 > n3:
    print(n1,"es el mayor. (n1)")
elif n2 > n1 and n2 > n3:
    print(n2,"es el mayor. (n2)")
elif n3 > n1 and n3 > n2:
    print(n3,"es el mayor. (n3)")
else:
    print("Los tres numeros son iguales.")