#Actividad 01
print("Semana No. 12: Ejercicio 1")

import math

def ObtenerAreaTriangulo(base, altura):
    return (base * altura) / 2

def ObtenerAreaCuadrado(lado):
    return lado ** 2

def ObtenerAreaRectangulo(base, altura):
    return base * altura

def ObtenerAreaCirculo(radio):
    return math.pi * radio ** 2

print("Seleccione la opción que desea calcular:")
print("a. Área de triángulo")
print("b. Área de cuadrado")
print("c. Área de rectángulo")
print("d. Área de círculo")

option = input("Ingrese la letra correspondiente a la opción: ")

match option:
    case 'a':
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = ObtenerAreaTriangulo(base, altura)
    case 'b':
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = ObtenerAreaCuadrado(lado)
    case 'c':
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = ObtenerAreaRectangulo(base, altura)
    case 'd':
        radio = float(input("Ingrese el radio del círculo: "))
        area = ObtenerAreaCirculo(radio)
    case _:  
        print("Opción no válida")
        exit()

print(f"El área es:" , area)  

#Actividad 02

print("Semana No. 12: Ejercicio 1")

x = 0 
y = 0

def MoverPosicion(cantX, cantY):
    global x, y 
    x += cantX
    y += cantY

opcion = 'a'
while(opcion != 'e'):
    print("Menú")
    print("a. Sube","b. Baja","c. Izquierda","d. Derecha", "e. Salir", sep = "\t\n")
    opcion = input("ingrese su opción: ")

    match opcion:
        case 'a': #opción sube
            MoverPosicion(0,1) #para cada opción se manda a llamar la función creada anteriormente
        case 'b': #opción baja
            MoverPosicion(0,-1)
        case 'c':
            MoverPosicion(-1,0)
        case 'd':
            MoverPosicion(1,0)

    print(f"La poscición actual es: [{x}][{y}]")
