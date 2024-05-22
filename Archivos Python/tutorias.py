n=int(input("Ingrese la cantidad de piezas en el tablero: "))
Tabla = [['-' for _ in range(1,8)] for _ in range(1,8)]
def datos_piezas():
    for i in range(0,n):
        print("1) Rey", "2) Reina", "3) Arfil", "4) Caballo", "5) Peón", sep="\n")
        p=(input("Ingrese el tipo de pieza que desea: "))
        c=(input("¿La pieza será blanco o negro? "))
        if c!='blanco' or c!='negro':
            print("Ingrese un color valido")  
        e=input("Ingrese la columna de ubicación (a-h): ")
        if e=='a':
            col=1
        elif e=='b':
            col=2
        elif e=='c':
            col=3
        elif e=='d':
            col=4
        elif e=='e':
            col=5
        elif e=='f':
            col=6
        elif e=='g':
            col=7
        elif e=='h':
            col=8
        else:
            print("Ingrese una columna valida")
        f=int(input("Ingrese la fila de ubicación (1-8): "))
        if 1>f>8:
            print("ingrese una fila valida")
        Tabla[f][col]=p,c
#Sintaxis
datos_piezas()
#datos de la torre
ct=(input("¿La torre será blanco o negro? "))
if ct!="blanco" or ct!="negro":
    print("Ingrese un color valido")    
et=input("Ingrese la columna de ubicación (a-h): ")
if et=='a':
    colt=1
elif et=='b':
    colt=2
elif et=='c':
    colt=3
elif et=='d':
    colt=4
elif et=='e':
    colt=5
elif et=='f':
    colt=6
elif et=='g':
    colt=7
elif et=='h':
    colt=8
else:
    print("Ingrese una columna valida")
ft=int(input("Ingrese la fila de ubicación (1-8): "))
if 1>ft>8:
    print("ingrese una fila valida: ")
Tabla[ft][colt]="Torre", ct
print(Tabla)