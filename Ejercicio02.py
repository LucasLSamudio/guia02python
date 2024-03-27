# Ejercicio 2

# - Un ciudadano argentino está exento de votar en estos casos:
#     .Tiene más de 70 años
#     .Tiene entre 18 y 70 años pero se encuentra a más de 500 km del centro de votación.
#   Suponiendo que las variables edad y distancia representan la edad y la distancia del
#   ciudadano, escribir la expresión lógica que representa esta situación.

print("Este programa está destinado a informar si está exento de votar o no.")
print("-----------------------------------------")

# Variables:

edad = int(input("Ingrese su edad: "))

#--------------------------------------------------------------------------------------------

if edad > 70:
    print("Usted está exento de votar.")
if edad >= 18 and edad <= 70:
    distancia = int(input("Ingrese la distancia a la que está de su centro de votación en kilómetros: "))
    if edad >= 18 and edad <= 70 and distancia > 500:
        print("Usted está exento de votar por estar a más de 500km del centro de votación.")
    else:
        print("Usted debe ir a votar.")
else:
    print("Usted es menor de edad, no puede votar.")