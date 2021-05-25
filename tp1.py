import random
## TAREAS A REALIZAR :
## USAR LA ALEATORIEDAD Y EL MEZCLADO QUE LOGRE EN "PRUEBAS" []
##  mostrar la matriz al final del turno []
##  PENSAR LA LOGICA DE LAS CARTAS []
## ERRORES :
##  - cuando pongo un numero que no correspone al rango de la matriz crashea
##  - corroborar datos pedidos , no tengo ninguna funcion que corrobore datos de nada( nombre, numeros de col y fil ) 

##  MATRICES :

def generar_matriz(n:int )->list:
    matriz = []
    cols = int(n / 2)
    for i in range(n):
        matriz.append([])
        for j in range(cols):
            rand_n = random.randrange(1,50)
            matriz[i].append([rand_n, "x"])
            matriz[i].append([rand_n, "x"])
    for i in range(n):
        for j in range(n):
            n1 = random.randrange(n)
            n2 = random.randrange(n)
            n3 = random.randrange(n)
            n4 = random.randrange(n - 1)
            elemento1 = matriz[n1].pop(n2)
            elemento2 = matriz[n3].pop(n4)
            matriz[n1].append(elemento2)
            matriz[n3].append(elemento1)
    return matriz

## JUEGO --> caracteristicas del juego y del jugador:
def arrancar_juego()->bool:
    print("\nArrancamos...?")
    juego = input("s/n : ")
    if juego == "s":
        return True
    else: return False

def nombre_jugadores()->str:
    nombre = input("\nIngresar nombre jugador : ")

    return nombre.capitalize()

def duracion_juego()->int:
    duracion = int(input("\nNivel de juego desea jugar 4/8/12, ponga el numero de duracion: "))
    while not duracion == 4 or duracion == 8 or duracion == 12:
        print("\n usted no esta ingresando ninguno de los niveles asignados, ingrese los pedidos...")
        print("\nson 4/8/12       ###      vamoooo")
        duracion = int(input("\nNivel de juego desea jugar 4/8/12, ponga el numero de duracion: "))
    return duracion

def contador(inicio: int)-> int:
    if inicio == 12:
        return 144
    elif inicio == 8:
        return 64
    else : return 16

def ganar(tablero: list )-> bool:
    cant = 0
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j][0] == 0:
                cant += 1
    if cant == contador(len(tablero)):
        return True
    else: return False

def turno(tablero: list )->list:
    termina_turno = False
    while not termina_turno:
        cord_correctas = False 
        while not cord_correctas:
            fila_1 = int(input("\ningrese la fila: "))
            columna_1 = int(input("ingrese la columna: "))
            num_1 = tablero[fila_1 -1][columna_1 - 1][0]
            print(f"\nTu ficha elegida es {ficha_elegida(tablero, fila_1,columna_1)}\n")
            
            mostrar_fichas(tablero, fila_1,columna_1)

            fila_2 = int(input("\ningrese la fila: "))
            columna_2 = int(input("ingrese la columna: "))
            num_2 = tablero[fila_2 -1][columna_2 - 1][0]
            print(f"\nTu ficha elegida es {ficha_elegida(tablero, fila_2,columna_2)}\n")

            mostrar_fichas(tablero, fila_1, columna_1, fila_2, columna_2)


            cord_correctas = chequear_fil_col(fila_1,columna_1,fila_2,columna_2)


        if chequear_fichas(num_1,num_2) == True:
            modifico_tablero(tablero, fila_1,columna_1,fila_2,columna_2,num_1,num_2)
            if ganar(tablero) == True:
                termina_turno = True
            else : 
                termina_turno = False
        else : 
            tablero[fila_1 -1][columna_1 - 1][0] = num_1 
            tablero[fila_2 -1][columna_2 - 1][0] = num_2
            termina_turno = True

    return tablero

## RANKING : 
def chequear_usuarios(usuario: str, ranking: list)->list:
    no_existe = True
    for i in range(len(ranking)):
        if ranking[i][0] == usuario:
            no_existe = False
    while no_existe:
        ranking.append([usuario, 0])
        no_existe = False
    return ranking

def sumar_victoria(usuario:str, ranking:list)->None:
    for i in range(len(ranking)):
        if ranking[i][0] == usuario:
            ranking[i][1] += 1

