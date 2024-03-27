# Ejercicio 6
# - Escribir en papel un programa que pida al usuario dos números, y que muestre en
#   pantalla al mayor de ambos. Luego hacer 3 corridas de escritorio, luego pasarlo a
#   Python y por último correr el programa con los valores iniciales de las corridas y
#   verificar que funciona como se esperaba.
# - Ídem anterior pero para encontrar el menor

n1 = int(input("Ingrese num 1: "))
n2 = int(input("Ingrese num 2: "))
aux:bool = True
#---------------------------------------

# Imprime el valor mayor.

if n1 > n2:
    print(n1,"es mayor.")
else:
    if n1 < n2:
        print(n2,"es mayor.")
    else:
        print("Ambos son iguales.")
#---------------------------------------

# Imprime el valor menor.

if n1 < n2:
    print(n1,"es menor.")
else:
    if n1 > n2:
        print(n2,"es menor.")
    else:
        print("Ambos son iguales.")
#---------------------------------------

# Intento de codigo de forma NO hardcodeada
        
# if n1 > n2:
#     aux = True
# else:
#     if n1 < n2:
#         aux = False
# if aux == True:
#     print(n1)