import os

#Importar juegos:
from lightbot.lightbot import lightBot
from escapismo.juegoEscapismo import escapismo

#Mostrar menú
def main():
    salir = False
    while salir==False:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Ingrese el número correspondiente al juego que quiera iniciar:")
        print("1) Juego de escapismo.")
        print("2) LightBot.")
        print("3) Salir.")
        opcion = str(input("-> "))
        match opcion:
            case "1":
                escapismo()
                os.system("cls")
            case "2":
                lightBot()
                os.system("cls")
            case "3":
                salir = True
            case _:
                print("Opción no válida.")

if __name__ == "__main__":
    main()