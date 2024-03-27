# Ejercicio 17

# Escribe un programa que pida los coeficientes de una ecuación de primer grado (ax + b = 0)
# y escriba la solución. Recuerda que una ecuación de primer grado puede no tener solución, tener
# una solución única, o que todos los números reales sean solución.

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

x: float

if a == 0:
    if b == 0:
        print("Tiene infinitas soluciones.")
    else:
        print("No tiene solución.")
else:
    x = -b / a
    print("La solucion de la ecuación es X =",x)