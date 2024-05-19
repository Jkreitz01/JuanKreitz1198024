#ejercicio 1 Juan Kreitz
matriz = []
for i in range(10):
    arreglo = [] 
    for j in range(10):
        dato = i * j
        arreglo.append(dato)  
    matriz.append(arreglo) 
for i in range(1, 10):
    for j in range(1, 10):
        print(matriz[i][j], end=" ")  
    print() 

#ejercicio 2 Juan Kreitz

import random

m = int(input("Ingrese la cantidad de filas: "))
n = int(input("Ingrese la cantidad de columnas: "))

matriz = []
for i in range(m):
    arreglo = [] 
    for j in range(n):
        dato = random.randint(-20, 20)
        arreglo.append(dato)  
    matriz.append(arreglo) 

print("Matriz original:")
for i in range(m):
    for j in range(n):
        print(matriz[i][j], end=" ")  
    print() 

matriz_traspuesta = []
for j in range(n):
    arreglo = []
    for i in range(m):
        arreglo.append(matriz[i][j])
    matriz_traspuesta.append(arreglo)

print("\nMatriz traspuesta:")
for i in range(n):
    for j in range(m):
        print(matriz_traspuesta[i][j], end=" ")  
    print() 

