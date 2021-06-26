'''
Correcciones del tp:
- funcion contador --> "no me parece que esta modularizacion aporte mucho" [x] la saque 
- funcion ganar --> "se puede devolver el valor al que evaluo el condicional directamente" [x] la cambie por la funcion cant_fichas_acertadas 
- funcion partida:
"""codigo repetido para los dos jugadores, reepensar el flujo del juego para evitar
ciclos anidados y repeticion de código
la implementacion de turno esta bien, no entiendo la necesidad de tener partida como
un wrapper para cada uno de los turnos cuando toda la logica esta en turno.
supongo que toda esta complicacion viene del planteo del ranking""" [x] elimine funcion 'partida' , inecesario aplique la logica dentro de turno 

- funcion sumar victoria --> "modularizacion innecesaria" [x] elimine , sumo directo
- funcion eliminar carta elegida :
"""se hace una modificacion a la lista recibida por aprametro pero tambien se la devuelve???
mal uso de la mutabilidad, tampoco me parece que esta modularizacion aporte algo""" [x] elimino la carta una ves que la use en turnos

- funcion ficha elegida --> """modularizacion innecesaria""" [x] - la elimine era al dope
- mostrar ficha --> """no entiendo la condicion de fila2 == 0, revisar""" [x] - saque el fila2 == 0 porque era inecesario
- en numero coordenada fila / columna , tenia las dos por separado , las uni [x]
- chequear ficha -->"""otra modularizacion que no aporta mucho""" [x] la saque

- main:
"""el planteo no sigue el enunciado donde claramente se pide un menu con opciones siendo estas setear
parametros del juego, iniciar juego y acceder al top 4 del ranking [x] --  ya puse el menu , nunca habia hecho un menu asique lo puse
el hecho de que el flujo del juego este ligado a 4 posiciones en el ranking hace que todo el planteo
este incorrecto, revisa el main y replantea eso deberian desaparece esos whiles anidados con flags raros""" [x] -- ya no se esta ligado a las 4 partidas
"""recalco una vez mas, hay que modularizar a conciencia, pensando en que complejidad agregan o quitan""" [x] 

'''

##  APLICANDO NUEVO MENU
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

def parametros()->None:
    print("\n   ###         DURACION --> TAMAÑO DEL TABLERO:       ###      ")
    print("\n   ###          4/8/12       ###      ")
    print("\n       EXPLICACION DE LAS CARTAS : ")
    print(" - Existen 4 cartas cada una tiene una habilidad y un porcentaje de salida :")
    print(f"\n\t\tLa habilidad y los porcentajes de cada carta son: \n")
    print(f"\tREPLAY -- podes volver a jugar ---> 25% \n\tLAYOUT -- mezcla el tablero que debe adivinar el contrario ---> 12.5%")
    print(f"\tTOTI -- Espeja el tablero que debe adivinar el contrario ---> 20% \n\tFATALITY -- transpone el tablero que debe adivinar el contrario ---> 10%")
    print("\n### VAMOS A JUGAR ###")

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
        duracion = input("\nNivel de juego desea jugar 4/8/12, ponga el numero de duracion: ")
    return int(duracion)

def canti_fichas_acertadas(tablero: list )-> int:
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
    return cant

def continuidad_turno(tablero:list, num_1:int, num_2:int, c_elegida:str = "")->int:
    '''
    PRE: Evalua el tablero , las fichas ingresadas y la carta que se uso en caso de haber elegido una
    POST: devuelve si va a seguir el turno en caso de haber ocurrido alguna opcion
    '''
    if canti_fichas_acertadas(tablero) == int(len(tablero) ** 2):
        return True
    elif num_1 == num_2: 
        print("\nAdivinaste --> seguis jugando\n")
        return  False
    elif c_elegida == "replay": return False
    else: return True

