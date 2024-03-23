print("Semana No. 10: Ejercicio 1")
m = int(input("Ingrese un número de mes "))
mes = ""
match m:
    case 1:
         mes = "Enero"
    case 2:
         mes = "Febrero"
    case 3:
         mes = "Marzo"
    case 4:
         mes = "Abril"
    case 5:
         mes = "Mayo"
    case 6:
         mes = "Junio"
    case 7:
         mes = "Julio"
    case 8:
         mes = "Agosto"
    case 9:
         mes = "Septiembre"
    case 10:
         mes = "Octubre"
    case 11:
         mes = "Noviembre"
    case 12:
         mes = "Diciembre"
    case _:
         print("Error : El número a ingresar debe estar contenido entre 1 y 12")

print("MES:", mes)

print("Semana No. 10: Ejercicio 2")

#Actividad 2
a = int(input("Ingrese un número entero mayor a cero "))
b = int(input("Ingrese otro número entero mayor a cero "))
c = int(input("Ingrese otro número entero mayor a cero "))

if (a <=0 or b <=0 or c <=0):
     print ("Error: El número debe ser enetro y mayor a cero")

print(" El número mayor es")
if (a>b):
     if (a>c):
        print (a)  
     else:
          if (a==c):
               print (a, "y", c)  
          else: 
               print (a)
else:
     if (a==b):
          if (a>c):
               print (a,"y",b)
          else:
               if (a==c):
                    print (a,",", b, "y",c)
               else:
                    print (c)
     else:
          if (b>c):
               print(b)
          else:
               if (b==c):
                    print (b,"y",c)
               else:
                    print (c)



