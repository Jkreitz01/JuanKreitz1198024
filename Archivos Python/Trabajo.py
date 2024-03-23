o = int(input(" Ingrese una opción " '\n' "1. Ver si un número es par o impar" '\n' 
              "2.Indicar si un número es múltiplo de 5" '\n' "3. Devolver una calificación con letras" '\n' 
              "4. Calcular la hipotenusa a partir de dos catetos "))
match o:
    case 1:
        n = int(input(" Ingrese un número "))
        if (n % 2 == 0):
            print("El número es par")
        else:
            print("El número es impar")
    case 2:
        n1 = int(input(" Ingrese un número "))
        if (n1 % 5 == 0):
            print("El número es múltiplo de 5")
        else:
            print("El número NO es múltiplo de 5")
    case 3:
        c = int(input(" Ingrese una calificación "))
        if (c < 50):
            print("F")
        elif (c >= 50 and c>60):
            print("D")
        elif (c >=60 and c<70):
            print("C")
        elif (c >=70 and  c<85):
            print("B")
        elif (c >=85):
            print("A")
    case 4:
         if (2 >= 50 and 2>60):
            print("D")
    case _:
         if (2 >= 50 and 2>60):
            print("D")