def turno(usuario: str, tablero: list ,tablero_contrario:list, mazo: list)->tuple:
    '''
    PRE: Se ingresa el jugador , el tablero que debe adivinar y su tablero
    POST: Se desarrolla el turno del jugador y se aplican las cartas , en caso de tener alguna .
    '''
    print(f"\n-----------\tTURNO DE {usuario}\t-----------")
    mazo = tirar_dado(mazo)
    termina_turno = False
    while not termina_turno:
        cord_correctas = False
        while not cord_correctas:
            num_1 = coordenada_valida(tablero)
            mostrar_fichas(tablero, num_1[1], num_1[2])

            num_2 = coordenada_valida(tablero)
            mostrar_fichas(tablero, num_1[1], num_1[2], num_2[1], num_2[2])

            cord_correctas = chequear_fil_col(num_1[1],num_1[2],num_2[1],num_2[2])

        tablero = modifico_tablero(tablero, num_1[1],num_1[2],num_2[1],num_2[2],num_1[0],num_2[0])
        termina_turno = continuidad_turno(tablero,num_1[0], num_2[0])
        ## --- si gana el jugador , termina el turno, sino tengo la posibilidad de jugar una carta 
        if termina_turno and canti_fichas_acertadas(tablero) != int(len(tablero) ** 2):
            if mazo:
                print("\nPodes usar una de tus cartas: \n")
                for element in mazo:
                    print(f" - {element}")
                c_elegida = carta_elegida()
                c_elegida.lower
                if c_elegida == "replay":
                    print(f"\nTu carta elegida fue : {c_elegida} -> ###\tVolve a jugar !\t###\n")
                elif c_elegida == "layout":
                    print(f"\nTu carta elegida fue : {c_elegida} -> ###\tAhora se mezclo todo el tablero del contrario\t###\n")
                elif c_elegida == "toti":
                    print(f"\nTu carta elegida fue : {c_elegida} -> ###\tSe espeja el tablero que tiene que adivinar el oponente : \t###\n")
                    toti(tablero_contrario)
                elif c_elegida == "fatality":
                    print(f"\nTu carta elegida fue : {c_elegida} -> ###\tSe transpone el tablero que debe adivinar el oponente: \t###\n")
                    tablero_contrario = fatality(tablero_contrario)

                if c_elegida != "n": mazo.remove(c_elegida)

                termina_turno = continuidad_turno(tablero,num_1[0], num_2[0],c_elegida)

    return tablero, tablero_contrario, mazo

## RANKING :

def mostrar_ranking(ranking:list, n_partidas:int)->None:
    '''
    PRE: Ingresando el ranking y la cantidad de partidas que se jugaron   
    POST: En el caso que la lista del ranking sea 5 elimino el primero asi la lista permanece con los datos de
    las ultimas 4 partidas
    '''
    if len(ranking) == 0:
        print("Todavia no gano nadie , no hay partidas jugadas")
    elif len(ranking) == 5:
        ranking.remove(ranking[0])
        n_partidas -= 3
        for i in range(len(ranking)):
            print(f"partida : {n_partidas} - Gano : {ranking[i][0]} - perdio : {ranking[i][1]}")
            n_partidas += 1
    elif len(ranking) < 5:
        cont = 1
        print(f"\nUltimas 4 partidas: ")
        for i in range(len(ranking)):
            print(f"partida : {cont} - Gano : {ranking[i][0]} - perdio : {ranking[i][1]}")
            cont += 1

## CARTAS :
def tirar_dado(mazo: list)->list:
    '''
    PRE: Se ingresa el mazo del jugador que esta jugando
    POST: Se tiran los dados y si le toca , la carta ingresa en su mazo , sino se retorna el mazo como estaba.
    '''
    print("\nxxxx\tTIRAR EL DADO\txxxx")
    tirar = input("\ningrese una letra y aprete enter para tirar el dado: ")
    while not tirar.isalpha():
        tirar = input("\n ---> Le pedi que ingrese una letra : ")
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
def coordenada_valida(tablero:list)->tuple:
    '''
    PRE: Se ingresan los datos de la fila y la columna  
    POST: En caso de ya haber sido elegido , pide volver a ingresar las coordenadas
    '''
    fila = numero_coordenada("fila", tablero)
    columna = numero_coordenada("columna",tablero)
    ficha = tablero[fila -1][columna - 1][0]
    while ficha == 0:
        print("\nVuelva a ingresar las coordenadas , las que puso ya las uso :")
        fila = numero_coordenada("fila",tablero)
        columna = numero_coordenada("columna",tablero)
        ficha = tablero[fila -1][columna - 1][0]

    return ficha,fila,columna

