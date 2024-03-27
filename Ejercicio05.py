# Ejercicio 5

# - Escribir en papel un programa que pida una nota y que en el caso de que sea menor a cuatro
# muestre "Debe recuperar". Luego pasarlo a Python.

nota = int(input("Por favor, ingrese una nota: "))

if nota < 4:
    print("Debe recuperar.")
else:
    print("No debe recuperar.")