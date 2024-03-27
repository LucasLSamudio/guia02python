# Ejercicio 1

# - Este programa chequea una serie de condiciones para los tres valores ingresados por el usuario.
#   Correrlo tal cual está en Python. Luego reemplazar donde dice True por una expresión lógica
#   que sea True o False según corresponda, en lugar de siempre True como ahora.

# 1.
# Variables: 
a = int(input("Ingrese un numero entero: "))
b = int(input("Ingrese un numero entero: "))
c = int(input("Ingrese un numero entero: "))
p:bool = True
# -----------------------------------------------------
print("Usted ingresó los valores:", a, b, c)
# -----------------------------------------------------
if a > b:
    p = True
else:
    p = False

print(a,"es mayor que",b, p)
print("------------------------------------------")
# -----------------------------------------------------
if a == b:
    p = True
else:
    p = False

print(a, "y", b, "son iguales", p)
print("------------------------------------------")
# -----------------------------------------------------
if a > b and a > c:
    p = True
else:
    p = False

print(a, "es el mayor de todos", p)
print("------------------------------------------")
# -----------------------------------------------------
if b < a and b < c:
    p = True
else:
    p = False

print(b, "es el menor de todos",p)
print("------------------------------------------")
# -----------------------------------------------------
if a > b or a > c:
    p = True
else:
    p = False 

print(a, "es mayor que alguno de los otros dos", p)
print("------------------------------------------")
# -----------------------------------------------------
if a <= b or a <=c:
    p = True
else:
    p = False

print(a, "es menor o igual que alguno de los otros dos", p)
print("------------------------------------------")
# -----------------------------------------------------
if a == b and b == c:
    p = True
else:
    p = False

print("Los tres numeros son iguales", p)
print("------------------------------------------")
# -----------------------------------------------------
if a != b and a != c and b != c:
    p = True
else:
    p = False

print("Los tres numeros son distintos",p)
print("------------------------------------------")
# -----------------------------------------------------
if a % 2 == 0:
    p = True
else:
    p = False

print(a, "es par", p)
print("------------------------------------------")
# -----------------------------------------------------
if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    p = True
else:
    p = False

print("alguno es par", p)
print("------------------------------------------")
# -----------------------------------------------------
if a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
    p = True
else:
    p = False

print("ninguno es par", p)
print("------------------------------------------")
# -----------------------------------------------------
if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    p = True
else:
    p = False

print("todos son pares", p)
print("------------------------------------------")
# -----------------------------------------------------
if a % 3 == 0:
    p = True
else:
    p = False

print(a, "es multiplo de 3", p)
print("------------------------------------------")
# -----------------------------------------------------
if a % 3 == 0 and a % 5 == 0:
    p = True
else:
    p = False

print(a, "es multiplo de 3 y de 5", p)
print("------------------------------------------")
# -----------------------------------------------------
if a % 3 == 0 and a % 2 == 0:
    p = True
else:
    p = False

print(a, "es multiplo de 3 y par", p)
print("------------------------------------------")
# -----------------------------------------------------
if a > b:
    p = True
else:
    p = False

print(a, "-", b, "da un numero positivo", p)
print("------------------------------------------")
# -----------------------------------------------------
if a > b and a % 2 == 0 and b % 2 == 0:
    p = True
else:
    p = False

print(a, "-", b, "da un numero par positivo", p)
print("------------------------------------------")