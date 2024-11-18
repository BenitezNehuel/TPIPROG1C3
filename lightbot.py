def iniciarJuego():
    salir = False
    while salir == False:
        print("🤖 LightBot 💡")
        print("1) Cargar partida")
        print("2) Reiniciar progreso")
        print("3) Salir")
        opcion = str(input("-> "))
        match opcion:
            case "1":
                return cargarEstadisticas()
            case "2":
                return reiniciarEstadisticas()
            case "3":
                salir==False #Hay que conectarlo al menú

def reiniciarEstadisticas():
    estadisticas = open("estadisticas.txt", "w")
    nivel = 0
    luces_conseguidas = 0
    tiempo_jugado = 0
    estadisticas.write("nivel "+str(nivel)+"\nluces_conseguidas "+str(luces_conseguidas)+"\ntiempo_jugado "+str(tiempo_jugado))
    estadisticas.close()

def cargarEstadisticas():
    estadisticas = open("estadisticas.txt", "r")
    datos = {}
    estadisticas_separadas = estadisticas.readlines()
    for linea in estadisticas_separadas:
        clave = (linea.strip().split())[0]
        valor = (linea.strip().split())[1]
        datos[clave] = valor
    estadisticas.close()
    print(datos)
    return datos

def crearNivel(posicion_jugador):
    nivel = [["⬜" for i in range(columnas)] for j in range(filas)]
    nivel[posicion_jugador[0]][posicion_jugador[1]] = "🤖"
    return nivel

def mostrarNivel():
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
                nivel[posicion_jugador[0]][posicion_jugador[1]] = "🤖"
                mostrarNivel()
                print(posicion_jugador)
            case 2: #Izquierda
                posicion_jugador[1] = posicion_jugador[1]-1
                nivel[posicion_jugador[0]][posicion_jugador[1]] = "🤖"
                mostrarNivel()
                print(posicion_jugador)
            case 3: #Arriba
                posicion_jugador[0] = posicion_jugador[0]-1
                nivel[posicion_jugador[0]][posicion_jugador[1]] = "🤖"
                mostrarNivel()
                print(posicion_jugador)
            case 4: #Abajo
                posicion_jugador[0] = posicion_jugador[0]+1
                nivel[posicion_jugador[0]][posicion_jugador[1]] = "🤖"
                mostrarNivel()
                print(posicion_jugador)
            case _:
                print("La secuencia no es correcta")
                break

def crearPuntos(cantidadPuntos,posicion_jugador):
    puntos_creados = 0
    while puntos_creados<cantidadPuntos:
        posicion_punto = [random.randint(0,filas-1),random.randint(0,columnas-1)]
        if posicion_jugador!=posicion_punto:
            nivel[(posicion_punto[0])][(posicion_punto[1])] = "💡"
            puntos_creados +=1

#-----------Programa principal -----------
import random #Preguntar a la profe si se puede usar.

#Inicio del juego - menú
datos = iniciarJuego()

#Definir area del nivel
global filas
global columnas


filas= int(datos["nivel"])

columnas= int(datos["nivel"])


#Cargar posicion inicial del jugador
#¿Hacer aleatoria o iniciar en niveles fijos?
posicion_jugador = [0,0]
nivel = crearNivel(posicion_jugador)

#Crear puntos por los que el jugador debe pasar.
cantidadPuntos = random.randint(0,4)
crearPuntos(cantidadPuntos,posicion_jugador)

salir = False
mostrarNivel()
while not salir:
    print("1) Derecha.\n2) Izquierda.\n3)Arriba.\n4) Abajo.\n10) Salir.")
    movimientos = input("Ingrese la secuencia de movimientos separadas por espacios")
    if movimientos != "10":
        movimiento(movimientos,posicion_jugador)
    else:
        salir = True

#Anotaciones:
#limitar la cantidad de movimientos para añadir dificultad
#Generar puntos por los que el jugador deba pasar


#Sugerencias y revisiones:
#Al final si hice lo de abajo Xd
#Tal vez crear un algoritmo que verifique la creación de puntos aleatorios <- No es buena idea para este trabajo
#*Añadir una opción de encender luz para evitar que se pueda resolver recorriendo todo aleatoriamente*