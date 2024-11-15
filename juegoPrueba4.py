print("Estas encerrado en una habitacion a oscuras. Podes ver una pequeña luz salir de una puerta cerrada. ¡Busca una forma de salir!")
luces_prendidas = False
escritorio_corrido = False
escape = False
llave = False
ultravioleta = False

#variables que dibujan con ASCII
def candadoCerrado():
    print("       _____________ ")
    print("      |             |")
    print("      | [4][5][6][7]|")
    print("      |_____________|")
    print("        ||      ||")
    print("        ||      ||")
    print("        ||______||")
    print("        |________|")
def cuartoVisible():
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
def mostrarCuadroReal():
    
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
def mostrarCuadro():


    
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

#bucle while principal (solo al abrir la puerta saldremos del bucle)
while not escape :
    print("\n1. Mirar a tu alrededor\n2. Caminar por la habitacion\n3. Intentar abrir la puerta")
    intro = int(input("-->"))

    if intro == 1:
        if not luces_prendidas:
            print("No podes ver nada, esta todo oscuro.")
        elif luces_prendidas:
            print("Podes ver la habitacion y los objetos alrededor.")
            print(cuartoVisible())
    
    elif intro == 2:
        if not luces_prendidas:
            print("Decidis caminar por la habitación a oscuras. Te golpeás con algunas paredes y finalmente encontrás un escritorio.")
            print("\n1. Examinar escritorio\n2. Dejarlo\n3. Correr escritorio")
            caminar_habitacion = int(input("-->"))

            if caminar_habitacion == 1:
                    print("Al tacto se siente como cualquier escritorio normal de madera. tiene un cajon que no puedes abrir")
            elif caminar_habitacion == 2:
                print("Decidís dejar el escritorio y seguir explorando.")
            elif caminar_habitacion == 3:
                escritorio_corrido = True
                print("Corriste el escritorio y encontraste un interruptor detras de el.")
                print("1. Presionar interruptor\n2. Dejarlo\n3. Acomodar escritorio")
                correr_escritorio = int(input("-->"))

                if correr_escritorio == 1:
                    if not luces_prendidas:
                        luces_prendidas = True
                        print("¡Se hizo la luz!")
                    else:
                        luces_prendidas = False
                        print("Se apago la luz")
                    
                elif correr_escritorio == 2:
                    print("Decidis no tocar el interruptor.")
                elif correr_escritorio == 3:
                    print("Acomodas el escritorio en su lugar.")
                    escritorio_corrido = False
        else:
            print("Ahora que hay luz, podes ver distintos objetos en la habitacion.")

            print("\n1. Examinar armario\n2. Examinar cama\n3. Examinar cuadro\n4.Examinar escritorio")
            explorar_habitacion = int(input("-->"))

            if explorar_habitacion == 1:
                print("Abris el armario y encontras una LUZ ULTRAVIOLETA.")
                ultravioleta = True  

            elif explorar_habitacion == 2:
                    print("Miras hasta por debajo de la cama pero no hay nada.")
            elif explorar_habitacion == 3:
                if ultravioleta:
                    print("Examinás el cuadro unos minutos, y utilizando la luz ultravioleta notas algo raro en la parte baja del cuadro, parece una clave.")
                    print(mostrarCuadroReal())
                else:
                    print("Examinas el cuadro unos minutos pero no encuentras nada particular")
                    print(mostrarCuadro())
            elif explorar_habitacion == 4:
                print("Ahora que ves el escritorio con claridad, notas que el cajon tiene un candado cidrado con 4 numeros.")
                print(candadoCerrado())
                print("\n1. tocar interruptor\n2. abrir cajon")
                menu_escritorio = int(input())
                if menu_escritorio == 1:
                    if not luces_prendidas:
                        luces_prendidas = True
                        print("¡Se hizo la luz!")
                    else:
                        luces_prendidas = False
                        print("Se apago la luz")
                elif menu_escritorio == 2:
                    print("ingresa la clave de 4 digitos:")
                    clave = int(input())
                    if clave == 1626:
                        print("Lograste abrir el cajon!. Conseguiste UNA LLAVE")
                        llave = True
                    else:
                        print("Esa no es la clave.")

                

    elif intro == 3:
        if llave:
            print("¡¡¡Felicidades!!!\n¡Abriste la puerta! ¡Sos libre!")
            escape = True
        else:
            print("La puerta está cerrada. Necesitás encontrar una llave.")
      
