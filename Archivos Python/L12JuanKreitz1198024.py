print ("Semana 12 ejercicio 1")

print (" a. Sumatoria \n b. Factorial \n c. Tablas de Multiplicar \n d. Número Perfecto")

o= str(input("Ingrese una opción: "))

match o:
    case "a":
        print ("Sumatoria")
        n = int(input("Ingrese un número entero mayor a cero: "))
        if (n >= 0):
            s= 0
            i=1
            while (i <= n):
                s= i + s
                i = i+1
            print ("La sumatoria es: ", s)        
        else:
            print ("ERROR: Ingrese un número válido mayor a cero")

    case "b":
        print ("Factorial")
        n = int(input("Ingrese un número entero mayor a cero: "))
        if (n >= 0):
            f= 1
            i=1
            while (i <= n):
                f= i * f
                i = i+1
            print ("El factorial es: ", f)        
        else:
            print ("ERROR: Ingrese un número válido mayor a cero")
    case "c":
        print ("Tablas de Multiplicar")
        tituloColumnas = "\t"
        for i in range(1, 11):
            tituloColumnas = tituloColumnas + str(i) + "\t"
        print (tituloColumnas, "\n")

        for n in range(1, 11):
            fila = str(n) + "\t"
            for c in range (1,11):
                fila = fila + str(n * c) + "\t"
            print (fila , "\n")
    case "d":
        print ("Número Perfecto")
        n = int(input("Ingrese un número entero mayor a cero: "))
        f = 0
        for i in range(1, n):
            if (n % i == 0):
                f = i + f
        if (f == n):
            print (n, "Sí es un número perfecto")
        else:
            print (n, "No es un número perfecto")

    case _:
        print ("Elija una opción válida")
        
