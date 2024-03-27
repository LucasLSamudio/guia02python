# Ejercicio 3

# - Para cada uno de los siguientes programas indicar qué se imprime cuando se ejecuta

# a)    
a = 10
if a != 0:
    print("perro")
# Este programa imprime "perro" ya que 10 no es igual (!=) a 0, la condición es verdadera.

# b)
a = 10
if a > 0 :
    print("manzana")
else:
    print("naranja")
# Este programa imprime "manzana", ya que la condición es verdadera. (a, que vale 10, es mayor a 0.)
    
# c)
a = 10
if a > 0 :
    print("Te quiero")
    print("bien lejos.")
# Este programa imprime ambos print, la condición es verdadera. (Ambos print están en la condición.)

# d)
a = 5
b = 3
c = 2
if a < b * c :
    print("Hola!")
else:
    print("Chau!")
# Este programa imprime "Hola!" ya que la condición es falsa. (b * c es igual a 6, y 5 es menor a 6.)

# e)
p1 = 3,14
p2 = 3,141569
if p1 == p2 :
    print("p1 y p2 son iguales!")
else:
    print("p1 y p2 no son iguales!")
# Este programa imprime "p1 y p2 no son iguales!" ya que la condición es falsa. (Los valores son distintos.)

# f)
a = "Hola"
b = "hola"
if a == b :
    print("Python es insensible!")
else:
    print("Python es muy sensible!")
# Este programa imprime "Python es muy sensible!" ya que la condición es falsa. (Es key sensitive.)