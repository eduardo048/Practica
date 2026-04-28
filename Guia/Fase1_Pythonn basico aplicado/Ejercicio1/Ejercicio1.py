#1. Crear una funcion que reciba dos numeros y devuelva suma, resta, multiplicacion y division.

def operaciones_basicas(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2

    if num2 != 0:
        division = num1 / num2
    else:
        division = 0
    
    return suma, resta, multiplicacion, division

#Ejemplo de uso
num1 = int(input("Ingrese el primer numero:"))
num2 = int(input("Ingrese el segundo numero:"))

resultados = operaciones_basicas(num1, num2)
for operacion, resultado in zip(["Suma", "Resta", "Multiplicacion", "Division"], resultados): #zip es una función que permite iterar sobre dos o 
                                                                                                #más secuencias al mismo tiempo, en este caso, la lista de operaciones
                                                                                                #y la lista de resultados.
    print(f"{operacion}: {resultado}")
    


