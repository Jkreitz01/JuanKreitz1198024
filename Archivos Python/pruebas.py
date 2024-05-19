print(" Bienvenido \n Juan Esteban Kreitz Caravantes \n 1198024 \n PROYECTO 2")

# Matriz del Tablero
Tablero = [[["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"]],
           [["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"]],
           [["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"]],
           [["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"]],
           [["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"]],
           [["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"]],
           [["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"]],
           [["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"]]]

# Convertir columna de letra a una posición dentro de la matriz
def convertir_columna(columna):
    match columna:
        case 'a':
            return 0
        case 'b':
            return 1
        case 'c':
            return 2
        case 'd':
            return 3
        case 'e':
            return 4
        case 'f':
            return 5
        case 'g':
            return 6
        case 'h':
            return 7

# Convertir fila de ajedrez a una posición dentro de la matriz
def convertir_fi(fila):
    match fila:
        case 1:
            return 7
        case 2:
            return 6
        case 3:
            return 5
        case 4:
            return 4
        case 5:
            return 3
        case 6:
            return 2
        case 7:
            return 1
        case 8:
            return 0

# Ingresar color de la torre
color_torre = input("Ingrese el color de la torre: ").lower()

# Ingresar la columna de la torre
colTorre = input("Ingrese la columna de la torre: ").lower()

# Convertir la columna de letra a posición dentro de la matriz
ct = convertir_columna(colTorre)

# Ingresar la fila de la torre
filaTorre = int(input("Ingrese la fila de la torre: "))

# Convertir la fila ingresada a posición dentro de la matriz 
ft = convertir_fi(filaTorre)

# Insertar la Torre al tablero
Tablero[ft][ct] = ["Torre", color_torre]

print(f"\n Nombre de pieza: {Tablero[ft][ct][0]}, color {Tablero[ft][ct][1]}")

# Imprimir matriz
for filaTablero in Tablero:
    print(filaTablero)

# Ingreso de más piezas al tablero
while True:
    nombre_pieza = input("Ingrese el nombre de la pieza (o escriba fin para terminar): ")
    if nombre_pieza == 'fin':
        break
    color = input("Ingrese el color de la pieza: ").lower()
    col_pieza = input("Ingrese la columna de la pieza: ").lower()
    fila_pieza = int(input("Ingrese la fila de la pieza: "))

    # Convertir columna y fila de la pieza a una posición dentro de la matriz
    cp = convertir_columna(col_pieza)
    fp = convertir_fi(fila_pieza)

    # Insertar la pieza en el tablero
    Tablero[fp][cp] = [nombre_pieza, color]

    print(f"\n Nombre de pieza: {Tablero[fp][cp][0]}, color {Tablero[fp][cp][1]}")

    # Imprimir matriz
    for filaTablero in Tablero:
        print(filaTablero)

# Movimientos a la derecha
colDerechaInicial = ct + 1
print("\nMovimientos hacia la Derecha: ")
#Verificar si esta en el borde del tablero
if colDerechaInicial >= 8:
    print("Invalido")
else:
    for x in range(colDerechaInicial, 8):
        #verificar si esta vacio el espacio
        if Tablero[ft][x][0] == "v":
            match x:
                case 0:
                    n = 'a'
                case 1:
                    n = 'b'
                case 2:
                    n = 'c'
                case 3:
                    n = 'd'
                case 4:
                    n = 'e'
                case 5:
                    n = 'f'
                case 6:
                    n = 'g'
                case 7:
                    n = 'h'
            print(f"Posición: {n}{filaTorre}, vacío")
            #Verificar si la pieza en el lugar tiene color diferente a la torre
        elif Tablero[ft][x][1] != color_torre:
            match x:
                case 0:
                    n = 'a'
                case 1:
                    n = 'b'
                case 2:
                    n = 'c'
                case 3:
                    n = 'd'
                case 4:
                    n = 'e'
                case 5:
                    n = 'f'
                case 6:
                    n = 'g'
                case 7:
                    n = 'h'
            print(f"Posición: {n}{filaTorre}, con {Tablero[ft][x][0]}{Tablero[x][ct][1]}")
            break
        else:
            print(f"")
            break

