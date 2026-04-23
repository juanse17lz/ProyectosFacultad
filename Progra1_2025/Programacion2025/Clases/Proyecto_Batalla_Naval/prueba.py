import pygame
from Configuraciones.Funciones_Naval import *
import pygame

def manejar_disparo(event, matriz_juego, matriz_cobertura, ancho_pantalla, alto_pantalla, lista_barcos, puntaje):
    """
    Maneja el disparo cuando se hace clic en el tablero.
    
    Args:
        event: evento de pygame (debe ser MOUSEBUTTONDOWN)
        matriz_juego: matriz con las posiciones de los barcos (1 = barco, 0 = agua)
        matriz_cobertura: matriz que muestra los disparos realizados (0 = no disparado, 1 = impacto, 9 = agua)
        ancho_pantalla: ancho de la pantalla
        alto_pantalla: alto de la pantalla
        lista_barcos: lista con información de todos los barcos
        puntaje: puntaje actual del jugador
    
    Returns:
        tuple: (impacto, fila, columna, nuevo_puntaje, barco_hundido) 
    """
    retorno = (None, None, None, puntaje, None)
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Click izquierdo
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
                        nuevo_puntaje = puntaje + 5  # +5 puntos por impacto
                        
                        # Verificar si se hundió un barco
                        barco_hundido = verificar_barco_hundido(fila, columna, lista_barcos, matriz_cobertura)
                        if barco_hundido:
                            # Obtener tamaño del barco hundido
                            tamaño_barco = barco_hundido[0]  # El primer elemento es el largo
                            puntos_extra = tamaño_barco * 10  # 10 puntos por cada elemento
                            nuevo_puntaje += puntos_extra
                            retorno = (True, fila, columna, nuevo_puntaje, barco_hundido)
                        else:
                            retorno = (True, fila, columna, nuevo_puntaje, None)
                    else:  # No hay barco (agua)
                        matriz_cobertura[fila][columna] = 9  # Falló
                        nuevo_puntaje = puntaje - 1  # -1 punto por fallo
                        retorno = (False, fila, columna, nuevo_puntaje, None)
    
    return retorno  # No se realizó disparo válido

def verificar_barco_hundido(fila_impacto, columna_impacto, lista_barcos, matriz_cobertura):
    """
    Verifica si un barco ha sido completamente hundido después de un impacto.
    
    Args:
        fila_impacto: fila donde se produjo el impacto
        columna_impacto: columna donde se produjo el impacto
        lista_barcos: lista con información de todos los barcos [largo, (fila_inicio, columna_inicio), horizontal]
        matriz_cobertura: matriz que muestra los disparos realizados
    
    Returns:
        list o None: información del barco hundido o None si no se hundió ningún barco
    """
    retorno = None
    for barco in lista_barcos:
        largo = barco[0]
        fila_inicio, columna_inicio = barco[1]
        horizontal = barco[2]  # True si es horizontal, False si es vertical
        
        # Verificar si el impacto pertenece a este barco
        impacto_en_barco = False
        
        if horizontal:
            # Barco horizontal
            if (fila_impacto == fila_inicio and 
                columna_inicio <= columna_impacto < columna_inicio + largo):
                impacto_en_barco = True
        else:
            # Barco vertical
            if (columna_impacto == columna_inicio and 
                fila_inicio <= fila_impacto < fila_inicio + largo):
                impacto_en_barco = True
        
        if impacto_en_barco:
            # Verificar si todo el barco está hundido
            barco_hundido = True
            
            for i in range(largo):
                if horizontal:
                    if matriz_cobertura[fila_inicio][columna_inicio + i] != 1:
                        barco_hundido = False
                        break
                else:
                    if matriz_cobertura[fila_inicio + i][columna_inicio] != 1:
                        barco_hundido = False
                        break
            
            if barco_hundido:
                retorno = barco
    
    return retorno

