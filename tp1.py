import random

##  MATRICES :

def mezclar_matriz(matriz:list )-> list:
    '''
    PRE: Recibe la una matriz/tablero
    POST: Una vez que tiene la matriz distribuye cada elemento , agarro dos elementos y los invierte de lugar
          y asi mezcla de manera aleatoria los elementos de la matriz
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            n1 = random.randrange(len(matriz))
            n2 = random.randrange(len(matriz))
            n3 = random.randrange(len(matriz))
            n4 = random.randrange(len(matriz) - 1)
            elemento1 = matriz[n1].pop(n2)
            elemento2 = matriz[n3].pop(n4)
            matriz[n1].append(elemento2)
            matriz[n3].append(elemento1)
    return matriz

def generar_matriz(n:int )->list:
    '''
    PRE: Recibe un numero n que le indica una el rango de la matriz nxn
    POST: Devuelve una matriz del rango que se ingreso , con numeros duplicados
    '''
    matriz = []
    cols = int(n / 2)
    for i in range(n):
        matriz.append([])
        for j in range(cols):
            rand_n = random.randrange(1,50)
            matriz[i].append([rand_n, "x"])
            matriz[i].append([rand_n, "x"])
    matriz = mezclar_matriz(matriz)
    return matriz

## JUEGO --> caracteristicas del juego y del jugador:

def instrucciones()->None:
    print("\t\t##########\nINSTRUCCIONES / REGLAS:")
    print("\nMEMOTEST")
    print("\n - A cada jugador se le asigna un tablero y debe adivinar todos los pares de numeros")
    print("\n - Cada ves que un jugador acierte el par , sigue jugando")
    print("\n - Cada ficha se da vuelta cuando el jugador elige las coordenadas , poniendo la fila y luego la columna ")
    print("\n - Cada jugador al empezar el turno tira un dado el cual puede tocarle una carta")
    print("\n - Las cartas se utilizan al finalizar el turno")
    print("\n       EXPLICACION DE LAS CARTAS : ")
    print(" - Existen 4 cartas cada una tiene una habilidad y un porcentaje de salida :")
    print(f"\n\t\tLa habilidad y los porcentajes de cada carta son: \n")
    print(f"\tREPLAY -- podes volver a jugar ---> 25% \n\tLAYOUT -- mezcla el tablero que debe adivinar el contrario ---> 12.5%")
    print(f"\tTOTI -- Espeja el tablero que debe adivinar el contrario ---> 20% \n\tFATALITY -- transpone el tablero que debe adivinar el contrario ---> 10%")
    print("\n### VAMOS A JUGAR ###")

def memotest_jugar(n_partidas: int)->tuple:
    memotest = input("\nQueres jugar al memotest ? (si/no) : ")
    while not (memotest == "si" or memotest == "no"):
        memotest = input("\ningrese si quiere o no jugar: ")
    if memotest == "si":
        instrucciones()
        memotest = True
        n_partidas = n_partidas
        return (memotest, n_partidas)
    else :
        memotest = False
        n_partidas = 4
        return (memotest, n_partidas)

def nombre_jugadores()->str:
    '''
    PRE: Pide el ingreso de los nombres 
    POST:  Devuelve los nombres de cada jugador 
    '''
    nombre = input("\nIngresar nombre del jugador : ")
    while not nombre.isalpha():
        nombre = input("\nIngresa un nombre o apodo no numeros (sin numero): ")
    return nombre.capitalize()

def duracion_juego()->int:
    '''
    PRE: Pide al usuario ingresar en que nivel de juego se desarrollara 
    POST:  Devuelve el valor que luego sera usado para crear la matriz nxn
    '''
    duracion = input("\nNivel de juego desea jugar 4/8/12, ponga el numero de duracion: ")
    while not (duracion == "4" or duracion == "8" or duracion == "12"):
        print("\n usted no esta ingresando ninguno de los niveles asignados, ingrese los pedidos...")
        print("\n   ###         son 4/8/12       ###      ")
        duracion = input("\nNivel de juego desea jugar 4/8/12, ponga el numero de duracion: ")
    return int(duracion)

def contador(inicio: int)-> int:
    '''
    PRE: Ingresa el rango del tablero
    POST:  Con el rango del tablero , asigna la cantidad de fichas que se deben adivinar
    '''
    if inicio == 12:
        return 144
    elif inicio == 8:
        return 64
    else : return 16

def ganar(tablero: list )-> bool:
    '''
    PRE: Recibe el tablero de los jugadores
    POST:  Asigna un contador y compara la cantidad de fichas que se adivinaron con las que necesita para 
        ganar , si completo todo el tablero , gana, sino el juego sigue.
    '''
    cant = 0
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j][0] == 0:
                cant += 1
    if cant == contador(len(tablero)):
        return True
    else: return False

def partida(tableroA: list, tableroB: list, cartas_J_A: list, cartas_J_B: list,duracion: int, usuario_A: str,usuario_B: str,ranking: list,juego: bool)->tuple:
    '''
    PRE: Meto todos los datos de la partida que se va a jugar
    POST: Devuelve si la partida termina o no, y el ranking de los jugadores
    '''
    ## PARTIDA EN PROGRESO --> TURNOS 
    print(f"\n   #####   TURNO DE {usuario_A}   #####  ")
    print_tablero(tableroB, duracion)
    ## antes de arrancar el turno : tiro dado a ver si le toca cartas:

    cartas_J_A = tirar_dado(cartas_J_A)

    ## inicio el turno:
    ## separo los valores que me devuelve el turno A en caso de usar cartas
    jugadorA = turno(tableroB,tableroA,cartas_J_A)
    tablero_jugadorA = jugadorA[0]
    cartas_J_A = jugadorA[1]  
    tableroA = jugadorA[2]

    ## si gano hago finalizar el juego

    if ganar(tablero_jugadorA) == True:
                print(f"\t##\t¡¡¡GANADOR : {usuario_A}!!!\t###\n")
                ranking = sumar_victoria(usuario_A, ranking)
                juego = False

    else :
                ## si no gano el jugador A paso al turno del B:
                
        print(f"\n   #####   TURNO DE {usuario_B}   #####  ")
        print_tablero(tableroA, duracion)

        cartas_J_B = tirar_dado(cartas_J_B)

        ## separo los valores que me devuelve el turno B en caso de usar cartas y lo que modifica
        jugadorB = turno(tableroA,tableroB, cartas_J_B)
        tablero_jugadorB = jugadorB[0]
        cartas_J_B = jugadorB[1]
        tableroB = jugadorB[2]

        if ganar(tablero_jugadorB) == True:
            print(f"\t##\t¡¡¡GANADOR : {usuario_B}!!!\t###\n")
            ranking = sumar_victoria(usuario_B, ranking)
            juego = False
        
        else : 
            juego = True
        
    datos_juego = (juego, ranking)

    return datos_juego

def turno(tablero: list ,tablero_contrario:list, mazo: list)->tuple:
    '''
    PRE: Se ingresa el jugador , el tablero que debe adivinar y su tablero
    POST: Se desarrolla el turno del jugador y se aplican las cartas , en caso de tener alguna .
    '''
    termina_turno = False
    while not termina_turno:
        cord_correctas = False 
        while not cord_correctas:
            fila_1 = numero_coordenada_fila(tablero)
            columna_1 = numero_coordenada_columna(tablero)
            num_1 = tablero[fila_1 -1][columna_1 - 1][0]
            print(f"\nTu ficha elegida es {ficha_elegida(tablero, fila_1,columna_1)}\n")
            
            mostrar_fichas(tablero, fila_1,columna_1)

            fila_2 = numero_coordenada_fila(tablero)
            columna_2 = numero_coordenada_columna(tablero)
            num_2 = tablero[fila_2 -1][columna_2 - 1][0]
            print(f"\nTu ficha elegida es {ficha_elegida(tablero, fila_2,columna_2)}\n")

            mostrar_fichas(tablero, fila_1, columna_1, fila_2, columna_2)

            cord_correctas = chequear_fil_col(fila_1,columna_1,fila_2,columna_2)

        ## Chequea si el jugador gana el juego al finalizar su turno 
        if chequear_fichas(num_1,num_2) == True:
            modifico_tablero(tablero, fila_1,columna_1,fila_2,columna_2,num_1,num_2)
            if ganar(tablero) == True:
                termina_turno = True

        ## Si termina el turno puedo usar alguna carta
        elif mazo:
            print("\nPodes usar una de tus cartas: \n")
            for element in mazo:
                print(f" - {element}")
            c_elegida = carta_elegida()
            c_elegida.lower
            ## Bucle para elegir o no carta
            if c_elegida == "n":
                termina_turno = True
            else :
                if c_elegida == "replay":
                    print(f"\nTu carta elegida fue : {c_elegida} -> ###\tVolve a jugar !\t###\n")
                    mazo = eliminar_c_elegida(c_elegida, mazo)
                    termina_turno = False
                elif c_elegida == "layout":
                    print(f"\nTu carta elegida fue : {c_elegida} -> ###\tAhora se mezclo todo el tablero del contrario\t###\n")
                    mazo = eliminar_c_elegida(c_elegida, mazo)
                    tablero_contrario = mezclar_matriz(tablero_contrario)
                    termina_turno = True
                elif c_elegida == "toti":
                    print(f"\nTu carta elegida fue : {c_elegida} -> ###\tSe espeja el tablero que tiene que adivinar el oponente : \t###\n")
                    mazo = eliminar_c_elegida(c_elegida, mazo)
                    toti(tablero_contrario)
                    termina_turno = True
                elif c_elegida == "fatality":
                    print(f"\nTu carta elegida fue : {c_elegida} -> ###\tSe transpone el tablero que debe adivinar el oponente: \t###\n")
                    mazo = eliminar_c_elegida(c_elegida, mazo)
                    tablero_contrario = fatality(tablero_contrario)
                    termina_turno = True

        ## Si no gana el juego , no usa ninguna carta y no adivino fichas, se da por terminado el turno 
        else : 
            tablero[fila_1 -1][columna_1 - 1][0] = num_1 
            tablero[fila_2 -1][columna_2 - 1][0] = num_2
            termina_turno = True

    return tablero, mazo, tablero_contrario

def carta_elegida()->str:
    '''
    PRE: Consulta para la eleccion de una carta
    POST: Retorna la carta elegida , en caso de que sea 'n' no se usan cartas.
    '''
    c = input("\nEscribi que carta queres usar , si no queres usar ninguna apreta la letra 'n' + enter : ")
    c = c.lower()
    while not (c == "replay" or c == "toti" or c == "fatality" or c == "layout" or c == "n"):
        c = input("\nEscribi que carta queres usar , si no queres usar ninguna apreta la letra 'n' + enter : ")
        c = c.lower()
    return c


## RANKING : 
def chequear_usuarios(usuario: str, ranking: list)->list:
    '''
    PRE: Se ingresa el usuario y el ranking 
    POST: Verifica si el usuario ya se encontraba en el ranking , si no estaba lo añade
    '''
    no_existe = True
    for i in range(len(ranking)):
        if ranking[i][0] == usuario:
            no_existe = False
    while no_existe:
        ranking.append([usuario, 0])
        no_existe = False
    return ranking

def sumar_victoria(usuario:str, ranking:list)->list:
    '''
    PRE: Se ingresa el ranking y el usuario que gano
    POST: Se le suma la victoria al usuario ganador
    '''
    for i in range(len(ranking)):
        if ranking[i][0] == usuario:
            ranking[i][1] += 1
    return ranking

def mostrar_ranking(ranking:list)->None:
    '''
    PRE: Ingresa el ranking 
    POST: Muestra el ranking por pantalla
    '''
    print("\nEl tablero de victorias es : \n")
    for i in range(len(ranking)):
        print(f"{ranking[i][0]} = {ranking[i][1]}")

## CARTAS :
def tirar_dado(mazo: list)->list:
    '''
    PRE: Se ingresa el mazo del jugador que esta jugando
    POST: Se tiran los dados y si le toca , la carta ingresa en su mazo , sino se retorna el mazo como estaba.
    '''
    print("\n###\tTIRAR EL DADO\t###")
    tirar = input("\ningrese una letra y aprete enter para tirar el dado: ")
    while not tirar.isalpha():
        tirar = input("\nLe pedi que ingrese una letra : ")
    if tirar: 
        dado = random.randrange(1,5)
        dado2 = int(random.random() * 100)
        if dado == 1: ## carta replay --> otro turno 
            if dado2 <= 100: ## --> porcentaje 25 porciento
                print("\nLe toco la carta replay")
                mazo.append("replay")
                return mazo
            else : 
                print("\nLastima no te toco nada")
                return mazo 
        elif dado == 2:  ## layout --> redistribuye todo 
            if dado2 <= 50:  ## --> porcentaje 12.5 porciento
                print("\nLe toco la carta layout")
                mazo.append("layout")
                return mazo
            else : 
                print("\nLastima no te toco nada")
                return mazo
        elif dado == 3: ## toti --> espeja el tablero
            if dado2 <= 80: ## --> porcentaje 20 porciento
                print("\nLe toco la carta toti")
                mazo.append("toti")
                return mazo
            else : 
                print("\nLastima no te toco nada")
                return mazo
        elif dado == 4: ## fatality --> traspone el tablero
            if dado2 <= 40: ## --> porcentaje 10 porciento
                print("\nLe toco la carta fatality")
                mazo.append("fatality")
                return mazo
            else : 
                print("\nLastima no te toco nada")
                return mazo

def eliminar_c_elegida(carta:str, mazo: list)-> list:
    '''
    PRE: Recibe la carta que se uso y el mazo del jugador que juega 
    POST: Una vez que se selecciono la carta que iba a usar , esta funcion la elimina del mazo
    '''
    for i in range(len(mazo)):
        if mazo[i] == carta:
            mazo.pop(i)
    return mazo

def toti(m:list)->None:
    '''
    PRE: Se ingresa el tablero que debe adivinar el contrario
    POST: Le hace print al tablero ingresado espejando las columnas o las filas, dependiendo del azar.
    '''
    ## numero aleatorio del 1 al 2 
    aleatorio = random.randrange(1,3)
    if aleatorio == 1:
    ## --------------> asi invierto las columnas:
        col_invertida = []
        for i in range(len(m)):
            col_invertida.append(m[i][::-1])
        print("\nEspejismo de columnas: \n")
        print_tablero(col_invertida, len(col_invertida), "visible")
    ## ------------->  invertir filas:
    else:
        fil_invertido = m[::-1]
        print("\nEspejismo de filas: \n")
        print_tablero(fil_invertido, len(fil_invertido), "visible")

def fatality(m:list)->list:
    '''
    PRE: Recibe el tablero que debe adivinar el contrario
    POST: Devuelve el tablero inviertiendo las filas por columnas
    '''
    transpuesta = []
    for i in range(len(m)):
        transpuesta.append([])
        for j in range(len(m)):
            transpuesta[i].append(m[j][i])
    return transpuesta

## FICHAS Y TABLERO   ---> todo lo que tiene que ver con el tablero de cada jugador :

def ficha_elegida(tablero: list, fila: int, columna: int)->int:
    '''
    PRE: Se ingresa el tablero , la fila y columna elegida
    POST: Devuelve el valor de la coordenada elegida 
    '''
    return tablero[fila-1][columna-1][0]

def mostrar_fichas(tablero: list, fila1:int, columna1: int, fila2:int = 0, columna2: int = 0)->list:
    '''
    PRE: Recibe el tablero que debe adivinar el jugador que esta en turno 
    POST: Muestra las fichas elegidas, "Se dan vuelta" las fichas.
    '''
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

def numero_coordenada_fila(m: list)->int:
    '''
    PRE: Le pido la coordenada de la fila al usuario que esta en juego
    POST: Chequea el dato ingresado y solo retorna el valor si es numerico
    '''
    fila = input("\n -> ingrese la fila: ")
    while not (fila.isnumeric() and 0 < int(fila) <= len(m)):
        print(f"\nLA COORDENADA SE PONE EN NUMERO y entre 0-{len(m)}")
        fila = input("ingrese la fila: ")
    return int(fila)

def numero_coordenada_columna(m: list)->int:
    '''
    PRE: Le pido la coordenada de la columna al usuario que esta en juego
    POST: Chequea el dato ingresado y solo retorna el valor si es numerico
    '''
    columna = input("\n -> ingrese la columna: ")
    while not (columna.isnumeric() and 0 < int(columna) <= len(m)):
        print(f"\nLA COORDENADA SE PONE EN NUMERO  y entre 0-{len(m)} ")
        columna = input("ingrese la columna: ")
    return int(columna)

def chequear_fil_col(fil1: int, col1: int, fil2: int, col2: int)->bool:
    '''
    PRE: Se ingresan los datos de las coordenadas elegidas
    POST: Se comparan las coordenadas y si son las mismas se pide volver a ingresar coordenadas
    '''
    if fil1 == fil2 and col1 == col2:
        print("\nPusiste el mismo lugar")
        print("\ningresa distintas coordenadas")
        return False
    else : return True

def chequear_fichas(ficha_1:int , ficha_2: int)->bool:
    '''
    PRE: Ingresa las fichas elegidas
    POST: Compara el valor de las fichas, si son las mismas el turno sigue , sino se termina el turno.
    '''
    if ficha_1 == ficha_2:
        return True
    else: 
        print("\nNo son las mismas proba mas tarde\n")
        
        return False

def modifico_tablero(tablero:list, fil1:int, col1:int, fil2:int,col2:int, n1:int, n2:int)->list:
    '''
    PRE: Recibe el tablero y las fichas en caso de haber acertado
    POST: Invierte las fichas que se adivinaron a su valor y el segundo valor que se convierte en 0, 
    se utiliza para aplicar un contador en caso de que todas las fichas tienen el valor 0, el jugador en turno
    gana.
    '''
    tablero[fil1 -1][col1 - 1][0] = 0
    tablero[fil2 -1][col2 - 1][0] = 0
    tablero[fil1 -1][col1 - 1][1] = n1
    tablero[fil2 -1][col2 - 1][1] = n2
    return tablero

## ----------> VISIBILIDAD DEL TABLERO : 

def print_tablero(matriz:list, rango:int, visibilidad: str = "oculto")->None:
    '''
    PRE: Recibe un tablero
    POST: Hace visible el tablero , o oculta sus fichas, dependiendo en que momento de la partida este,
    '''
    if visibilidad == "visible":
        for i in range(rango):
            for j in range(rango):
                print(matriz[i][j][0], end=" ")
            print("\n")
    else :
        for i in range(rango):
            for j in range(rango):
                print(matriz[i][j][1], end=" ")
            print("\n")

## PROGRAMA PRINCIPAL

def main()->None:
    ranking = []
    memotest = True
    n_partidas = 0
    while n_partidas < 4:

                ## MENU :
        if n_partidas == 0:
            memotest_juego = memotest_jugar(n_partidas)
            memotest = memotest_juego[0]
            n_partidas = memotest_juego[1]
        ## --> MUESTRO EL SCORE DE PARTIDAS ANTERIORES: 
        else :
            mostrar_ranking(ranking)
            memotest_juego = memotest_jugar(n_partidas)
            memotest = memotest_juego[0]
            n_partidas = memotest_juego[1]

        while memotest:
            ## --> SOLICITO EL NOMBRE DE CADA JUGADOR Y LE ASIGNO SUS TABLEROS Y CARTAS:
            usuario_A = nombre_jugadores()
            print("\n###\tOponente\t###")
            usuario_B = nombre_jugadores() 

            duracion = duracion_juego()
            tableroA = generar_matriz(duracion)
            tableroB = generar_matriz(duracion)
            cartas_J_A = []
            cartas_J_B = []

            ranking = chequear_usuarios(usuario_A, ranking)
            ranking = chequear_usuarios(usuario_B, ranking)

            ## --> MUESTRO A CADA JUGADOR EL TABLERO QUE DEBE ADIVINAR:
            print(f"\nEl tablero de {usuario_A} que tiene que adivinar es : \n")
            print_tablero(tableroB, duracion, "visible")
                
            print(f"El tablero de {usuario_B} que tiene que adivinar es : \n")
            print_tablero(tableroA, duracion, "visible")

            ## --> EMPEZAR JUEGO :
            juego = True
            while juego:

                juego_y_ranking = partida(tableroA, tableroB, cartas_J_A, cartas_J_B,duracion, usuario_A,usuario_B,ranking, juego)
                juego = juego_y_ranking[0]
                ranking = juego_y_ranking[1]

            memotest = False
        n_partidas +=1

main()