def mostrar_fichas(tablero: list, fila1:int, columna1: int, fila2:int = 0, columna2: int = 0)->list:
    '''
    PRE: Recibe el tablero que debe adivinar el jugador que esta en turno
    POST: Muestra las fichas elegidas, "Se dan vuelta" las fichas.
    '''
    print("\n")
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if i == (fila1-1) and j == (columna1 - 1):
                print(tablero[i][j][0], end=" ")
            elif i == (fila2-1) and j == (columna2 - 1):
                print(tablero[i][j][0], end=" ")
            else : print(tablero[i][j][1], end=" ")
        print("\n")

def numero_coordenada(tipo: str,m: list)->int:
    '''
    PRE: Le pido la coordenada de la fila al usuario que esta en juego
    POST: Chequea el dato ingresado y solo retorna el valor si es numerico
    '''
    coordenada = input(f"\n -> ingrese la {tipo}: ")
    while not (coordenada.isnumeric() and 0 < int(coordenada) <= len(m)):
        print(f"\nLA COORDENADA SE PONE EN NUMERO y entre 0-{len(m)}")
        coordenada = input(f"->ingrese la {tipo}: ")
    return int(coordenada)

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

def modifico_tablero(tablero:list, fil1:int, col1:int, fil2:int,col2:int, n1:int, n2:int)->list:
    '''
    PRE: Recibe el tablero y las fichas en caso de haber acertado
    POST: Invierte las fichas que se adivinaron a su valor y el segundo valor que se convierte en 0,
    se utiliza para aplicar un contador en caso de que todas las fichas tienen el valor 0, el jugador en turno
    gana.
    '''
    if n1 == n2 :
        tablero[fil1 -1][col1 - 1][0] = 0
        tablero[fil2 -1][col2 - 1][0] = 0
        tablero[fil1 -1][col1 - 1][1] = n1
        tablero[fil2 -1][col2 - 1][1] = n2
        return tablero
    else : return tablero

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

def menu():
    '''
    Muestra el menu
    '''
    print("\na - Comenzar nueva partida \nb - duracion, probabilidad de cada carta\nc - score de las ultimas 4 partidas\nd - Finalizar juego ")

def main()->None:

    n_partidas = 0
    ranking = list()

    menu()
    desicion = input("\n---> Opcion : ")

    while desicion == "a" or desicion == "b" or desicion == "c":

        if desicion == "a":
            usuario_A = nombre_jugadores()
            print("\n###\tOponente\t###")
            usuario_B = nombre_jugadores()
            duracion = duracion_juego()
            tableroA = generar_matriz(duracion)
            tableroB = generar_matriz(duracion)
            cartas_J_A = []
            cartas_J_B = []
            # ranking = chequear_usuarios(usuario_A, ranking)
            # ranking = chequear_usuarios(usuario_B, ranking)

            ## --> MUESTRO A CADA JUGADOR EL TABLERO QUE DEBE ADIVINAR:
            print(f"\nEl tablero de {usuario_A} que tiene que adivinar es : \n")
            print_tablero(tableroB, duracion, "visible")

            print(f"El tablero de {usuario_B} que tiene que adivinar es : \n")
            print_tablero(tableroA, duracion, "visible")

            juego = True
            while juego:
                jugadorA = turno(usuario_A, tableroB, tableroA,cartas_J_A)
                if canti_fichas_acertadas(jugadorA[0]) == int(len(tableroB) ** 2):
                    print(f"###         Ganador : {usuario_A}       ###\n")
                    ganador = usuario_A
                    perdedor = usuario_B
                    ranking.append((ganador, perdedor))
                    juego = False
                else:
                    jugadorB = turno(usuario_B,tableroA, tableroB, cartas_J_B)
                    if canti_fichas_acertadas(jugadorB[0]) == int(len(tableroA) ** 2):
                        print(f"###         Ganador : {usuario_B}       ###\n")
                        ganador = usuario_B
                        perdedor = usuario_A
                        ranking.append((ganador, perdedor))
                        juego = False
                    else: juego = True

            n_partidas += 1

        elif desicion == "b":
            parametros()

        else:
            mostrar_ranking(ranking, n_partidas)

        menu()
        desicion = input("---> Opcion : ")  

main()

