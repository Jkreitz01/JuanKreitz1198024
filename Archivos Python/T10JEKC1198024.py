d = int(input("Ingrese su día de nacimiento "))
m = int(input("Ingrese su mes de nacimiento "))
a = int(input("Ingrese su año de nacimiento "))

match m:
    case 1:
        if (d<=19):
            print("Capricornio")
        else: 
            print("Acuario")
    case 2:
        if (d<=18):
            print("Acuario")
        else: 
            print("Piscis")
    case 3:
        if (d<=20):
            print("Piscis")
        else: 
            print("Aries")
    case 4:
        if (d<=19):
            print("Aries")
        else: 
            print("Tauro")
    case 5:
        if (d<=20):
            print("Tauro")
        else: 
            print("Géminis")
    case 6:
        if (d<=20):
            print("Géminis")
        else: 
            print("Cáncer")
    case 7:
        if (d<=22):
            print("Cáncer")
        else: 
            print("Leo")
    case 8:
        if (d<=22):
            print("Leo")
        else: 
            print("Virgo")
    case 9:
        if (d<=22):
            print("Virgo")
        else: 
            print("Libra")
    case 10:
        if (d<=22):
            print("Libra")
        else: 
            print("Escorpio")
    case 11:
        if (d<=21):
            print("Escorpio")
        else: 
            print("Sagitario")
    case 12:
        if (d<=21):
            print("Sagitario")
        else: 
            print("Capricornio")