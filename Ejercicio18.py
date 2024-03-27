# Ejercicio 18

# - Una función cuadrática se escribe como a * x ** 2 + b * x + c . La misma puede tener una, dos o ninguna
#   raíz. Escribir un programa que pida al usuario los datos de la misma, es decir, a, b y c, y muestre
#   todas sus raíces, o el mensaje "No tiene raíces" cuando corresponda. Recordar que las raíces están
#   dadas por la fórmula
#   ( -b +- (x**0.5) b ** 2 - 4 * a * c ) / 2 * a | x = Representa la raiz cuadrada
import math

a = int(input("Ingrese el dato de a: "))
b = int(input("Ingrese el dato de b: "))
c = int(input("Ingrese el dato de c: "))
R: float
R1:float 
R2:float

print("f(x) =",a,"x² +",b,"x +",c)

if b**2-4*a*c > 0:
    R1 =( -b + math.sqrt(b**2-4*a*c))/(2*a)
    R2 =( -b - math.sqrt(b**2-4*a*c))/(2*a)
    print("Las raices son",R1," y",R2)
elif b**2-4*a*c < 0:
    print("No tiene raices.")
else:
    R = (-b)/(2*a)
    print("La raiz es",R)