def mostrar_puntaje(screen, puntaje, ancho_pantalla):
    """
    Muestra el puntaje en pantalla.
    
    Args:
        screen: superficie de pygame para dibujar
        puntaje: puntaje actual del jugador
        ancho_pantalla: ancho de la pantalla
    """
    font = pygame.font.Font(None, 48)
    texto_puntaje = f"Puntaje: {puntaje:04d}"
    color_puntaje = (255, 255, 255) if puntaje >= 0 else (255, 100, 100)  # Rojo si es negativo
    
    texto = font.render(texto_puntaje, True, color_puntaje)
    texto_rect = texto.get_rect(center=(ancho_pantalla // 2, 25))
    screen.blit(texto, texto_rect)

def procesar_turno_jugador(screen, matriz_juego, matriz_cobertura, ancho_pantalla, alto_pantalla, clock, lista_barcos, puntaje):
    """
    Procesa el turno del jugador, mostrando el tablero y esperando un disparo.
    
    Args:
        screen: superficie de pygame para dibujar
        matriz_juego: matriz con las posiciones de los barcos
        matriz_cobertura: matriz que muestra los disparos realizados
        ancho_pantalla: ancho de la pantalla
        alto_pantalla: alto de la pantalla
        clock: reloj de pygame
        lista_barcos: lista con información de todos los barcos
        puntaje: puntaje actual del jugador
    
    Returns:
        tuple: (impacto, fila, columna, nuevo_puntaje, barco_hundido) del disparo realizado
    """
    turno_activo = True
    
    while turno_activo:
        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return (None, None, None)
            
            # Procesar disparo
            resultado = manejar_disparo(event, matriz_juego, matriz_cobertura, ancho_pantalla, alto_pantalla, lista_barcos, puntaje)
            
            if resultado[0] is not None:  # Se realizó un disparo válido
                impacto, fila, columna, nuevo_puntaje, barco_hundido = resultado
                
                # Mostrar mensaje de resultado
                if impacto:
                    puntos_ganados = nuevo_puntaje - puntaje
                    if barco_hundido:
                        tamaño_barco = barco_hundido[0]
                        print(f"¡BARCO HUNDIDO! en posición ({fila}, {columna})")
                        print(f"¡Has hundido un barco de {tamaño_barco} elementos!")
                        print(f"Puntos ganados: +{puntos_ganados} (5 por impacto + {puntos_ganados-5} por hundir barco)")
                    else:
                        print(f"¡IMPACTO! en posición ({fila}, {columna}) - Puntos ganados: +5")
                else:
                    print(f"Agua en posición ({fila}, {columna}) - Puntos perdidos: -1")
                
                return resultado
        
        # Dibujar el tablero
        screen.fill((50, 50, 50))  # Fondo gris
        
        # Mostrar puntaje
        mostrar_puntaje(screen, puntaje, ancho_pantalla)
        
        # Mostrar tablero
        mostrar_tablero(screen, matriz_cobertura, ancho_pantalla, alto_pantalla)
        
        # Agregar texto de instrucciones
        font = pygame.font.Font(None, 36)
        texto = font.render("Haz clic en un casillero para disparar", True, (255, 255, 255))
        texto_rect = texto.get_rect(center=(ancho_pantalla // 2, 80))
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
    for fila in range(len(matriz_juego)):
        for columna in range(len(matriz_juego[0])):
            # Si hay un barco que no ha sido impactado
            if matriz_juego[fila][columna] == 1 and matriz_cobertura[fila][columna] != 1:
                return False
    return True

# Ejemplo de uso en el bucle principal del juego
def ejemplo_bucle_juego():
    """
    Ejemplo de cómo integrar las funciones en el bucle principal del juego.
    """
    pygame.init()
    ancho_pantalla = 800
    alto_pantalla = 600
    screen = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
    pygame.display.set_caption("Batalla Naval")
    clock = pygame.time.Clock()
    
    # Crear tablero de juego
    tablero_info = tablero_juego("D")  # Dificultad Fácil
    matriz_juego = tablero_info[0]
    lista_barcos = tablero_info[1]
    
    # Crear matriz de cobertura (lo que ve el jugador)
    filas = len(matriz_juego)
    columnas = len(matriz_juego[0])
    matriz_cobertura = [[0 for _ in range(columnas)] for _ in range(filas)]
    
    # Inicializar puntaje
    puntaje = 0
    print(f"=== BATALLA NAVAL ===")
    print(f"Puntaje inicial: {puntaje:04d}")
    print("Reglas de puntuación:")
    print("• Impacto: +5 puntos")
    print("• Fallo: -1 punto")
    print("• Barco hundido: +10 puntos por cada elemento del barco")
    print("=" * 40)
    
    juego_activo = True
    
    while juego_activo:
        # Procesar turno del jugador
        resultado = procesar_turno_jugador(screen, matriz_juego, matriz_cobertura, 
                                         ancho_pantalla, alto_pantalla, clock, lista_barcos, puntaje)
        
        if resultado[0] is None:  # El jugador cerró el juego
            juego_activo = False
        else:
            # Actualizar puntaje
            puntaje = resultado[3]
            print(f"Puntaje actual: {puntaje:04d}")
            print("-" * 30)
            
            # Verificar si ganó
            if verificar_victoria(matriz_juego, matriz_cobertura):
                print("=" * 40)
                print("¡FELICITACIONES! ¡Has hundido todos los barcos!")
                print(f"PUNTAJE FINAL: {puntaje:04d}")
                print("=" * 40)
                
                # Mostrar mensaje de victoria en pantalla por unos segundos
                screen.fill((0, 100, 0))  # Fondo verde de victoria
                font_grande = pygame.font.Font(None, 72)
                font_pequeña = pygame.font.Font(None, 48)
                
                texto_victoria = font_grande.render("¡VICTORIA!", True, (255, 255, 255))
                texto_puntaje_final = font_pequeña.render(f"Puntaje Final: {puntaje:04d}", True, (255, 255, 255))
                
                rect_victoria = texto_victoria.get_rect(center=(ancho_pantalla // 2, alto_pantalla // 2 - 50))
                rect_puntaje = texto_puntaje_final.get_rect(center=(ancho_pantalla // 2, alto_pantalla // 2 + 50))
                
                screen.blit(texto_victoria, rect_victoria)
                screen.blit(texto_puntaje_final, rect_puntaje)
                pygame.display.flip()
                
                pygame.time.wait(3000)  # Esperar 3 segundos
                juego_activo = False
    
    pygame.quit()

if __name__ == "__main__":
    ejemplo_bucle_juego()