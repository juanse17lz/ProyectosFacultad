import random
from pygame import *
import pygame
import json

def printear_lista_continua(lista:list):
    """Recibe una lista y muestra sus elementos por pantalla.

    Args:
        lista (list): Lista cualquiera.
    """
    for i in range(len(lista)):
        if type(lista[i]) == list:
            printear_lista_continua(lista[i])
        elif i == len(lista):
            print(lista[i])
        else:
            print(lista[i],end=" ")


def printear_matriz(matriz:list):
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            print(matriz[f][c], end= " ")
        print("")

def bool_aleatorio()->bool:
    numero = random.randint(0,1)
    if numero == 0:
        retorno = False
    else:
        retorno = True
    return retorno

def inicializar_matriz(filas:int,columnas:int,valor_inicial=0)->list:
    """Inicializa una matriz con la cantidad de filas y columas ingresadas. Por defecto los elmentos seran ceros pero se le puede pasar por parametro el valor de los elementos iniciales. 

    Args:
        filas (int): Cantidad de filas que tendra la matriz.
        columnas (int): Cantida de columnas que tendra la matriz.
        valor_inicial : Valor inicial que tendran los elementos de la matriz, por defecto en cero.

    Returns:
        list: Retorna la matriz inicializada.
    """
    matriz = []
    for i in range(filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]
    return matriz

def colocar_barco(matriz:list,barco:list)->list:
    pos = bool_aleatorio()
    posicion_valida = False
    while posicion_valida == False:
        fila = random.randint(0,len(matriz)-1)
        columna = random.randint(0,len(matriz[0])-1)
        for i in range(len(barco)):
            if pos:
                if columna + i >= len(matriz[0]) or matriz[fila][columna + i] == 1:
                    break
                elif matriz[fila][columna + i] == 0 and i == len(barco)-1:
                    posicion_valida = True
            else:
                if fila + i >= len(matriz) or matriz[fila + i][columna] == 1:
                    break
                elif matriz[fila + i][columna] == 0 and i == len(barco)-1:
                    posicion_valida = True
    if posicion_valida:
        for i in range(len(barco)):
            if pos:
                matriz[fila][columna + i] = 1
            else:
                matriz[fila + i][columna] = 1
    coordenada = (fila,columna)
    poscicion = pos
    largo = len(barco)
    #cuadrado = pygame.Rect((27*columna)+27,(27*fila)+100,25,25)            
    datos_barco = [largo,coordenada,poscicion]
    return datos_barco

def colocacion_barcos(matriz:list,barco:list):
    lista_datos = []
    if len(barco) == 1:
        for c in range(4):
            datos = colocar_barco(matriz,barco)
            lista_datos.append(datos)
    elif len(barco) == 2:
        for c in range(3):
            datos = colocar_barco(matriz,barco)
            lista_datos.append(datos)
    elif len(barco) == 3:
        for c in range(2):
            datos = colocar_barco(matriz,barco)
            lista_datos.append(datos)
    elif len(barco) == 4:
        datos = colocar_barco(matriz,barco)
        lista_datos.append(datos)
    return lista_datos

def limpiar_datos(lista_barcos:list)->list:
    lista_limpia = []
    for i in range(len(lista_barcos)):
        tipos_barcos = lista_barcos[i]
        for f in range(len(tipos_barcos)):
            lista_limpia.append(tipos_barcos[f])
            
    return lista_limpia


def tablero_juego(dificultad:str="F")->list:
    filas = 10
    columnas = 10
    repeticiones = 1
    if dificultad == "M":
        filas *= 2
        columnas *= 2
        repeticiones *= 2
    elif dificultad == "D":
        filas *= 4
        columnas *= 4
        repeticiones *= 3

    submarino = [1]
    destructore = [1,1]
    crucero = [1,1,1]
    acorazado =[1,1,1,1]
    barcos = [submarino,destructore,crucero,acorazado]

    tablero = inicializar_matriz(filas,columnas)
    informacion_tablero = False
    for r in range(repeticiones):
        for barco in barcos:
            if informacion_tablero == False:
                info_barcos = [colocacion_barcos(tablero,barco)]
                informacion_tablero = True
            else:
                datos = colocacion_barcos(tablero,barco)
                info_barcos.append(datos)

    lista_limpia = limpiar_datos(info_barcos)

    tablero_info = [tablero,lista_limpia]
    return tablero_info
        
def generar_casilleros(matriz:list)->list:
    lista_casilleros = []
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            cuadrado = pygame.Rect((27 * (1+c))+27,(27 * (1+f))+100,25,25) 
            casillero = ((cuadrado),True)
            lista_casilleros.append(casillero)
    return lista_casilleros

