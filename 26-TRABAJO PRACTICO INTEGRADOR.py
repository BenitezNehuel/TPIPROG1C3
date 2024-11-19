
print("FIGURAS GEOMETRICAS PLANAS")
print()
print( "El presente codigo les mostrara a las (seis) figuras planas de lados","\n",
"rectos mas comunes y usuales de la geometria, siga las instrucciones","\n",
"y realice algunos calculos de sus perimetros y areas")
print()
print("Elija una de las figuras de las referencias")
print("Referencias: 1-cuadrado, 2-rectángulo, 3-triangulo, 4-rombo, 5-paralelogramo, 6-trapecio")
print()
tipo_de_figura=int(input("Ingrese la figura que quieras conocer: "))

f=11
c=11
cont=1

lista=["🟩","🟧","🔺","🔷","📦","🟥","💚"]

try:
    while tipo_de_figura>6 or tipo_de_figura<1:
        print("Referencia incorrecta, el numero debe ser del 1 al 6:")
        tipo_de_figura = int(input("Ingrese la figura que quieras conocer: "))

except ValueError:
    print("Referencia incorrecta, el numero debe ser del 1 al 6")
    tipo_de_figura = int(input("Ingrese la figura que quieras conocer: "))

try:
    while 1<=cont<=6:
        if tipo_de_figura==1:
            print()
            print("Ha elegido el CUADRADO")
            print("Tiene sus cuatro lados IGUALES")
            print("Tiene sus cuatro angulos IGUALES de 90ª")
            print("Su forma es: La coloreada en verde", lista[0])
            print()

            matriz=[["⬜" for i in range (c)] for j in range (f)]
            for i in range (f):
                for j in range (c):
                    print(matriz[i][j],end=" ")
                print()

                for i in range(2, f-2):
                    for j in range(2, c-2):
                        matriz[i][j] = lista[0]
                        matriz[5][0] = "L1"
                        matriz[1][5] = "L2"
                        matriz[5][10] = "L3"
                        matriz[10][5] = "L4"
            print()
            print("Vamos a calcular el perimetro y el area del CUADRADO")
            print()
            lado = float(input("Ingrese la longitud del lado: "))
            perimetro = 4 * lado
            print()
            print("El PERIMETRO del cuadrado es:", perimetro,"[m]")
            area = lado ** 2
            print("El AREA del cuadrado es:", area,"[m2]")
            cont += 1
            print()
            tipo_de_figura = int(input("Ingrese la figura que quieras conocer: "))


        if tipo_de_figura==2:
            print()
            print("Ha elegido el RECTANGULO")
            print("Tiene dos lados cortos IGUALES entre si")
            print("Tiene dos lados largos IGUALES entre si")
            print("Tiene los 4 angulos IGUALES de 90º")
            print("Su forma es: La coloreada en naranja", lista[1])
            print()

            matriz=[["⬜" for i in range (c)] for j in range (f)]
            for i in range (f):
                for j in range (c):
                    print(matriz[i][j],end=" ")
                print()

                for i in range(3, f-3):
                    for j in range(2, c-2):
                        matriz[i][j] = lista[1]
                        matriz[5][0] = "L1"
                        matriz[1][5] = "L2"
                        matriz[5][10] = "L1"
                        matriz[9][5] = "L2"

            print()
            print("Vamos a calcular el perimetro y el area del RECTANGULO")
            print()
            lado1 = float(input("Ingrese la longitud del lado1: "))
            lado2 = float(input("Ingrese la longitud del lado2: "))
            perimetro = (lado1*2) + (lado2*2)
            print()
            print("El PERIMETRO del rectangulo es:", perimetro, "[m]")
            area = (lado1*lado2)
            print("El AREA del rectangulo es:", area, "[m2]")
            cont += 1
            print()
            tipo_de_figura = int(input("Ingrese la figura que quieras conocer: "))

        if tipo_de_figura==3:
            print()
            print("Ha elegido el TRIANGULO")
            print("La clasificacion segun sus lados es:")
            print("Equilatero: Tiene sus tres lados y angulos IGUALES")
            print("Isosceles: Tiene dos lados IGUALES y uno DESIGUAL y tiene dos angulos IGUALES y uno DESIGUAL")
            print("Escaleno: Tiene sus tres lados DESIGUALES y sus tres angulos DESIGUALES")
            print("Su forma es: La coloreada en rojo",lista[2])
            print()

            matriz=[["⬜" for i in range (c+2)] for j in range (f)]
            for i in range (f):
                for j in range (c+2):
                    print(matriz[i][j],end=" ")
                print()
                for i in range(3,4,1):
                    for j in range(6,7,1):
                        matriz[i][j] = lista[2]
                for i in range(4,5,1):
                    for j in range(5,8,1):
                        matriz[i][j] = lista[2]
                for i in range(5, 6, 1):
                    for j in range(4, 9, 1):
                        matriz[i][j] = lista[2]
                for i in range(6, 7, 1):
                    for j in range(3, 10, 1):
                        matriz[i][j] = lista[2]
                for i in range(7, 8, 1):
                    for j in range(2, 11, 1):
                        matriz[i][j] = lista[2]
                        matriz[4][2] = "L1"
                        matriz[4][10] = "L2"
                        matriz[4][12] = " h"
                        matriz[9][6] = "L3"

            print()
            print("Vamos a calcular el perimetro y el area del TRIANGULO")
            print()
            lado1 = float(input("Ingrese la longitud del lado1: "))
            lado2 = float(input("Ingrese la longitud del lado2: "))
            base = float(input("Ingrese la longitud de la lado 3 o base: "))
            altura = float(input("Ingrese la longitud de la altura: "))

            perimetro = lado1 + lado2 + base
            print()
            print("El PERIMETRO del triangulo es:", perimetro, "[m]")
            area = (base * altura) / 2
            print("El AREA del triangulo es:", area, "[m2]")
            cont += 1
            print()
            tipo_de_figura = int(input("Ingrese la figura que quieras conocer: "))

        if tipo_de_figura==4:
            print()
            print("Ha elegido el ROMBO")
            print("Tiene sus cuatro lados IGUALES")
            print("Tiene dos angulos IGUALES y menorea a 90ª")
            print("Tiene dos angulos IGUALES y mayores a 90ª")
            print("Tiene una diagonal maypr y una diagonal menor que son DESIGUALES entre si")
            print("Su forma es: La coloreada en azul", lista[3])
            print()

            matriz = [["⬜" for i in range(c + 2)] for j in range(f+2)]
            for i in range(f):
                for j in range(c + 2):
                    print(matriz[i][j], end=" ")
                print()
                for i in range(1, 2, 1):
                    for j in range(6, 7, 1):
                        matriz[i][j] = lista[3]
                    for i in range(2, 3, 1):
                        for j in range(5, 8, 1):
                            matriz[i][j] = lista[3]
                    for i in range(3, 4, 1):
                        for j in range(4, 9, 1):
                            matriz[i][j] = lista[3]
                    for i in range(4, 5, 1):
                        for j in range(3, 10, 1):
                            matriz[i][j] = lista[3]
                    for i in range(5, 6, 1):
                        for j in range(2, 11, 1):
                            matriz[i][j] = lista[3]
                    for i in range(6, 7, 1):
                        for j in range(3, 10, 1):
                            matriz[i][j] = lista[3]
                    for i in range(7, 8, 1):
                        for j in range(4, 9, 1):
                            matriz[i][j] = lista[3]
                    for i in range(8, 9, 1):
                        for j in range(5, 8, 1):
                            matriz[i][j] = lista[3]
                    for i in range(9, 10, 1):
                        for j in range(6, 7, 1):
                            matriz[i][j] = lista[3]
                            matriz[2][3] = "L1"
                            matriz[2][9] = " L1"
                            matriz[8][9] = " L1"
                            matriz[8][3] = "L1"
                            matriz[1][8] = "Dm"
                            matriz[9][2] = "dm"

            print()
            print("Vamos a calcular el perimetro y el area del ROMBO")
            print()
            lado = float(input("Ingrese la longitud del lado: "))
            diagonal_mayor = float(input("Ingrese la longitud de la diagonal mayor: "))
            diagonal_menor = float(input("Ingrese la longitud de la diagonal menor: "))

            perimetro = lado * 4
            print()
            print("El PERIMETRO del rombo es:", perimetro, "[m]")
            area = (diagonal_mayor * diagonal_menor)/2
            print("El AREA del rombo es:", area, "[m2]")
            cont += 1
            print()
            tipo_de_figura = int(input("Ingrese la figura que quieras conocer: "))

        if tipo_de_figura==5:
            print()
            print("Ha elegido el PARALELOGRAMO")
            print("Tiene dos lados cortos IGUALES entre si")
            print("Tiene dos lados largos IGUALES entre si")
            print("Tiene dos angulos IGUALES y menorea a 90ª")
            print("Tiene dos angulos IGUALES y mayores a 90ª")
            print("Su forma es: La coloreada en marron claro",lista[4])
            print()

            matriz=[["🟪" for i in range (c+2)] for j in range (f-1)]
            for i in range (f-1):
                for j in range (c+2):
                    print(matriz[i][j],end=" ")
                print()
                for i in range(3,7,1):
                    for j in range(2,11,1):
                        if ((i+j==8)):
                            matriz[i][j] = lista[4]
                        if ((i+j==9)):
                            matriz[i][j] = lista[4]
                        if ((i+j == 10)):
                            matriz[i][j] = lista[4]
                        if ((i+j == 11)):
                            matriz[i][j] = lista[4]
                        if ((i+j == 12)):
                            matriz[i][j] = lista[4]
                        if ((i+j == 13)):
                            matriz[i][j] = lista[4]
                            matriz[4][2] = " L1"
                            matriz[1][8] = "L2"
                            matriz[5][10] = "L1"
                            matriz[8][4] = "L2"
                            matriz[9][5] = "b"
                            matriz[4][0] = " h"

            print()
            print("Vamos a calcular el perimetro y el area del PARALELOGRAMO")
            print()
            lado1 = float(input("Ingrese la longitud del lado1: "))
            lado2 = float(input("Ingrese la longitud del lado2: "))
            base = float(input("Ingrese la longitud de la base: "))
            altura = float(input("Ingrese la longitud de la altura: "))

            perimetro = (lado1*2) + (lado2*2)
            print()
            print("El PERIMETRO del paralelogramo es:", perimetro, "[m]")
            area = (base * altura)
            print("El AREA del paralelogramo es:", area, "[m2]")
            cont += 1
            print()
            tipo_de_figura = int(input("Ingrese la figura que quieras conocer: "))

        if tipo_de_figura==6:
            print()
            print("Ha elegido el TRAPECIO")
            print("Tiene cuatro lados, estos pueden ser: ")
            print("Cuatro lados DESIGUALES entre si")
            print("Tres lados IGUALES entre si y uno DESIGUAL")
            print("Dos lados IGUALES entre si y dos lados DESIGUALES a los anteriores e IGUALES entre si")
            print("Su forma es: La coloreada en rojo",lista[5])
            print()

            matriz=[["🟦" for i in range (c+2)] for j in range (f)]
            for i in range (f):
                for j in range (c+2):
                    print(matriz[i][j],end=" ")
                print()
                for i in range(3, 2,-1):
                    for j in range(5, 8, 1):
                       matriz[i][j] = lista[5]
                for i in range(4, 3,-1):
                    for j in range(4, 9, 1):
                       matriz[i][j] = lista[5]
                for i in range(5, 4,-1):
                    for j in range(3, 10, 1):
                       matriz[i][j] = lista[5]
                for i in range(6, 5,-1):
                    for j in range(2, 11, 1):
                       matriz[i][j] = lista[5]
                       matriz[1][6] = "L2"
                       matriz[8][6] = "L4"
                       matriz[4][0] = " h"
                       matriz[4][2] = " L1"
                       matriz[4][10] = "L3"

            print()
            print("Vamos a calcular el perimetro y el area del TRAPECIO")
            print()
            lado1= float(input("Ingrese la longitud del lado1: "))
            lado2 = float(input("Ingrese la longitud del lado2: "))
            lado3 = float(input("Ingrese la longitud del lado3: "))
            lado4 = float(input("Ingrese la longitud del lado4: "))
            base_menor = float(input("Ingrese la longitud del base menor: "))
            base_mayor = float(input("Ingrese la longitud del base mayor: "))
            altura = float(input("Ingrese la longitud de la altura: "))

            perimetro = lado1 + lado2 + lado3 + lado4
            print()
            print("El PERIMETRO del trapecio es:", perimetro, "[m]")
            area = (((base_menor + base_mayor)/2) * altura)
            print("El AREA del trapecio es:", area, "[m2]")
            cont += 1

    else:
        print()
        print("Ya agoto sus 6 (seis) intentos")
        print("Deje participar a otro compañero")
        print("MUCHAS GRACIAS", lista[6])

except ValueError:
        print("Ingrese un dato correcto")