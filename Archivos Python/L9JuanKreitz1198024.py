print("Ejercicio 1")
n1= int(input("ingrese el primer número "))
n2= int(input("ingrese el segundo número "))
suma= n1+n2
resta = n1-n2
multi= n1*n2
divReal= n1/n2
divEntera = n1//n2
divMod= n1 % n2
print(n1, "+", n2, "=", suma,)
print(n1, "-", n2, "=", resta,)
print(n1, "*", n2, "=", multi,)
print(n1, "/", n2, "=", divReal,)
print(n1, "//", n2, "=", divEntera,)
print(n1, "%", n2, "=", divMod,)

print("Ejercicio 2")

igualdad = n1 == n2
diferencia = n1 != n2
mayor = n1 > n2
menor = n1 < n2

print(n1, "==", n2, "=", igualdad,)
print(n1, "!=", n2, "=", diferencia,)
print(n1, ">", n2, "=", mayor,)
print(n1, "<", n2, "=", menor,)

print("Ejercicio 3")

a= int(input("ingrese el primer número "))
b= int(input("ingrese el segundo número "))
c= int(input("ingrese el tercer número "))

print("ii", a*b+c)
print("ii", a*(b+c))
print("iii", a/(b+c))
print("iv",(3*a+2*b)/c**2)

print("Actividad, Ejercicio 1")

metros1= int(input("ingrese una cantidad en metros "))

km= metros1/ 1000
milla = km / 1.609 
pie = metros1 * 3.28084
inc= pie * 12
print("km:", km)
print("milla:", milla)
print("pies:", pie)
print("pulgadas:", inc)

print("Actividad, Ejercicio 2")

metros2= float(input("ingrese otra cantidad de metros "))

yd= metros2 // 0.9144
mdyd = metros2 % 0.9144
ft= mdyd // 0.3
mdft = mdyd % 0.3
inch= (mdft / 0.3) * 12

print("yardas:", yd)
print("pies:", ft)
print("pulgadas:", inch)