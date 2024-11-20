import os

#Importar juegos:
from lightbot.lightbot import lightBot
from escapismo.juegoEscapismo import escapismo
from figuras_geometricas.figurasGeometricas import figurasGeometricas

#Mostrar menú
def main():
    salir = False
    while salir==False:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Ingrese el número correspondiente al juego que quiera iniciar:")
        print("1) Juego de escapismo.")
        print("2) LightBot.")
        print("3) Figuras geometricas.")
        print("4) Salir.")
        opcion = str(input("-> "))
        match opcion:
            case "1":
                os.system("cls")
                escapismo()
                os.system("cls")
            case "2":
                os.system("cls")
                lightBot()
                os.system("cls")
            case "3":
                os.system("cls")
                figurasGeometricas()
                os.system("cls")
            case "4":
                salir = True
            case _:
                print("Opción no válida.")

if __name__ == "__main__":
    main()