print ("Juan Kreitz - 1198024 \n Diego Barrios- 1061924")

n= int(input("Ingrese un número mayor a 0 "))

ResultadoA=0
ResultadoB= 0
c=0

if (n>0):
    for x in range (1, n+1):
        ResultadoA += (1/x)
    print ("a.", ResultadoA)

    for x in range (1, n+1):
        ResultadoB += ((1/2)**x)
    print ("b.", ResultadoB)

    print("c.")

x1 = int(input("Ingrese el valor de x (número entero): "))
a1 = int(input("Ingrese el valor de a (número entero): "))
n1 = int(input("Ingrese el valor de n (número entero): "))

ResultadoC = 0

for k in range(n1 + 1): 
    ResultadoC += (x1 ** k) * (a1 ** (n1 - k))
print("c.", ResultadoC)
