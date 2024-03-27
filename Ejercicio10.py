# Ejercicio 10

# - Hacer en pseudocodigo y luego un programa que calcule el importe que se le facturará a un
#   cliente por consumo de electricidad sabiendo que la compañía que se la provee cobra una tarifa
#   fija de 480 pesos que incluye los primeros 200 KW consumidos y los KW excedentes se los cobra
#   a 25,5 pesos el KW, además se agregan $78 de impuestos. Se leen los valores del medidor al
#   comienzo y al fin del período.

tarFij = 480
kwBase = 200
imp = 78
tarImp = tarFij + imp

consFinal = int(input("Ingrese kw total consumido: "))

if consFinal > 200:

    precKwExc = ( consFinal - 200 ) * 25.5
    precFinal = tarImp + precKwExc
    
    print("Debe pagar $",precFinal,"por",consFinal,"consumidos.")

else:
    print("Debe pagar $",tarImp,"de precio base.")