def colocar_casilla(key,screen):
    pygame.draw.rect(screen,"white",key)

#Funciones Pygame
def centrar_eje_x(superfice, objeto_a_centrar)->int:
    """Se encarga de centrar un objeto en su eje X.

    Args:
        superfice : Superficie donde se va a centrar.
        objeto_a_centrar : Objeto que se va a centrar.
    Returns:
        int: centro del eje X.
    """
    centro = superfice.x +(superfice.width - objeto_a_centrar.get_width())/2
    return centro

def centrar_eje_y(superfice, objeto_a_centrar)->int:
    """Se encarga de centrar un objeto en su eje Y.

    Args:
        superfice : Superficie donde se va a centrar.
        objeto_a_centrar : Objeto que se va a centrar.
    Returns:
        int: centro del eje Y.
    """
    centro = superfice.y +(superfice.height - objeto_a_centrar.get_height())/2
    return centro

def poner_boton(screen, boton, palabra:str, color_apretado, color_no_apretado, fuente):
    """Se encarga de poner un boton en la pantalla.

    Args:
        screen : pantalla donde se colocara el boton.
        boton : boton a colocar.(El boton ya debe estar creado con su posicion y tamaño.)
        palabra (str): texto del boton.
        color_apretado : color del boton.
        color_no_apretado : color del boton al posicionarse encima.
        fuente : fuente del texto.
    """
    if boton.collidepoint(mouse.get_pos()):
        draw.rect(screen,(color_apretado), boton, 0)
    else:
        draw.rect(screen,(color_no_apretado), boton, 0)
    texto = fuente.render(palabra, True, ("white"))
    screen.blit(texto,(centrar_eje_x(boton,texto),centrar_eje_y(boton,texto)))

def cargar_imagen(ruta:str,medidas:tuple):
    imagen = pygame.image.load(ruta)
    imagen_transformada = pygame.transform.scale(imagen,medidas)
    return imagen_transformada


def escribir_palabara(screen,text, pos=(0,0), size=16, color=(0,0,0)):
    font = pygame.font.SysFont("Consolas", size)
    screen.blit(font.render(text, True, color), pos)

#punto C, muestra tablero
def dibujar_tablero(screen, matriz, x_inicial, y_inicial, tamaño_casillero):
    """
    Dibuja en pantalla la matriz del tablero.

        matriz: la matriz a mostrar (tablero de cobertura).
        x_inicial: posición X donde empieza el tablero.
        y_inicial: posición Y donde empieza el tablero.
        tamaño_casillero: tamaño (ancho y alto) de cada cuadrado.
    """
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            x = x_inicial + columna * tamaño_casillero
            y = y_inicial + fila * tamaño_casillero
            valor = matriz[fila][columna]

            if valor == 0:
                color = (0, 102, 204)  # Azul seria agua
            elif valor == 1:
                color = (0, 204, 102)  # Verde seria la pego
            elif valor == 9:
                color = (255, 0, 0)    # Rojo seria falló

            draw.rect(screen, color, (x, y, tamaño_casillero, tamaño_casillero))
            draw.rect(screen, (0, 0, 0), (x, y, tamaño_casillero, tamaño_casillero), 1)  # borde

#ounto c centra lo que da dibujar_tablero asi queda lindo 
def mostrar_tablero(screen, matriz, ancho_pantalla, alto_pantalla):
    tamaño_casillero = 20
    filas = len(matriz)
    columnas = len(matriz[0])
    ancho_total = columnas * tamaño_casillero
    alto_total = filas * tamaño_casillero
    x_inicial = (ancho_pantalla - ancho_total) // 2
    y_inicial = (alto_pantalla - alto_total) // 2

    dibujar_tablero(screen, matriz, x_inicial, y_inicial, tamaño_casillero)


#punto d, muestra puntaje

def mostrar_puntaje(screen, puntaje, ancho, alto):
    fuente = pygame.font.SysFont("Arial", 24)
    texto = fuente.render(f"Puntaje: {puntaje:04}", True, (255, 255, 255))
    screen.blit(texto, (50, alto - 30))


def escribir_json(lista_diccionarios:list,archivo:str):
    for i in range(len(lista_diccionarios)):
        with open(archivo, 'a') as archivo_json:
            json.dump(lista_diccionarios[i], archivo_json, indent=4)


