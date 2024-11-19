def iniciarJuego():
    salir = False
    while salir == False:
        print("🤖 LightBot 💡")
        print("1) Cargar partida (Nivel",str(cargarEstadisticas()["nivel"])+")")
        print("2) Reiniciar progreso")
        print("3) Salir")
        opcion = str(input("-> "))
        match opcion:
            case "1":
                return cargarEstadisticas()
            case "2":
                reiniciarEstadisticas()
                return cargarEstadisticas()
            case "3":
                salir=True #Hay que conectarlo al menú

def iniciarNivel():
    os.system('cls')
    #Definir area del nivel
    global filas
    global columnas

    filas= int(datos["nivel"])+3

    columnas= int(datos["nivel"])+3

    #Cargar posicion inicial del jugador
    #¿Hacer aleatoria o iniciar en niveles fijos?ç
    global posicion_jugador
    posicion_jugador = [0,0]
    global nivel
    nivel = crearNivel(posicion_jugador)

    #Crear puntos por los que el jugador debe pasar.
    global cantidadPuntos
    cantidadPuntos = (random.randint(1,2))*int(datos["nivel"])
    crearPuntos(cantidadPuntos,posicion_jugador)
    juegoMenu()

def juegoMenu():
    salir = False
    mostrarNivel()
    while not salir:
        print(puntoMasCercano())
        print("1) Derecha.\n2) Izquierda.\n3)Arriba.\n4) Abajo.\n10) Salir.")
        movimientos = input("Ingrese la secuencia de movimientos separadas por espacios")
        if movimientos != "10":
            os.system('cls')
            movimiento(movimientos,posicion_jugador)
        else:
            salir = True

def reiniciarEstadisticas():
    with open("estadisticas.txt", "w") as estadisticas:
        nivel = 1
        luces_conseguidas = 0
        tiempo_jugado = 0
        estadisticas.write("nivel "+str(nivel)+"\nluces_conseguidas "+str(luces_conseguidas)+"\ntiempo_jugado "+str(tiempo_jugado))

def cargarEstadisticas():
    estadisticas = open("estadisticas.txt", "r")
    datos = {}
    estadisticas_separadas = estadisticas.readlines()
    for linea in estadisticas_separadas:
        clave = (linea.strip().split())[0]
        valor = int((linea.strip().split())[1])
        datos[clave] = valor
    estadisticas.close()
    print(datos)
    return datos

def actualizarEstadisticas():
    with open("estadisticas.txt", "w") as estadisticas:
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
    r = ("El punto más cercano esta a",distancia,"movimientos\nEn x",luz_cercana_posicion[0],". y",luz_cercana_posicion[1])
    return r

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
    print("| Nivel",datos["nivel"],"| Puntos restantes",cantidadPuntos,"|")
    for i in range(filas):
        for j in range(columnas):
            print(nivel[i][j],end="")
        print("")

def movimiento(movimientos, posicion_jugador):
    #Recorrer la cadena con la secuencia de movimientos ingresada
    for i in range(0,len(movimientos),2):
        nivel[posicion_jugador[0]][posicion_jugador[1]] = "⬜"
        match int(movimientos[i]):
            case 1: #Derecha
                posicion_jugador[1] = posicion_jugador[1]+1
                verificarLuz()
                nivel[posicion_jugador[0]][posicion_jugador[1]] = "🤖"
                mostrarNivel()
                print(posicion_jugador)
            case 2: #Izquierda
                posicion_jugador[1] = posicion_jugador[1]-1
                verificarLuz()
                nivel[posicion_jugador[0]][posicion_jugador[1]] = "🤖"
                mostrarNivel()
                print(posicion_jugador)
            case 3: #Arriba
                posicion_jugador[0] = posicion_jugador[0]-1
                verificarLuz()
                nivel[posicion_jugador[0]][posicion_jugador[1]] = "🤖"
                mostrarNivel()
                print(posicion_jugador)
            case 4: #Abajo
                posicion_jugador[0] = posicion_jugador[0]+1
                verificarLuz()
                nivel[posicion_jugador[0]][posicion_jugador[1]] = "🤖"
                mostrarNivel()
                print(posicion_jugador)
            case _:
                print("La secuencia no es correcta")
                break
        if cantidadPuntos==0:
            terminarNivel()
            global datos
            datos = cargarEstadisticas()
            iniciarNivel()
            break
            
def terminarNivel():
    os.system("cls")
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
        actualizarEstadisticas()

def crearPuntos(cantidadPuntos,posicion_jugador):
    puntos_creados = 0
    while puntos_creados<cantidadPuntos:
        posicion_punto = [random.randint(0,filas-1),random.randint(0,columnas-1)]
        if posicion_jugador!=posicion_punto:
            nivel[(posicion_punto[0])][(posicion_punto[1])] = "💡"
            puntos_creados +=1

#-----------Programa principal -----------
import random
import time
import os

#Inicio del juego - menú
global datos
datos = iniciarJuego()
iniciarNivel()



#Anotaciones:
#limitar la cantidad de movimientos para añadir dificultad ⌛
#Generar puntos por los que el jugador deba pasar ✔


#Sugerencias y revisiones:
#Esto de acá abajo se puede hacer tanto como no
#*Añadir una opción de encender luz para evitar que se pueda resolver recorriendo todo aleatoriamente*