def iniciarJuego():
    salir = False
    global iniciar_reloj
    while salir == False:
        print("🤖 LightBot 💡")
        print("1) Cargar partida")
        print("     -Nivel",str(cargarEstadisticas()["nivel"])+"\n     -Luces conseguidas: "+str(cargarEstadisticas()["luces_conseguidas"])+"\n     -Tiempo jugado:",tiempoJugado(cargarEstadisticas()["tiempo_jugado"]))
        print("2) Reiniciar progreso")
        print("3) Salir")
        opcion = str(input("-> "))
        match opcion:
            case "1":
                iniciar_reloj = time.time()
                return cargarEstadisticas()
            case "2":
                iniciar_reloj = time.time()
                reiniciarEstadisticas()
                return cargarEstadisticas()
            case "3":
                salir=True #Hay que conectarlo al menú
                return "cerrar juego"
        os.system("cls")

def tiempoJugado(tiempo):
    if tiempo<60:
        return(str(tiempo)+" segundos")
    elif tiempo<3600:
        return str(tiempo//60)+" minutos"
    else:
        return str((tiempo/60)/60)+" horas"

def iniciarNivel():
    os.system('cls')
    #Definir area del nivel
    global filas
    global columnas

    filas= int(datos["nivel"])+3

    columnas= int(datos["nivel"])+3

    #Cargar posicion inicial del jugador
    global posicion_jugador
    posicion_jugador = [0,0]
    global nivel
    nivel = crearNivel(posicion_jugador)

    #Crear puntos por los que el jugador debe pasar.
    global cantidadPuntos
    cantidadPuntos = (random.randint(1,2))*int(datos["nivel"])
    crearPuntos(cantidadPuntos,posicion_jugador)
    juegoMenu()

def sacarEspacios(movimientos):
    movs_sin_espacio = ""
    for i in range(len(movimientos)):
        if movimientos[i]>="0" and movimientos[i]<="9":
            movs_sin_espacio+=movimientos[i]
    return movs_sin_espacio

def juegoMenu():
    salir = False
    mostrarNivel()
    while salir==False:
        distancia = puntoMasCercano()
        print("1) Derecha.\n2) Izquierda.\n3) Arriba.\n4) Abajo.\n10) Salir.")
        movimientos = input("Ingrese la secuencia de movimientos separadas por espacios: ")
        if movimientos != "10":
            if len(sacarEspacios(movimientos))<=distancia:
                os.system('cls')
                sacarEspacios(movimientos)
                movimiento(movimientos,posicion_jugador)
            else:
                os.system('cls')
                print("La secuencia ingresada excede la cantidad de movimientos permitidos en este momento.")
                mostrarNivel()
        else:
            finalizar_reloj = time.time()
            datos["tiempo_jugado"] += int(finalizar_reloj-iniciar_reloj)
            actualizarEstadisticas()
            salir = True

def reiniciarEstadisticas():
    with open("lightbot\estadisticas.txt", "w") as estadisticas:
        nivel = 1
        luces_conseguidas = 0
        tiempo_jugado = 0
        estadisticas.write("nivel "+str(nivel)+"\nluces_conseguidas "+str(luces_conseguidas)+"\ntiempo_jugado "+str(tiempo_jugado))

def cargarEstadisticas():
    estadisticas = open("lightbot\estadisticas.txt", "r")
    datos = {}
    estadisticas_separadas = estadisticas.readlines()
    for linea in estadisticas_separadas:
        clave = (linea.strip().split())[0]
        valor = int((linea.strip().split())[1])
        datos[clave] = valor
    estadisticas.close()
    #print(datos)
    return datos

def actualizarEstadisticas():
    with open("lightbot\estadisticas.txt", "w") as estadisticas:
        estadisticas.write("nivel "+str(datos["nivel"])+"\nluces_conseguidas "+str(datos["luces_conseguidas"])+"\ntiempo_jugado "+str(datos["tiempo_jugado"]))

def puntoMasCercano():
    distancia = 999
    luz_cercana_posicion = [0,0]
    for fila in range(filas):
        for columna in range(columnas):
            if nivel[fila][columna]=="💡":
                if distanciaManhattan(fila,columna)<distancia:
                    distancia=distanciaManhattan(fila,columna)
                    luz_cercana_posicion[0] = fila
                    luz_cercana_posicion[1] = columna
    #r = ("El punto más cercano esta a",distancia,"movimientos\nEn x",luz_cercana_posicion[0],". y",luz_cercana_posicion[1])
    print("Tienes",distancia,"movimientos máximos para llegar a la luz más cercana")
    return distancia

def distanciaManhattan(fila,columna):
    #La formula es (x2-x1)+(y2-y1)
    #Se debe usar el valor absoluto del resultado de cada resta.
    return valorAbsoluto(fila-posicion_jugador[0])+valorAbsoluto(columna-posicion_jugador[1])

def valorAbsoluto(resta_distancia):
    if resta_distancia<0:
        resta_distancia *=-1
    return resta_distancia

def crearNivel(posicion_jugador):
    nivel = [["⬜" for i in range(columnas)] for j in range(filas)]
    nivel[posicion_jugador[0]][posicion_jugador[1]] = "🤖"
    return nivel

def mostrarNivel():
    print("| Nivel",datos["nivel"],"| Luces restantes",cantidadPuntos,"|","Luces totales conseguidas",datos["luces_conseguidas"])
    for i in range(filas):
        for j in range(columnas):
            print(nivel[i][j],end="")
        print("")

def movimiento(movimientos, posicion_jugador):
    global nivel
    nivel_copia = [["⬜" for i in range(columnas)] for j in range(filas)]
    for fila in range(filas):
        for columna in range(columnas):
            nivel_copia[fila][columna] = nivel[fila][columna]

    luz_encontrada = False
    #Recorrer la cadena con la secuencia de movimientos ingresada
    try:
        for i in range(0,len(movimientos),2):
            nivel[posicion_jugador[0]][posicion_jugador[1]] = "⬜"
            os.system("cls")
            match int(movimientos[i]):
                case 1: #Derecha
                    posicion_jugador[1] = posicion_jugador[1]+1
                    luz_encontrada = verificarLuz()
                    nivel[posicion_jugador[0]][posicion_jugador[1]] = "🤖"
                    mostrarNivel()
                    #print(posicion_jugador)
                case 2: #Izquierda
                    posicion_jugador[1] = posicion_jugador[1]-1
                    luz_encontrada = verificarLuz()
                    nivel[posicion_jugador[0]][posicion_jugador[1]] = "🤖"
                    mostrarNivel()
                    #print(posicion_jugador)
                case 3: #Arriba
                    posicion_jugador[0] = posicion_jugador[0]-1
                    luz_encontrada = verificarLuz()
                    nivel[posicion_jugador[0]][posicion_jugador[1]] = "🤖"
                    mostrarNivel()
                    #print(posicion_jugador)
                case 4: #Abajo
                    posicion_jugador[0] = posicion_jugador[0]+1
                    luz_encontrada = verificarLuz()
                    nivel[posicion_jugador[0]][posicion_jugador[1]] = "🤖"
                    mostrarNivel()
                    #print(posicion_jugador)
                case _:
                    print("La secuencia no es correcta")
                    nivel = nivel_copia
                    break
            if cantidadPuntos==0:
                terminarNivel()
                global datos
                datos = cargarEstadisticas()
                iniciarNivel()
                break
            time.sleep(0.5)
        if not luz_encontrada:
            print("La secuencia no es correcta, regresando a la posición inicial.")
            for i in range(5,0,-1):
                time.sleep(1)
                print("Reiniciando en",i,"segundos.")
            os.system("cls")
            nivel = nivel_copia
            posicion_jugador[0] = ultima_luz_encontrada[0]
            posicion_jugador[1] = ultima_luz_encontrada[1]
            mostrarNivel()
    except:
        print("Ocurrio un problema leyendo la secuencia.")
        posicion_jugador[0] = ultima_luz_encontrada[0]
        posicion_jugador[1] = ultima_luz_encontrada[1]
        nivel[posicion_jugador[0]][posicion_jugador[1]] = "🤖"
        mostrarNivel()
            
def terminarNivel():
    print("")
    #os.system("cls")
    for i in range(3):
        print("Solución correcta\nPasando al siguiente nivel")
        for i in range(3):
            print(".",end=" ")
            time.sleep(0.6)
        os.system("cls")
    datos["nivel"]+=1
    actualizarEstadisticas()

def verificarLuz():
    global cantidadPuntos
    if nivel[posicion_jugador[0]][posicion_jugador[1]] == "💡":
        print("Luz encontrada")
        datos["luces_conseguidas"]+=1
        cantidadPuntos-=1
        global ultima_luz_encontrada
        ultima_luz_encontrada=[posicion_jugador[0],posicion_jugador[1]]
        actualizarEstadisticas()
        return True

def crearPuntos(cantidadPuntos,posicion_jugador):
    puntos_creados = 0
    while puntos_creados<cantidadPuntos:
        posicion_punto = [random.randint(0,filas-1),random.randint(0,columnas-1)]
        if posicion_jugador!=posicion_punto and nivel[posicion_punto[0]][posicion_punto[1]]!="💡":
            nivel[(posicion_punto[0])][(posicion_punto[1])] = "💡"
            puntos_creados +=1

#-----------Programa principal -----------
import random
import time
import os

def lightBot():
    #Limpiar pantalla para quitar el menú
    os.system("cls")
    global ultima_luz_encontrada
    ultima_luz_encontrada=[0,0]
    #Inicio del juego - menú
    global datos
    datos = iniciarJuego()
    
    if datos!="cerrar juego":
        iniciarNivel()
    else:
        os.system("cls")
        for i in range(3):
            print("Cerrando juego, volviendo al menú principal.")
            for i in range(3):
                print(".",end=" ")
                time.sleep(0.2)
            os.system("cls")
        

if __name__ == "__main__":
    lightBot()