# Movimiento hacia la izquierda
colIzquierdaInicial = ct - 1
print("\nMovimientos hacia la Izquierda: ")
#Verificar que no e salga del tablero
if colIzquierdaInicial < 0:
    print("Invalido")
else:
    for x in range(colIzquierdaInicial, -1, -1):
        #Verificar si el espacio esta vacío
        if Tablero[ft][x][0] == "v":
            match x:
                case 0:
                    q = 'a'
                case 1:
                    q = 'b'
                case 2:
                    q = 'c'
                case 3:
                    q = 'd'
                case 4:
                    q = 'e'
                case 5:
                    q = 'f'
                case 6:
                    q = 'g'
                case 7:
                    q = 'h'
            print(f"Posición: {q}{filaTorre}, vacío")
            #Verificar si el color de la pieza es diferente al de la torre
        elif Tablero[ft][x][1] != color_torre:
            match x:
                case 0:
                    q = 'a'
                case 1:
                    q = 'b'
                case 2:
                    q = 'c'
                case 3:
                    q = 'd'
                case 4:
                    q = 'e'
                case 5:
                    q = 'f'
                case 6:
                    q = 'g'
                case 7:
                    q = 'h'
            print(f"Posición: {q}{filaTorre}, con {Tablero[ft][x][0]}{Tablero[x][ct][1]}")
            break
        else:
            print(f"")
            break

# Movimiento hacia arriba
filSuperiorInicial = ft - 1
print("\n Movimientos hacia Arriba: ")
#Verificar que no se salga del tablero
if filSuperiorInicial <= -1:
    print("Invalido")
else:
    for x in range(filSuperiorInicial, -1, -1):
        # Verificar si la casilla está vacía
        if Tablero[x][ct][0] == "v":
            match x:
                case 0:
                    o = 8
                case 1:
                    o = 7
                case 2:
                    o = 6
                case 3:
                    o = 5
                case 4:
                    o = 4
                case 5:
                    o = 3
                case 6:
                    o = 2
                case 7:
                    o = 1
            print(f"Posición: {colTorre}{o}, vacío")
            #Verificar que el color de la pieza sea diferente al de la torre
        elif Tablero[x][ct][1] != color_torre:
            match x:
                case 0:
                    o = 8
                case 1:
                    o = 7
                case 2:
                    o = 6
                case 3:
                    o = 5
                case 4:
                    o = 4
                case 5:
                    o = 3
                case 6:
                    o = 2
                case 7:
                    o = 1
            print(f"Posición: {colTorre}{o}, con {Tablero[x][ct][0]}{Tablero[x][ct][1]}")
            break
        else:
            print(f"")
            break

# Movimiento hacia abajo
filInferiorInicial = ft + 1
print("Movimientos hacia Abajo: ")
#Verificar que no se salga del tablero
if filInferiorInicial >= 8:
    print("Invalido")
else:
    for x in range(filInferiorInicial, 8):
        #Verificar si la casilla está vacía
        if Tablero[x][ct][0] == "v":
            match x:
                case 0:
                    p = 8
                case 1:
                    p = 7
                case 2:
                    p = 6
                case 3:
                    p = 5
                case 4:
                    p = 4
                case 5:
                    p = 3
                case 6:
                    p = 2
                case 7:
                    p = 1
            print(f"Posición: {colTorre}{p}, vacío")
            #Verificar si el color es diferente al de la torre
        elif Tablero[x][ct][1] != color_torre:
            match x:
                case 0:
                    p = 8
                case 1:
                    p = 7
                case 2:
                    p = 6
                case 3:
                    p = 5
                case 4:
                    p = 4
                case 5:
                    p = 3
                case 6:
                    p = 2
                case 7:
                    p = 1
            print(f"Posición: {colTorre}{p}, con {Tablero[x][ct][0]}{Tablero[x][ct][1]}")
            break
        else:
            print(f"")
            break
