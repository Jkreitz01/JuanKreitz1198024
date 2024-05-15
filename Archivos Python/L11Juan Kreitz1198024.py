print ("Semana 11 ejercicio 1")

n= int(input("Ingrese un número mayor a 0 "))

# declaración de variables
a=0
b=1
c=0
i=2
resultado= ""

if (n>0):
    resultado= str(a)

    if (n<1):
        resultado += "", str(b)

    while (i < n):
        c= a + b
        resultado += "" + str(c)
        a = b
        b= c
        i = i+1
        
        print(resultado)
    else:
        print(resultado)