def mostrar_ranking(ranking:list)->None:
    print("\n JUGADOR | VICTORIAS")
    for i in range(len(ranking)):
        print(f"{ranking[i][0]} = {ranking[i][1]}")


## CARTAS :


## FICHAS Y TABLERO   ---> todo lo que tiene que ver con el tablero de cada jugador :

def ficha_elegida(tablero: list, fila: int, columna: int)->int:
    return tablero[fila-1][columna-1][0]

def mostrar_fichas(tablero: list, fila1:int, columna1: int, fila2:int = 0, columna2: int = 0)->list:
    if fila2 == 0:
        for i in range(len(tablero)):
            for j in range(len(tablero)):
                if i == (fila1 -1) and j == (columna1 - 1):
                    print(tablero[i][j][0], end=" ")
                else : print(tablero[i][j][1], end=" ")
            print("\n")
    else : 
        for i in range(len(tablero)):
            for j in range(len(tablero)):
                if i == (fila1-1) and j == (columna1 - 1):
                    print(tablero[i][j][0], end=" ")
                elif i == (fila2-1) and j == (columna2 - 1):
                    print(tablero[i][j][0], end=" ")
                else : print(tablero[i][j][1], end=" ")
            print("\n")

def chequear_fil_col(fil1: int, col1: int, fil2: int, col2: int)->bool:
    if fil1 == fil2 and col1 == col2:
        print("\nPusiste el mismo lugar")
        print("\ningresa distintas coordenadas")
        return False
    else : return True

def chequear_fichas(ficha_1:int , ficha_2: int)->bool:
    if ficha_1 == ficha_2:
        return True
    else: 
        print("\nNo son las mismas proba mas tarde\n")
        
        return False

def modifico_tablero(tablero:list, fil1:int, col1:int, fil2:int,col2:int, n1:int, n2:int)->list:
    tablero[fil1 -1][col1 - 1][0] = 0
    tablero[fil2 -1][col2 - 1][0] = 0
    tablero[fil1 -1][col1 - 1][1] = n1
    tablero[fil2 -1][col2 - 1][1] = n2
    return tablero

## ----------> VISIBILIDAD DEL TABLERO : 

def print_tablero(matriz:list, rango:int, visibilidad: str = "oculto")->None:
    if visibilidad == "visible":
        for i in range(rango):
            for j in range(rango):
                print(matriz[i][j], end=" ")
            print("\n")
    else :
        for i in range(rango):
            for j in range(rango):
                print(matriz[i][j][1], end=" ")
            print("\n")

## PROGRAMA PRINCIPAL

def main()->None:
    ranking = []
    for i in range(4):
        juego = arrancar_juego()
        if i == 0:
            print("No hay ganadores ...")
        else :
            mostrar_ranking(ranking)
        while juego:
            print("\nEMPECEMOS A JUGAR!!!\n")

            usuario_A = nombre_jugadores()
            usuario_B = nombre_jugadores() 
            
        
            ## METO A LOS JUGADORES AL RANKING
            ranking = chequear_usuarios(usuario_A, ranking)
            ranking = chequear_usuarios(usuario_B, ranking)

            duracion = duracion_juego()

            tableroA = generar_matriz(duracion)
            tableroB = generar_matriz(duracion)
            
            print(f"\nEl tablero de {usuario_A} que tiene que adivinar es : \n")
            print_tablero(tableroB, duracion, "visible")
            
            print(f"El tablero de {usuario_B} que tiene que adivinar es : \n")
            print_tablero(tableroA, duracion, "visible")
            
            ## PARTIDA EN PROGRESO
            print(f"\n   #####   TURNO DE {usuario_A}   #####  ")
            print_tablero(tableroB, duracion)
            tablero_jugadorA = turno(tableroB)
            if ganar(tablero_jugadorA) == True:
                print(f"Ganador : {usuario_A}")
                sumar_victoria(usuario_A, ranking)
                juego = False
            else :
                print(f"\n   #####   TURNO DE {usuario_B}   #####  ")
                print_tablero(tableroA, duracion)
                tablero_jugadorB = turno(tableroA)
                if ganar(tablero_jugadorB) == True:
                    print(f"Ganador : {usuario_B}")
                    sumar_victoria(usuario_B, ranking)
                    juego = False
                    return juego
                else : 
                    juego = False
                    return juego



main()

