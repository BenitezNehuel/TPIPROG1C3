print("Estas encerrado en una habitacion a oscuras. Podes ver una pequeña luz salir de una puerta cerrada. ¡Busca una forma de salir!")
lucesPrendidas = False
escritorioCorrido = False
escape = False
llave = False
ultravioleta = False
def cuarto_visible():
    print("+------------------------------------------+")
    print("|                   [Cuadro]               |")
    print("|                                          |")
    print("| _________                                |")
    print("||         |                               |")
    print("||  Cama   |                               |")
    print("||_________|                               |")
    print("||         |                               |")
    print("||         |                    __________ |")
    print("||         |                   |          ||")
    print("||_________|                   |Escritorio||")
    print("|                              |__________||")
    print("|                             [Interruptor]|")
    print("|                                          |")
    print("|                                          |")
    print("|   ________                               |")
    print("|  |        |                              |")
    print("|  |armario |                              |")
    print("|  |________|                              |")
    print("|                                          |")
    print("|                           [Puerta]       |")
    print("+------------------------------------------+")
def mostrar_cuadro_real():
    
    print( "+-----------------------+")
    print( "|   #################   |")
    print( "| ## L# ###A### ## ## # |")
    print( "|  ## ## C#L##A# ## ##  |")
    print( "| ## ## ##V#### ## ## # |")
    print( "|    #######E#########  |")
    print( "| ## ## ####### ## ## # |")
    print( "|  ###################  |")
    print( "| ## ###E############# #|")
    print( "|   ## ## ##### ## ##   |")
    print( "| ## ## ####### S# ## # |")
    print( "|      ### ##### ###    |")
    print( "| ##################### |")
    print( "|         1626          |")
    print( "+-----------------------+")

def mostrar_cuadro():
    
    print( "+-----------------------+")
    print( "|   #################   |")
    print( "| ## ## ####### ## ## # |")
    print( "|  ## ## ####### ## ##  |")
    print( "| ## ## ####### ## ## # |")
    print( "|    #################  |")
    print( "| ## ## ####### ## ## # |")
    print( "|  ###################  |")
    print( "| ## ################# #|")
    print( "|   ## ## ##### ## ##   |")
    print( "| ## ## ####### ## ## # |")
    print( "|      ### ##### ###    |")
    print( "| ##################### |")
    print( "|         ####          |")
    print( "+-----------------------+")
while not escape :
    print("\n1. Mirar a tu alrededor\n2. Caminar por la habitacion\n3. Intentar abrir la puerta")
    intro = int(input("-->"))

    if intro == 1:
        if not lucesPrendidas:
            print("No podes ver nada, esta todo oscuro.")
        elif lucesPrendidas:
            print("Podes ver la habitacion y los objetos alrededor.")
            print(cuarto_visible())
    
    elif intro == 2:
        if not lucesPrendidas:
            print("Decidis caminar por la habitación a oscuras. Te golpeás con algunas paredes y finalmente encontrás un escritorio.")
            print("\n1. Examinar escritorio\n2. Dejarlo\n3. Correr escritorio")
            caminarHabitacion = int(input("-->"))

            if caminarHabitacion == 1:
                print("Al tacto se siente como cualquier escritorio normal de madera. tiene un cajon que no puedes abrir")
            elif caminarHabitacion == 2:
                print("Decidís dejar el escritorio y seguir explorando.")
            elif caminarHabitacion == 3:
                escritorioCorrido = True
                print("Corriste el escritorio y encontraste un interruptor detras de el.")
                print("1. Presionar interruptor\n2. Dejarlo\n3. Acomodar escritorio")
                correrEscritorio = int(input("-->"))

                if correrEscritorio == 1:
                    if not lucesPrendidas:
                        lucesPrendidas = True
                        print("¡Se hizo la luz!")
                    else:
                        lucesPrendidas = False
                        print("Se apago la luz")
                    
                elif correrEscritorio == 2:
                    print("Decidis no tocar el interruptor.")
                elif correrEscritorio == 3:
                    print("Acomodas el escritorio en su lugar.")

        else:
            print("Ahora que hay luz, podes ver distintos objetos en la habitacion.")

            print("\n1. Examinar armario\n2. Examinar cama\n3. Examinar cuadro\n4.Examinar escritorio")
            explorarHabitacion = int(input("-->"))

            if explorarHabitacion == 1:
                print("Abris el armario y encontras una LUZ ULTRAVIOLETA.")
                ultravioleta = True  
            elif explorarHabitacion == 2:
                    print("Miras hasta por debajo de la cama pero no hay nada.")
            elif explorarHabitacion == 3:
                if ultravioleta:
                    print("Examinás el cuadro unos minutos, y utilizando la luz ultravioleta notas algo raro en la parte baja del cuadro, parece una clave.")
                    print(mostrar_cuadro_real())
                else:
                    print("Examinas el cuadro unos minutos pero no encuentras nada particular")
                    print(mostrar_cuadro())
            elif explorarHabitacion == 4:
                print("\n1. tocar interruptor\n2. abrir cajon")
                menuEscritorio = int(input())
                if menuEscritorio == 1:
                    if not lucesPrendidas:
                        lucesPrendidas = True
                        print("¡Se hizo la luz!")
                    else:
                        lucesPrendidas = False
                        print("Se apago la luz")
                elif menuEscritorio == 2:
                    print("ingrese la clave de 4 digitos:")
                    clave = int(input())
                    if clave == 1626:
                        print("Lograste abrir el cajon!. Conseguiste UNA LLAVE")
                        llave = True

                

    elif intro == 3:
        if llave:
            print("¡Abriste la puerta! ¡Sos libre!")
            escape = True
        else:
            print("La puerta está cerrada. Necesitás encontrar una llave.")
      
