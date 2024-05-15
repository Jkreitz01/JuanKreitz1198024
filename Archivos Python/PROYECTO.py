print ("Bienvenido al programa!")
print ("Datos generales (Campos OBLIGATORIOS) ")
nombre= str(input("Nombre Completo: "))
edad = str(input("Escribe tu edad: "))
print ("¿Cuál es tu color favorito? \n")
print ("1. Café \n")
print ("2. Anaranjado \n")
print ("3. Amarillo \n")
print ("4. Azul \n")
print ("5. Verde \n")
color = int (input("Elige el color mediante el número: "))

import turtle
turtle.pendown()
turtle.teleport(-300,170)
for x in range(0, 2):
    turtle.forward(600)
    turtle.left(-90)
    for x in range (2,3):
        turtle.forward(300)
        turtle.left(-90)
turtle.penup()
turtle.forward(135)  
turtle.left(-90)
turtle.forward(50)
turtle.color("brown")  
turtle.write("BIENVENIDO "+ nombre + "!!!", font=("Arial", 20, "bold"))
turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
turtle.write("Edad: " + edad, font=("Arial", 12))
turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
turtle.write("Que empiece el cuento :D. Presione espacio", font=("Arial", 12))  
turtle.hideturtle()

def cambiar_escena_inicio():
    turtle.write("", align="center", font=("Arial", 14, "bold"))

    numero_escena = turtle.textinput("AVISOOOOO!", "Desea iniciar? Presione 00")

    try:
        numero_escena = int (numero_escena) 
        print(f"Cambiando a la escena...")  
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")

    if (numero_escena==00):
        escena= int(turtle.textinput("Coloque la escena a la que quiere trasladarse","5 escenas disponibles, 6 salir"))
        match (escena):
            case 1:
                turtle.pendown()
                turtle.setheading(-90)
                turtle.clear()
                turtle.color("black")
                turtle.teleport(-300,250)
                for x in range(0, 2):
                    turtle.forward(50)
                    turtle.left(-90)
                    for x in range (2,3):
                        turtle.forward(-600)
                        turtle.left(-90)
                turtle.penup()
                turtle.forward(50)  
                turtle.left(90)
                turtle.forward(50)  
                turtle.write("Titulo escena 1: El Comienzo", font=("Arial", 16, "bold"))
                turtle.hideturtle()

                turtle.pendown()
                turtle.teleport(300,-250)
                for x in range(0, 2):
                    turtle.forward(-600)
                    turtle.left(90)
                    for x in range (2,3):
                        turtle.forward(100)
                        turtle.left(90)
                turtle.penup()
                turtle.forward(-590)  
                turtle.left(-90)
                turtle.forward(-65)  
                turtle.write("En un bosque muy lejano llamado Bosque Encantado, vivía una ardilla traviesa llama-", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
                turtle.write("da Cuki. Cuki era conocida por su curiosidad y su amor por las aventuras. Un día, ", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
                turtle.write("mientras saltaba de rama en rama, encontró un mapa antiguo entre las hojas secas.", font=("Arial", 12))  
                turtle.hideturtle()

                turtle.pendown()
                turtle.teleport (-300, 200)
                for x in range(0, 2):
                    turtle.forward(350)
                    turtle.left(-90)
                    for x in range (2,3):
                        turtle.forward(-600)
                        turtle.left(-90)

                for x in range(1,2):


                    def dibujar_ardilla():
                        #cabeza Cuki
                        def dibujar_circulo():
                            turtle.penup()
                            turtle.goto(-15, 15)
                            turtle.pendown()
                            turtle.color("brown")
                            turtle.begin_fill()
                            turtle.circle(20)
                            turtle.end_fill()

                        dibujar_circulo()

                            #orejas Cuki
                        def dibujar_ore():
                            turtle.penup()
                            turtle.goto(-15, 35)
                            turtle.pendown()
                            turtle.color("brown")
                            turtle.begin_fill()
                            turtle.circle(5)
                            turtle.end_fill()

                        dibujar_ore()

                        #Ojo Cuki
                        def dibujar_ojo():
                            turtle.penup()
                            turtle.goto(10, 10)
                            turtle.pendown()
                            turtle.color("black")
                            turtle.begin_fill()
                            turtle.circle(5)
                            turtle.end_fill()

                        dibujar_ojo()

                        #cuerpo Cuki
                        def dibujar_rectangulo():
                            turtle.goto(-12.5, -10)
                            turtle.color("brown")
                            turtle.begin_fill()
                            for _ in range(2):
                                turtle.forward(45)
                                turtle.left(90)
                                turtle.forward(25)
                                turtle.left(90)
                            turtle.end_fill()

                        dibujar_rectangulo()

                        #patas Cuki
                        def dibujar_rectangulo2():
                            turtle.goto(-12.5, -45)
                            turtle.color("brown")
                            turtle.begin_fill()
                            for _ in range(2):
                                turtle.forward(10)
                                turtle.left(90)
                                turtle.forward(35)
                                turtle.left(90)
                            turtle.end_fill()

                        dibujar_rectangulo2()

                        #garras Cuki
                        def dibujar_rectangulo2():
                            turtle.goto(-12.5, -15)
                            turtle.color("brown")
                            turtle.begin_fill()
                            for _ in range(2):
                                turtle.forward(10)
                                turtle.left(90)
                                turtle.forward(35)
                                turtle.left(90)
                            turtle.end_fill()

                        dibujar_rectangulo2()

                        #cola
                        def dibujar_triangulo():
                            lado = 30

                            turtle.penup()
                            turtle.goto(-12.5, -45)
                            turtle.pendown()
                            turtle.setheading(-250)
                            turtle.color("brown")  
                            turtle.begin_fill()
                            turtle.forward(lado)
                            turtle.left(120)
                            turtle.forward(lado)
                            turtle.left(120)
                            turtle.forward(lado)
                            turtle.end_fill() 

                        dibujar_triangulo()
                    dibujar_ardilla()

                    def dibujar_grama():
                        turtle.goto(-300, -80) 
                        turtle.color("green")
                        turtle.setheading(0)
                        turtle.begin_fill()
                        for _ in range(2):
                            turtle.forward(600)
                            turtle.left(90)
                            turtle.forward(20)
                            turtle.left(90)
                        turtle.end_fill()
                    dibujar_grama ()

                    def dibujar_arbol():
                        #tronco
                        def dibujar_tronco():
                            turtle.goto(150, -70)  #
                            turtle.color("brown")
                            turtle.setheading(0)
                            turtle.begin_fill()
                            for _ in range(2):
                                turtle.forward(30)
                                turtle.left(90)
                                turtle.forward(100)
                                turtle.left(90)
                            turtle.end_fill()
                        dibujar_tronco()

                        #hojas
                        def dibujar_hojas():
                            turtle.penup()
                            turtle.goto(170, 25)
                            turtle.pendown()
                            turtle.color("green")
                            turtle.begin_fill()
                            turtle.circle(75)
                            turtle.end_fill()
                        dibujar_hojas()

                    dibujar_arbol()

                turtle.penup()
                turtle.goto(turtle.xcor(), turtle.ycor() - 475)
                turtle.write("Si quiere cambiar de escena presione la tecla espacio", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)

                def activar_cambio_escena1():
                    turtle.onkey(cambiar_escena, "space") 

                turtle.listen()
                activar_cambio_escena1()
                turtle.mainloop()
                cambiar_escena()

                def cambiar_escena():
                    turtle.write("", align="center", font=("Arial", 14, "bold"))

                numero_escena = turtle.textinput("AVISOOOOO!", "Desea Cambiar de escena? Presione 6")

                try:
                    numero_escena = int (numero_escena) 
                    print(f"Cambiando a la escena...")  
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido.")

            case 3:
                turtle.clear()
                turtle.pendown()
                turtle.color("black")
                turtle.setheading(270)
                turtle.teleport(-300,250)
                for x in range(0, 2):
                    turtle.forward(50)
                    turtle.left(-90)
                    for x in range (2,3):
                        turtle.forward(-600)
                        turtle.left(-90)
                turtle.penup()
                turtle.forward(50)  
                turtle.left(90)
                turtle.forward(50)  
                turtle.write("Titulo escena 3: El Desafío de la Cueva", font=("Arial", 16, "bold"))
                turtle.hideturtle()

                turtle.pendown()
                turtle.teleport(300,-250)
                for x in range(0, 2):
                    turtle.forward(-600)
                    turtle.left(90)
                    for x in range (2,3):
                        turtle.forward(100)
                        turtle.left(90)
                turtle.penup()
                turtle.forward(-590)  
                turtle.left(-90)
                turtle.forward(-65)  
                turtle.write("Dentro de la cueva, Cuki se encontró con un guardián sorpresa: un búho sabio llamado", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
                turtle.write("Don Hoot. Para obtener el tesoro, Don Hoot le propuso a Cuki resolver un acertijo.", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
                turtle.write("Cuki, con su ingenio, respondió correctamente y ganó la admiración del búho.", font=("Arial", 12))  
                turtle.hideturtle()

                turtle.pendown()
                turtle.teleport (-300, 200)
                for x in range(0, 2):
                    turtle.forward(350)
                    turtle.left(-90)
                    for x in range (2,3):
                        turtle.forward(-600)
                        turtle.left(-90)

                def dibujar_ardilla():
                        #cabeza Cuki
                        def dibujar_circulo():
                            turtle.penup()
                            turtle.goto(-15, 15)
                            turtle.pendown()
                            turtle.color("brown")
                            turtle.begin_fill()
                            turtle.circle(20)
                            turtle.end_fill()

                        dibujar_circulo()

                            #orejas Cuki
                        def dibujar_ore():
                            turtle.penup()
                            turtle.goto(-15, 35)
                            turtle.pendown()
                            turtle.color("brown")
                            turtle.begin_fill()
                            turtle.circle(5)
                            turtle.end_fill()

                        dibujar_ore()

                        #Ojo Cuki
                        def dibujar_ojo():
                            turtle.penup()
                            turtle.goto(10, 10)
                            turtle.pendown()
                            turtle.color("black")
                            turtle.begin_fill()
                            turtle.circle(5)
                            turtle.end_fill()

                        dibujar_ojo()

                        #cuerpo Cuki
                        def dibujar_rectangulo():
                            turtle.goto(-12.5, -10)
                            turtle.color("brown")
                            turtle.begin_fill()
                            for _ in range(2):
                                turtle.forward(45)
                                turtle.left(90)
                                turtle.forward(25)
                                turtle.left(90)
                            turtle.end_fill()

                        dibujar_rectangulo()

                        #patas Cuki
                        def dibujar_rectangulo2():
                            turtle.goto(-12.5, -45)
                            turtle.color("brown")
                            turtle.begin_fill()
                            for _ in range(2):
                                turtle.forward(10)
                                turtle.left(90)
                                turtle.forward(35)
                                turtle.left(90)
                            turtle.end_fill()

                        dibujar_rectangulo2()

                        #garras Cuki
                        def dibujar_rectangulo2():
                            turtle.goto(-12.5, -15)
                            turtle.color("brown")
                            turtle.begin_fill()
                            for _ in range(2):
                                turtle.forward(10)
                                turtle.left(90)
                                turtle.forward(35)
                                turtle.left(90)
                            turtle.end_fill()

                        dibujar_rectangulo2()

                        #cola
                        def dibujar_triangulo():
                            lado = 30

                            turtle.penup()
                            turtle.goto(-12.5, -45)
                            turtle.pendown()
                            turtle.setheading(-250)
                            turtle.color("brown")  
                            turtle.begin_fill()
                            turtle.forward(lado)
                            turtle.left(120)
                            turtle.forward(lado)
                            turtle.left(120)
                            turtle.forward(lado)
                            turtle.end_fill() 

                        dibujar_triangulo()
                dibujar_ardilla()

                def dibujar_suelo():
                        turtle.goto(-300, -70) 
                        turtle.color("DarkGrey")
                        turtle.setheading(0)
                        turtle.begin_fill()
                        for _ in range(2):
                            turtle.forward(600)
                            turtle.left(90)
                            turtle.forward(20)
                            turtle.left(90)
                        turtle.end_fill()
                dibujar_suelo()

                def dibujar_buho():
                    # Cuerpo del búho
                    turtle.penup()
                    turtle.goto(100, -50)
                    turtle.pendown()
                    turtle.color("brown")
                    turtle.begin_fill()
                    turtle.circle(50)
                    turtle.end_fill()

                    # Ojos del búho
                    # Iris
                    turtle.penup()
                    turtle.goto(80, 20)
                    turtle.pendown()
                    turtle.color("yellow")
                    turtle.begin_fill()
                    turtle.circle(15)
                    turtle.end_fill()
                    turtle.penup()
                    turtle.goto(120, 20)
                    turtle.pendown()
                    turtle.begin_fill()
                    turtle.circle(15)
                    turtle.end_fill()
                    # Pupilas
                    turtle.penup()
                    turtle.goto(80, 20)
                    turtle.pendown()
                    turtle.color("black")
                    turtle.begin_fill()
                    turtle.circle(5)
                    turtle.end_fill()
                    turtle.penup()
                    turtle.goto(120, 20)
                    turtle.pendown()
                    turtle.begin_fill()
                    turtle.circle(5)
                    turtle.end_fill()

                    # Pico del búho
                    turtle.penup()
                    turtle.goto(100, 20)
                    turtle.pendown()
                    turtle.color("orange")
                    turtle.setheading(270)
                    turtle.begin_fill()
                    turtle.forward(30)
                    turtle.left(135)
                    turtle.forward(20)
                    turtle.left(90)
                    turtle.forward(20)
                    turtle.left(135)
                    turtle.forward(30)
                    turtle.end_fill()

                    # Patas del búho
                    turtle.penup()
                    turtle.goto(90, -50)
                    turtle.pendown()
                    turtle.color("yellow")
                    turtle.begin_fill()
                    turtle.setheading(120)
                    for _ in range(3):
                        turtle.forward(20)
                        turtle.left(120)
                    turtle.end_fill()

                    turtle.penup()
                    turtle.goto(110, -50)
                    turtle.pendown()
                    turtle.color("yellow")
                    turtle.begin_fill()
                    turtle.setheading(60)
                    for _ in range(3):
                        turtle.forward(20)
                        turtle.left(120)
                    turtle.end_fill()

                dibujar_buho()

                turtle.penup()
                turtle.goto(turtle.xcor(), turtle.ycor() - 475)
                turtle.write("Si quiere cambiar de escena presione la tecla espacio", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)

                def activar_cambio_escena1():
                    turtle.onkey(cambiar_escena, "space") 

                turtle.listen()
                activar_cambio_escena1()
                turtle.mainloop()
                cambiar_escena()

                def cambiar_escena():
                    turtle.write("", align="center", font=("Arial", 14, "bold"))

                numero_escena = turtle.textinput("AVISOOOOO!", "Desea Cambiar de escena? Presione 6")

                try:
                    numero_escena = int (numero_escena) 
                    print(f"Cambiando a la escena...")  
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido.")

            case 2:
                turtle.clear()
                turtle.pendown()
                turtle.color("black")
                turtle.setheading(270)

                turtle.teleport(-300,250)
                for x in range(0, 2):
                    turtle.forward(50)
                    turtle.left(-90)
                    for x in range (2,3):
                        turtle.forward(-600)
                        turtle.left(-90)
                turtle.penup()
                turtle.forward(50)  
                turtle.left(90)
                turtle.forward(50)  
                turtle.write("Titulo escena 2: La búsqueda del tesoro", font=("Arial", 16, "bold"))
                turtle.hideturtle()

                turtle.pendown()
                turtle.teleport(300,-250)
                for x in range(0, 2):
                    turtle.forward(-600)
                    turtle.left(90)
                    for x in range (2,3):
                        turtle.forward(100)
                        turtle.left(90)
                turtle.penup()
                turtle.forward(-590)  
                turtle.left(-90)
                turtle.forward(-65)  
                turtle.write("El mapa mostraba el camino hacia un tesoro escondido. Con gran emoción, Cuki ", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
                turtle.write(" decidió seguir el mapa. Atravesó arroyos cristalinos y pasó por campos de", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
                turtle.write("flores, hasta llegar a una cueva misteriosa donde, según el mapa, estaba el tesoro.", font=("Arial", 12))  
                turtle.hideturtle()

                turtle.pendown()
                turtle.teleport (-300, 200)
                for x in range(0, 2):
                    turtle.forward(350)
                    turtle.left(-90)
                    for x in range (2,3):
                        turtle.forward(-600)
                        turtle.left(-90)

                def dibujar_ardilla():
                        #cabeza Cuki
                        def dibujar_circulo():
                            turtle.penup()
                            turtle.goto(-15, 15)
                            turtle.pendown()
                            turtle.color("brown")
                            turtle.begin_fill()
                            turtle.circle(20)
                            turtle.end_fill()

                        dibujar_circulo()

                            #orejas Cuki
                        def dibujar_ore():
                            turtle.penup()
                            turtle.goto(-15, 35)
                            turtle.pendown()
                            turtle.color("brown")
                            turtle.begin_fill()
                            turtle.circle(5)
                            turtle.end_fill()

                        dibujar_ore()

                        #Ojo Cuki
                        def dibujar_ojo():
                            turtle.penup()
                            turtle.goto(10, 10)
                            turtle.pendown()
                            turtle.color("black")
                            turtle.begin_fill()
                            turtle.circle(5)
                            turtle.end_fill()

                        dibujar_ojo()

                        #cuerpo Cuki
                        def dibujar_rectangulo():
                            turtle.goto(-12.5, -10)
                            turtle.color("brown")
                            turtle.begin_fill()
                            for _ in range(2):
                                turtle.forward(45)
                                turtle.left(90)
                                turtle.forward(25)
                                turtle.left(90)
                            turtle.end_fill()

                        dibujar_rectangulo()

                        #patas Cuki
                        def dibujar_rectangulo2():
                            turtle.goto(-12.5, -45)
                            turtle.color("brown")
                            turtle.begin_fill()
                            for _ in range(2):
                                turtle.forward(10)
                                turtle.left(90)
                                turtle.forward(35)
                                turtle.left(90)
                            turtle.end_fill()

                        dibujar_rectangulo2()

                        #garras Cuki
                        def dibujar_rectangulo2():
                            turtle.goto(-12.5, -15)
                            turtle.color("brown")
                            turtle.begin_fill()
                            for _ in range(2):
                                turtle.forward(10)
                                turtle.left(90)
                                turtle.forward(35)
                                turtle.left(90)
                            turtle.end_fill()

                        dibujar_rectangulo2()

                        #cola
                        def dibujar_triangulo():
                            lado = 30

                            turtle.penup()
                            turtle.goto(-12.5, -45)
                            turtle.pendown()
                            turtle.setheading(-250)
                            turtle.color("brown")  
                            turtle.begin_fill()
                            turtle.forward(lado)
                            turtle.left(120)
                            turtle.forward(lado)
                            turtle.left(120)
                            turtle.forward(lado)
                            turtle.end_fill() 

                        dibujar_triangulo()
                dibujar_ardilla()

                def dibujar_arroyo():
                        turtle.goto(-300, -90) 
                        turtle.color("CadetBlue1")
                        turtle.setheading(0)
                        turtle.begin_fill()
                        for _ in range(2):
                            turtle.forward(600)
                            turtle.left(90)
                            turtle.forward(20)
                            turtle.left(90)
                        turtle.end_fill()
                dibujar_arroyo()

                def dibujar_grama():
                        turtle.goto(-300, -70) 
                        turtle.color("green")
                        turtle.setheading(0)
                        turtle.begin_fill()
                        for _ in range(2):
                            turtle.forward(600)
                            turtle.left(90)
                            turtle.forward(20)
                            turtle.left(90)
                        turtle.end_fill()
                dibujar_grama ()

                def dibujar_cueva():
                    def afuera():
                            turtle.goto(150, -70)  #
                            turtle.color("DarkGray")
                            turtle.setheading(0)
                            turtle.begin_fill()
                            for _ in range(2):
                                turtle.forward(150)
                                turtle.left(90)
                                turtle.forward(200)
                                turtle.left(90)
                            turtle.end_fill()
                    afuera()

                    def entrada():
                            turtle.goto(180, -70)  #
                            turtle.color("black")
                            turtle.setheading(0)
                            turtle.begin_fill()
                            for _ in range(2):
                                turtle.forward(30)
                                turtle.left(90)
                                turtle.forward(100)
                                turtle.left(90)
                            turtle.end_fill()
                    entrada()
                dibujar_cueva()

                turtle.penup()
                turtle.goto(turtle.xcor(), turtle.ycor() - 475)
                turtle.write("Si quiere cambiar de escena presione la tecla espacio", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)

                def activar_cambio_escena1():
                    turtle.onkey(cambiar_escena, "space") 

                turtle.listen()
                activar_cambio_escena1()
                turtle.mainloop()
                cambiar_escena()

                def cambiar_escena():
                    turtle.write("", align="center", font=("Arial", 14, "bold"))

                numero_escena = turtle.textinput("AVISOOOOO!", "Desea Cambiar de escena? Presione 6")

                try:
                    numero_escena = int (numero_escena) 
                    print(f"Cambiando a la escena...")  
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido.")

            case 4:
                turtle.clear()
                turtle.pendown()
                turtle.setheading(270)
                turtle.color("black")
                turtle.teleport(-300,250)
                for x in range(0, 2):
                    turtle.forward(50)
                    turtle.left(-90)
                    for x in range (2,3):
                        turtle.forward(-600)
                        turtle.left(-90)
                turtle.penup()
                turtle.forward(50)  
                turtle.left(90)
                turtle.forward(50)  
                turtle.write("Titulo escena 4: El tesoro descubierto", font=("Arial", 16, "bold"))
                turtle.hideturtle()

                turtle.pendown()
                turtle.teleport(300,-250)
                for x in range(0, 2):
                    turtle.forward(-600)
                    turtle.left(90)
                    for x in range (2,3):
                        turtle.forward(100)
                        turtle.left(90)
                turtle.penup()
                turtle.forward(-590)  
                turtle.left(-90)
                turtle.forward(-65)  
                turtle.write("Con el acertijo resuelto, Don Hoot le mostró a Cuki el tesoro: una caja llena de gemas", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
                turtle.write("brillantes y una corona de flores. Cuki estaba fascinada por la belleza del tesoro", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
                turtle.write("y agradeció al búho con un abrazo de amistad.", font=("Arial", 12))  
                turtle.hideturtle()

                turtle.pendown()
                turtle.teleport (-300, 200)
                for x in range(0, 2):
                    turtle.forward(350)
                    turtle.left(-90)
                    for x in range (2,3):
                        turtle.forward(-600)
                        turtle.left(-90)
                def dibujar_ardilla():
                        #cabeza Cuki
                        def dibujar_circulo():
                            turtle.penup()
                            turtle.goto(-15, 15)
                            turtle.pendown()
                            turtle.color("brown")
                            turtle.begin_fill()
                            turtle.circle(20)
                            turtle.end_fill()

                        dibujar_circulo()

                            #orejas Cuki
                        def dibujar_ore():
                            turtle.penup()
                            turtle.goto(-15, 35)
                            turtle.pendown()
                            turtle.color("brown")
                            turtle.begin_fill()
                            turtle.circle(5)
                            turtle.end_fill()

                        dibujar_ore()

                        #Ojo Cuki
                        def dibujar_ojo():
                            turtle.penup()
                            turtle.goto(10, 10)
                            turtle.pendown()
                            turtle.color("black")
                            turtle.begin_fill()
                            turtle.circle(5)
                            turtle.end_fill()

                        dibujar_ojo()

                        #cuerpo Cuki
                        def dibujar_rectangulo():
                            turtle.goto(-12.5, -10)
                            turtle.color("brown")
                            turtle.begin_fill()
                            for _ in range(2):
                                turtle.forward(45)
                                turtle.left(90)
                                turtle.forward(25)
                                turtle.left(90)
                            turtle.end_fill()

                        dibujar_rectangulo()

                        #patas Cuki
                        def dibujar_rectangulo2():
                            turtle.goto(-12.5, -45)
                            turtle.color("brown")
                            turtle.begin_fill()
                            for _ in range(2):
                                turtle.forward(10)
                                turtle.left(90)
                                turtle.forward(35)
                                turtle.left(90)
                            turtle.end_fill()

                        dibujar_rectangulo2()

                        #garras Cuki
                        def dibujar_rectangulo2():
                            turtle.goto(-12.5, -15)
                            turtle.color("brown")
                            turtle.begin_fill()
                            for _ in range(2):
                                turtle.forward(10)
                                turtle.left(90)
                                turtle.forward(35)
                                turtle.left(90)
                            turtle.end_fill()

                        dibujar_rectangulo2()

                        #cola
                        def dibujar_triangulo():
                            lado = 30

                            turtle.penup()
                            turtle.goto(-12.5, -45)
                            turtle.pendown()
                            turtle.setheading(-250)
                            turtle.color("brown")  
                            turtle.begin_fill()
                            turtle.forward(lado)
                            turtle.left(120)
                            turtle.forward(lado)
                            turtle.left(120)
                            turtle.forward(lado)
                            turtle.end_fill() 

                        dibujar_triangulo()
                dibujar_ardilla()
                def dibujar_suelo():
                        turtle.goto(-300, -70) 
                        turtle.color("DarkGrey")
                        turtle.setheading(0)
                        turtle.begin_fill()
                        for _ in range(2):
                            turtle.forward(600)
                            turtle.left(90)
                            turtle.forward(20)
                            turtle.left(90)
                        turtle.end_fill()
                dibujar_suelo()

                def dibujar_buho():
                    # Cuerpo del búho
                    turtle.penup()
                    turtle.goto(100, -50)
                    turtle.pendown()
                    turtle.color("brown")
                    turtle.begin_fill()
                    turtle.circle(50)
                    turtle.end_fill()

                    # Ojos del búho
                    # Iris
                    turtle.penup()
                    turtle.goto(80, 20)
                    turtle.pendown()
                    turtle.color("yellow")
                    turtle.begin_fill()
                    turtle.circle(15)
                    turtle.end_fill()
                    turtle.penup()
                    turtle.goto(120, 20)
                    turtle.pendown()
                    turtle.begin_fill()
                    turtle.circle(15)
                    turtle.end_fill()
                    # Pupilas
                    turtle.penup()
                    turtle.goto(80, 20)
                    turtle.pendown()
                    turtle.color("black")
                    turtle.begin_fill()
                    turtle.circle(5)
                    turtle.end_fill()
                    turtle.penup()
                    turtle.goto(120, 20)
                    turtle.pendown()
                    turtle.begin_fill()
                    turtle.circle(5)
                    turtle.end_fill()

                    # Pico del búho
                    turtle.penup()
                    turtle.goto(100, 20)
                    turtle.pendown()
                    turtle.color("orange")
                    turtle.setheading(270)
                    turtle.begin_fill()
                    turtle.forward(30)
                    turtle.left(135)
                    turtle.forward(20)
                    turtle.left(90)
                    turtle.forward(20)
                    turtle.left(135)
                    turtle.forward(30)
                    turtle.end_fill()

                    # Patas del búho
                    turtle.penup()
                    turtle.goto(90, -50)
                    turtle.pendown()
                    turtle.color("yellow")
                    turtle.begin_fill()
                    turtle.setheading(120)
                    for _ in range(3):
                        turtle.forward(20)
                        turtle.left(120)
                    turtle.end_fill()

                    turtle.penup()
                    turtle.goto(110, -50)
                    turtle.pendown()
                    turtle.color("yellow")
                    turtle.begin_fill()
                    turtle.setheading(60)
                    for _ in range(3):
                        turtle.forward(20)
                        turtle.left(120)
                    turtle.end_fill()

                dibujar_buho()

                def dibujar_cofre():
                            def cuerpo():
                                turtle.goto(-150, -70)  #
                                turtle.color("brown")
                                turtle.setheading(0)
                                turtle.begin_fill()
                                for _ in range(2):
                                    turtle.forward(60)
                                    turtle.left(90)
                                    turtle.forward(40)
                                    turtle.left(90)
                                turtle.end_fill()
                            cuerpo()
                            def tapa():
                                turtle.goto(-150, -70)  #
                                turtle.color("brown")
                                turtle.setheading(0)
                                turtle.begin_fill()
                                for _ in range(2):
                                    turtle.forward(20)
                                    turtle.left(90)
                                    turtle.forward(70)
                                    turtle.left(90)
                                turtle.end_fill()
                            tapa()
                dibujar_cofre()

                def dibujar_moneda(x, y):
                    turtle.penup()
                    turtle.goto(x, y)
                    turtle.pendown()
                    turtle.color("gold")
                    turtle.begin_fill()
                    turtle.circle(10)
                    turtle.end_fill()

                posiciones = [(-150, -50), (-130, -30), (-115, -65), (-120, -85), (-100, -40)]
                for posicion in posiciones:
                    dibujar_moneda(posicion[0], posicion[1])

                turtle.penup()
                turtle.goto(turtle.xcor(), turtle.ycor() - 475)
                turtle.write("Si quiere cambiar de escena presione la tecla espacio", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)

                def activar_cambio_escena1():
                    turtle.onkey(cambiar_escena, "space") 

                turtle.listen()
                activar_cambio_escena1()
                turtle.mainloop()
                cambiar_escena()

                def cambiar_escena():
                    turtle.write("", align="center", font=("Arial", 14, "bold"))

                numero_escena = turtle.textinput("AVISOOOOO!", "Desea Cambiar de escena? Presione 6")

                try:
                    numero_escena = int (numero_escena) 
                    print(f"Cambiando a la escena...")  
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido.")
               
            case 5:
                turtle.pendown()
                turtle.clear()
                turtle.setheading(270)
                turtle.color("black")
                turtle.teleport(-300,250)
                for x in range(0, 2):
                    turtle.forward(50)
                    turtle.left(-90)
                    for x in range (2,3):
                        turtle.forward(-600)
                        turtle.left(-90)
                turtle.penup()
                turtle.forward(50)  
                turtle.left(90)
                turtle.forward(50)  
                turtle.write("Titulo escena 5: El regreso a casa", font=("Arial", 16, "bold"))
                turtle.hideturtle()

                turtle.pendown()
                turtle.teleport(300,-250)
                for x in range(0, 2):
                    turtle.forward(-600)
                    turtle.left(90)
                    for x in range (2,3):
                        turtle.forward(100)
                        turtle.left(90)
                turtle.penup()
                turtle.forward(-590)  
                turtle.left(-90)
                turtle.forward(-65)  
                turtle.write("Llena de alegría y con el tesoro en sus patitas, Cuki regresó al Bosque Encantado. Sus", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
                turtle.write("amigos animales la recibieron con entusiasmo y todos celebraron con una fiesta bajo", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
                turtle.write(" la luz de la luna. Desde entonces, Cuki aprendió que las aventuras más valiosas son", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)   
                turtle.write("las compartidas con amigos                                     FIN", font=("Arial", 12))
                turtle.hideturtle()

                turtle.pendown()
                turtle.teleport (-300, 200)
                for x in range(0, 2):
                    turtle.forward(350)
                    turtle.left(-90)
                    for x in range (2,3):
                        turtle.forward(-600)
                        turtle.left(-90)
                def dibujar_ardilla():
                        #cabeza Cuki
                        def dibujar_circulo():
                            turtle.penup()
                            turtle.goto(-15, 15)
                            turtle.pendown()
                            turtle.color("brown")
                            turtle.begin_fill()
                            turtle.circle(20)
                            turtle.end_fill()

                        dibujar_circulo()

                            #orejas Cuki
                        def dibujar_ore():
                            turtle.penup()
                            turtle.goto(-15, 35)
                            turtle.pendown()
                            turtle.color("brown")
                            turtle.begin_fill()
                            turtle.circle(5)
                            turtle.end_fill()

                        dibujar_ore()

                        #Ojo Cuki
                        def dibujar_ojo():
                            turtle.penup()
                            turtle.goto(10, 10)
                            turtle.pendown()
                            turtle.color("black")
                            turtle.begin_fill()
                            turtle.circle(5)
                            turtle.end_fill()

                        dibujar_ojo()

                        #cuerpo Cuki
                        def dibujar_rectangulo():
                            turtle.goto(-12.5, -10)
                            turtle.color("brown")
                            turtle.begin_fill()
                            for _ in range(2):
                                turtle.forward(45)
                                turtle.left(90)
                                turtle.forward(25)
                                turtle.left(90)
                            turtle.end_fill()

                        dibujar_rectangulo()

                        #patas Cuki
                        def dibujar_rectangulo2():
                            turtle.goto(-12.5, -45)
                            turtle.color("brown")
                            turtle.begin_fill()
                            for _ in range(2):
                                turtle.forward(10)
                                turtle.left(90)
                                turtle.forward(35)
                                turtle.left(90)
                            turtle.end_fill()

                        dibujar_rectangulo2()

                        #garras Cuki
                        def dibujar_rectangulo2():
                            turtle.goto(-12.5, -15)
                            turtle.color("brown")
                            turtle.begin_fill()
                            for _ in range(2):
                                turtle.forward(10)
                                turtle.left(90)
                                turtle.forward(35)
                                turtle.left(90)
                            turtle.end_fill()

                        dibujar_rectangulo2()

                        #cola
                        def dibujar_triangulo():
                            lado = 30

                            turtle.penup()
                            turtle.goto(-12.5, -45)
                            turtle.pendown()
                            turtle.setheading(-250)
                            turtle.color("brown")  
                            turtle.begin_fill()
                            turtle.forward(lado)
                            turtle.left(120)
                            turtle.forward(lado)
                            turtle.left(120)
                            turtle.forward(lado)
                            turtle.end_fill() 

                        dibujar_triangulo()
                dibujar_ardilla()

                def dibujar_ardilla2():
                        turtle.setheading(270)

                        #cabeza Cuke
                        def dibujar_circuloa():
                            turtle.penup()
                            turtle.goto(-65, 15)
                            turtle.pendown()
                            turtle.color("DeepPink")
                            turtle.begin_fill()
                            turtle.circle(20)
                            turtle.end_fill()

                        dibujar_circuloa()

                            #orejas Cuke
                        def dibujar_orea():
                            turtle.penup()
                            turtle.goto(-65, 35)
                            turtle.pendown()
                            turtle.color("DeepPink")
                            turtle.begin_fill()
                            turtle.circle(5)
                            turtle.end_fill()

                        dibujar_orea()

                        #Ojo Cuke
                        def dibujar_ojoa():
                            turtle.penup()
                            turtle.goto(-40, 10)
                            turtle.pendown()
                            turtle.color("black")
                            turtle.begin_fill()
                            turtle.circle(5)
                            turtle.end_fill()

                        dibujar_ojoa()

                        #cuerpo Cuke
                        def dibujar_rectanguloa():
                            turtle.goto(-62.5, -10)
                            turtle.color("DeepPink")
                            turtle.begin_fill()
                            for _ in range(2):
                                turtle.forward(45)
                                turtle.left(90)
                                turtle.forward(25)
                                turtle.left(90)
                            turtle.end_fill()

                        dibujar_rectanguloa()

                        #patas Cuke
                        def dibujar_rectangulo2a():
                            turtle.goto(-62.5, -45)
                            turtle.color("DeepPink")
                            turtle.begin_fill()
                            for _ in range(2):
                                turtle.forward(10)
                                turtle.left(90)
                                turtle.forward(35)
                                turtle.left(90)
                            turtle.end_fill()

                        dibujar_rectangulo2a()

                        #garras Cuke
                        def dibujar_rectangulo3():
                            turtle.goto(-62.5, -15)
                            turtle.color("DeepPink")
                            turtle.begin_fill()
                            for _ in range(2):
                                turtle.forward(10)
                                turtle.left(90)
                                turtle.forward(35)
                                turtle.left(90)
                            turtle.end_fill()

                        dibujar_rectangulo3()

                        #cola
                        def dibujar_trianguloa():
                            lado = 30

                            turtle.penup()
                            turtle.goto(-62.5, -45)
                            turtle.pendown()
                            turtle.setheading(-250)
                            turtle.color("DeepPink")  
                            turtle.begin_fill()
                            turtle.forward(lado)
                            turtle.left(120)
                            turtle.forward(lado)
                            turtle.left(120)
                            turtle.forward(lado)
                            turtle.end_fill() 

                        dibujar_trianguloa()
                dibujar_ardilla2()

                def dibujar_grama():
                        turtle.goto(-300, -80) 
                        turtle.color("green")
                        turtle.setheading(0)
                        turtle.begin_fill()
                        for _ in range(2):
                            turtle.forward(600)
                            turtle.left(90)
                            turtle.forward(20)
                            turtle.left(90)
                        turtle.end_fill()
                dibujar_grama ()

                def dibujar_arbol():
                        #tronco
                        def dibujar_tronco():
                            turtle.goto(150, -70)  #
                            turtle.color("brown")
                            turtle.setheading(0)
                            turtle.begin_fill()
                            for _ in range(2):
                                turtle.forward(30)
                                turtle.left(90)
                                turtle.forward(100)
                                turtle.left(90)
                            turtle.end_fill()
                        dibujar_tronco()

                        #hojas
                        def dibujar_hojas():
                            turtle.penup()
                            turtle.goto(170, 25)
                            turtle.pendown()
                            turtle.color("green")
                            turtle.begin_fill()
                            turtle.circle(75)
                            turtle.end_fill()
                        dibujar_hojas()

                dibujar_arbol()

                def dibujar_luna():
                            turtle.penup()
                            turtle.goto(-170, 55)
                            turtle.pendown()
                            turtle.color("cornsilk1")
                            turtle.begin_fill()
                            turtle.circle(55)
                            turtle.end_fill()
                dibujar_luna()

                turtle.penup()
                turtle.goto(turtle.xcor(), turtle.ycor() - 475)
                turtle.write("Si quiere cambiar de escena presione la tecla espacio", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)

                def activar_cambio_escena1():
                    turtle.onkey(cambiar_escena, "space") 

                turtle.listen()
                activar_cambio_escena1()
                turtle.mainloop()
                cambiar_escena()

                def cambiar_escena():
                    turtle.write("", align="center", font=("Arial", 14, "bold"))

                numero_escena = turtle.textinput("AVISOOOOO!", "Desea Cambiar de escena? Presione 6")

                try:
                    numero_escena = int (numero_escena) 
                    print(f"Cambiando a la escena...")  
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido.")

                turtle.penup()
                turtle.goto(turtle.xcor(), turtle.ycor() - 475)
                turtle.write("Si quiere cambiar de escena presione la tecla espacio", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)

                def activar_cambio_escena1():
                    turtle.onkey(cambiar_escena, "space") 

                turtle.listen()
                activar_cambio_escena1()
                turtle.mainloop()
                cambiar_escena()

                def cambiar_escena():
                    turtle.write("", align="center", font=("Arial", 14, "bold"))

                numero_escena = turtle.textinput("AVISOOOOO!", "Desea Cambiar de escena? Presione 6")

                try:
                    numero_escena = int (numero_escena) 
                    print(f"Cambiando a la escena...")  
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido.")
            case 6:
                turtle.bye()

               

# Mover la tortuga a una posición adecuada y mostrar mensaje inicial
turtle.penup()
turtle.goto(turtle.xcor(), turtle.ycor() - 500)
turtle.write("Si quiere cambiar de escena presione la tecla espacio", font=("Arial", 12))
turtle.goto(turtle.xcor(), turtle.ycor() - 20)

# Llamar a la función cambiar_escena() cuando se presione la tecla "space"
def activar_cambio_escena():
    turtle.onkey(cambiar_escena_inicio, "space") 

turtle.listen()

# Llamar a activar_cambio_escena() para configurar la tecla "space"
activar_cambio_escena()
turtle.mainloop()



turtle.done()