def manejar_disparo(event, matriz_juego, matriz_cobertura, ancho_pantalla, alto_pantalla):
    """
    Maneja el disparo cuando se hace clic en el tablero.
    
    Args:
        event: evento de pygame (debe ser MOUSEBUTTONDOWN)
        matriz_juego: matriz con las posiciones de los barcos (1 = barco, 0 = agua)
        matriz_cobertura: matriz que muestra los disparos realizados (0 = no disparado, 1 = impacto, 9 = agua)
        ancho_pantalla: ancho de la pantalla
        alto_pantalla: alto de la pantalla
    
    Returns:
        tuple: (impacto, fila, columna) donde impacto es True si le dio a un barco
    """
    retorno = (None,None,None)
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Click izquierdo
        retorno = (None,None,None)
        # Obtener la posición del mouse
        mouse_x, mouse_y = event.pos
        
        # Calcular las mismas coordenadas que usa mostrar_tablero
        tamaño_casillero = 20
        filas = len(matriz_juego)
        columnas = len(matriz_juego[0])
        ancho_total = columnas * tamaño_casillero
        alto_total = filas * tamaño_casillero
        x_inicial = (ancho_pantalla - ancho_total) // 2
        y_inicial = (alto_pantalla - alto_total) // 2
        
        # Verificar si el clic está dentro del tablero
        if (x_inicial <= mouse_x <= x_inicial + ancho_total and 
            y_inicial <= mouse_y <= y_inicial + alto_total):
            
            # Calcular fila y columna del casillero clickeado
            columna = (mouse_x - x_inicial) // tamaño_casillero
            fila = (mouse_y - y_inicial) // tamaño_casillero
            
            # Verificar que esté dentro de los límites de la matriz
            if 0 <= fila < filas and 0 <= columna < columnas:
                # Verificar si ya se disparó en esta posición
                if matriz_cobertura[fila][columna] == 0:  # No disparado anteriormente
                    # Efectuar el disparo
                    if matriz_juego[fila][columna] == 1:  # Hay un barco
                        matriz_cobertura[fila][columna] = 1  # Impacto
                        retorno = (True, fila, columna)
                    else:  # No hay barco (agua)
                        matriz_cobertura[fila][columna] = 9  # Falló
                        retorno = (False, fila, columna)
    
    return retorno  # No se realizó disparo válido

def procesar_turno_jugador(screen, matriz_juego, matriz_cobertura, ancho_pantalla, alto_pantalla, clock):
    """
    Procesa el turno del jugador, mostrando el tablero y esperando un disparo.
    
    Args:
        screen: superficie de pygame para dibujar
        matriz_juego: matriz con las posiciones de los barcos
        matriz_cobertura: matriz que muestra los disparos realizados
        ancho_pantalla: ancho de la pantalla
        alto_pantalla: alto de la pantalla
        clock: reloj de pygame
    
    Returns:
        tuple: (impacto, fila, columna) del disparo realizado
    """
    turno_activo = True
    
    while turno_activo:
        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return (None, None, None)
            
            # Procesar disparo
            resultado = manejar_disparo(event, matriz_juego, matriz_cobertura, ancho_pantalla, alto_pantalla)
            
            if resultado[0] is not None:  # Se realizó un disparo válido
                impacto, fila, columna = resultado
                
                # Mostrar mensaje de resultado
                if impacto:
                    print(f"¡IMPACTO! en posición ({fila}, {columna})")
                else:
                    print(f"Agua en posición ({fila}, {columna})")
                
                return resultado
        
        # Dibujar el tablero
        screen.fill((50, 50, 50))  # Fondo gris
        mostrar_tablero(screen, matriz_cobertura, ancho_pantalla, alto_pantalla)
        
        # Agregar texto de instrucciones
        font = pygame.font.Font(None, 36)
        texto = font.render("Haz clic en un casillero para disparar", True, (255, 255, 255))
        texto_rect = texto.get_rect(center=(ancho_pantalla // 2, 50))
        screen.blit(texto, texto_rect)
        
        pygame.display.flip()
        clock.tick(60)

def verificar_victoria(matriz_juego, matriz_cobertura):
    """
    Verifica si el jugador ha ganado (todos los barcos hundidos).
    
    Args:
        matriz_juego: matriz con las posiciones de los barcos
        matriz_cobertura: matriz que muestra los disparos realizados
    
    Returns:
        bool: True si se hundieron todos los barcos
    """
    retorno = True
    for fila in range(len(matriz_juego)):
        for columna in range(len(matriz_juego[0])):
            # Si hay un barco que no ha sido impactado
            if matriz_juego[fila][columna] == 1 and matriz_cobertura[fila][columna] != 1:
                retorno = False
    return retorno

def calcular_puntaje(matriz_covertura:list,matriz_real:list):
    pass
