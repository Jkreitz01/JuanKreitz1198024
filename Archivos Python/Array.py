
numeros = []

for i in range(0,10):
  n = float(input(f"Ingrese el número {i + 1}: "))
  numeros.append(n)

suma = 0
numero_mayor = 0

for i in (numeros):
  suma += i
  if i > numero_mayor:
    numero_mayor = i

promedio = suma / 10

print("El promedio de los números ingresados es:", promedio)
print("El número mayor ingresado es:", numero_mayor)