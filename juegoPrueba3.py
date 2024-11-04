print("Estas encerrado en una habitacion a oscuras. Podes ver una pequeña luz salir de una puerta cerrada. ¡Busca una forma de salir!")
lucesApagadas = False
escritorioCorrido = False
escape = False
win = False

while not win:
    print("\n1. Mirar a tu alrededor\n2. Caminar por la habitacion\n3. Intentar abrir la puerta")
    intro = int(input("-->"))

    if intro == 1:
        if not lucesApagadas:
            print("No podes ver nada, esta todo oscuro.")
        elif lucesApagadas:
            print("Podes ver la habitacion y los objetos alrededor.")
    
    elif intro == 2:
        if not lucesApagadas:
            print("Decidis caminar por la habitación a oscuras. Te golpeás con algunas paredes y finalmente encontrás un escritorio.")
            print("\n1. Examinar escritorio\n2. Dejarlo\n3. Correr escritorio")
            caminarHabitacion = int(input("-->"))

            if caminarHabitacion == 1:
                print("Al tacto se siente como cualquier escritorio normal de madera.")
            elif caminarHabitacion == 2:
                print("Decidís dejar el escritorio y seguir explorando.")
            elif caminarHabitacion == 3:
                escritorioCorrido = True
                print("Corriste el escritorio y encontraste un interruptor detras de el.")
                print("1. Presionar interruptor\n2. Dejarlo\n3. Acomodar escritorio")
                correrEscritorio = int(input("-->"))

                if correrEscritorio == 1:
                    lucesApagadas = True
                    print("¡Se hizo la luz!")
                elif correrEscritorio == 2:
                    print("Decidis no tocar el interruptor.")
                elif correrEscritorio == 3:
                    print("Acomodas el escritorio en su lugar.")

        else:
            print("Ahora que hay luz, podes ver distintos objetos en la habitacion.")
            print("\n1. Examinar armario\n2. Examinar cama\n3. Examinar cuadro")
            explorarHabitacion = int(input("-->"))

            if explorarHabitacion == 1:
                print("Abris el armario y encontras una llave.")
                escape = True  
            elif explorarHabitacion == 2:
                print("Miras hasta por debajo de la cama pero no hay nada.")
            elif explorarHabitacion == 3:
                print("Examinás el cuadro unos minutos, pero no encontrás nada especial.")

    elif intro == 3:
        if escape:
            print("¡Encontraste la llave y abriste la puerta! ¡Sos libre!")
            break  
        else:
            print("La puerta está cerrada. Necesitás encontrar una llave.")
