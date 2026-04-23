import pygame
import json
import os
from datetime import datetime
import pygame
from Configuraciones.Funciones_Naval import *

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
                            return (True, fila, columna, nuevo_puntaje, barco_hundido)
                        else:
                            return (True, fila, columna, nuevo_puntaje, None)
                    else:  # No hay barco (agua)
                        matriz_cobertura[fila][columna] = 9  # Falló
                        nuevo_puntaje = puntaje - 1  # -1 punto por fallo
                        return (False, fila, columna, nuevo_puntaje, None)
    
    return (None, None, None, puntaje, None)  # No se realizó disparo válido

def cargar_puntajes(archivo="puntajes.json"):
    """
    Carga los puntajes desde un archivo JSON.
    
    Args:
        archivo: nombre del archivo JSON
    
    Returns:
        list: lista de diccionarios con los puntajes
    """
    try:
        if os.path.exists(archivo):
            with open(archivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            return []
    except Exception as e:
        print(f"Error al cargar puntajes: {e}")
        return []

def guardar_puntaje(nombre, puntaje, archivo="puntajes.json"):
    """
    Guarda un nuevo puntaje en el archivo JSON.
    
    Args:
        nombre: nombre del jugador
        puntaje: puntaje obtenido
        archivo: nombre del archivo JSON
    """
    try:
        # Cargar puntajes existentes
        puntajes = cargar_puntajes(archivo)
        
        # Crear nuevo registro
        nuevo_puntaje = {
            "nombre": nombre,
            "puntaje": puntaje,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Agregar nuevo puntaje
        puntajes.append(nuevo_puntaje)
        
        # Ordenar por puntaje (de mayor a menor)
        puntajes.sort(key=lambda x: x["puntaje"], reverse=True)
        
        # Guardar en archivo
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(puntajes, f, indent=2, ensure_ascii=False)
        
        print(f"Puntaje guardado exitosamente para {nombre}: {puntaje}")
        
    except Exception as e:
        print(f"Error al guardar puntaje: {e}")

def mostrar_mejores_puntajes(puntajes, cantidad=5):
    """
    Muestra los mejores puntajes en consola.
    
    Args:
        puntajes: lista de diccionarios con los puntajes
        cantidad: cantidad de puntajes a mostrar
    """
    print("\n" + "=" * 50)
    print("🏆 MEJORES PUNTAJES 🏆")
    print("=" * 50)
    
    if not puntajes:
        print("No hay puntajes registrados aún.")
    else:
        for i, puntaje in enumerate(puntajes[:cantidad], 1):
            fecha = puntaje["fecha"].split(" ")[0]  # Solo la fecha, sin hora
            print(f"{i:2d}. {puntaje['nombre']:15s} - {puntaje['puntaje']:5d} pts ({fecha})")
    
    print("=" * 50)

def solicitar_nombre_jugador(screen, ancho_pantalla, alto_pantalla, clock):
    """
    Solicita el nombre del jugador mediante una interfaz gráfica.
    
    Args:
        screen: superficie de pygame
        ancho_pantalla: ancho de la pantalla
        alto_pantalla: alto de la pantalla
        clock: reloj de pygame
    
    Returns:
        str: nombre ingresado por el jugador
    """
    font_titulo = pygame.font.Font(None, 48)
    font_texto = pygame.font.Font(None, 36)
    nombre = ""
    activo = True
    
    while activo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Jugador Anónimo"
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if nombre.strip():  # Si hay texto ingresado
                        return nombre.strip()
                elif event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                elif event.key == pygame.K_ESCAPE:
                    return "Jugador Anónimo"
                else:
                    # Agregar caracteres válidos
                    if len(nombre) < 20:  # Límite de caracteres
                        if event.unicode.isprintable():
                            nombre += event.unicode
        
        # Dibujar interfaz
        screen.fill((30, 30, 60))  # Fondo azul oscuro
        
        # Título
        titulo = font_titulo.render("¡Ingresa tu nombre!", True, (255, 255, 255))
        titulo_rect = titulo.get_rect(center=(ancho_pantalla // 2, alto_pantalla // 2 - 100))
        screen.blit(titulo, titulo_rect)
        
        # Campo de texto
        texto_fondo = pygame.Rect(ancho_pantalla // 2 - 150, alto_pantalla // 2 - 20, 300, 40)
        pygame.draw.rect(screen, (255, 255, 255), texto_fondo)
        pygame.draw.rect(screen, (0, 0, 0), texto_fondo, 2)
        
        # Texto ingresado
        texto_nombre = font_texto.render(nombre, True, (0, 0, 0))
        screen.blit(texto_nombre, (texto_fondo.x + 5, texto_fondo.y + 5))
        
        # Cursor parpadeante
        if pygame.time.get_ticks() % 1000 < 500:
            cursor_x = texto_fondo.x + 5 + texto_nombre.get_width()
            pygame.draw.line(screen, (0, 0, 0), 
                           (cursor_x, texto_fondo.y + 5), 
                           (cursor_x, texto_fondo.y + 35), 2)
        
        # Instrucciones
        instrucciones = [
            "Presiona ENTER para confirmar",
            "ESC para usar 'Jugador Anónimo'",
            f"Máximo 20 caracteres ({len(nombre)}/20)"
        ]
        
        for i, instruccion in enumerate(instrucciones):
            texto_inst = font_texto.render(instruccion, True, (200, 200, 200))
            texto_rect = texto_inst.get_rect(center=(ancho_pantalla // 2, alto_pantalla // 2 + 60 + i * 30))
            screen.blit(texto_inst, texto_rect)
        
        pygame.display.flip()
        clock.tick(60)
    
    return nombre if nombre.strip() else "Jugador Anónimo"
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
                return barco
    
    return None

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

def mostrar_tabla_puntajes_pantalla(screen, puntajes, ancho_pantalla, alto_pantalla, clock):
    """
    Muestra la tabla de mejores puntajes en pantalla.
    
    Args:
        screen: superficie de pygame
        puntajes: lista de puntajes
        ancho_pantalla: ancho de la pantalla
        alto_pantalla: alto de la pantalla
        clock: reloj de pygame
    """
    esperando = True
    
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                esperando = False
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                esperando = False
        
        # Fondo
        screen.fill((20, 30, 50))
        
        # Título
        font_titulo = pygame.font.Font(None, 64)
        titulo = font_titulo.render("🏆 MEJORES PUNTAJES 🏆", True, (255, 215, 0))
        titulo_rect = titulo.get_rect(center=(ancho_pantalla // 2, 50))
        screen.blit(titulo, titulo_rect)
        
        # Tabla de puntajes
        font_puntajes = pygame.font.Font(None, 36)
        y_inicio = 120
        
        if not puntajes:
            texto_vacio = font_puntajes.render("No hay puntajes registrados", True, (255, 255, 255))
            texto_rect = texto_vacio.get_rect(center=(ancho_pantalla // 2, y_inicio + 50))
            screen.blit(texto_vacio, texto_rect)
        else:
            # Encabezados
            encabezados = font_puntajes.render("Pos  Nombre           Puntaje    Fecha", True, (200, 200, 200))
            screen.blit(encabezados, (50, y_inicio))
            
            # Línea separadora
            pygame.draw.line(screen, (100, 100, 100), (50, y_inicio + 35), (ancho_pantalla - 50, y_inicio + 35), 2)
            
            # Puntajes (mostrar top 10)
            for i, puntaje in enumerate(puntajes[:10]):
                y_pos = y_inicio + 50 + i * 40
                
                # Color dorado para el primer lugar, plateado para segundo, bronce para tercero
                if i == 0:
                    color = (255, 215, 0)  # Dorado
                elif i == 1:
                    color = (192, 192, 192)  # Plateado
                elif i == 2:
                    color = (205, 127, 50)  # Bronce
                else:
                    color = (255, 255, 255)  # Blanco
                
                # Formatear texto
                pos = f"{i+1:2d}."
                nombre = f"{puntaje['nombre'][:15]:15s}"  # Truncar nombre si es muy largo
                puntos = f"{puntaje['puntaje']:5d}"
                fecha = puntaje['fecha'].split(' ')[0]  # Solo la fecha
                
                linea_texto = f"{pos} {nombre} {puntos:>8s}    {fecha}"
                texto_puntaje = font_puntajes.render(linea_texto, True, color)
                screen.blit(texto_puntaje, (50, y_pos))
        
        # Instrucciones
        font_inst = pygame.font.Font(None, 32)
        instruccion = font_inst.render("Presiona cualquier tecla o haz clic para continuar", True, (150, 150, 150))
        inst_rect = instruccion.get_rect(center=(ancho_pantalla // 2, alto_pantalla - 50))
        screen.blit(instruccion, inst_rect)
        
        pygame.display.flip()
        clock.tick(60)

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
    tablero_info = tablero_juego("F")  # Dificultad Fácil
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
    
    # Mostrar puntajes existentes al inicio
    puntajes_existentes = cargar_puntajes()
    if puntajes_existentes:
        print("\n🏆 MEJORES PUNTAJES ACTUALES:")
        for i, p in enumerate(puntajes_existentes[:3], 1):
            print(f"{i}. {p['nombre']} - {p['puntaje']} pts")
    
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
                
                # Solicitar nombre del jugador
                nombre_jugador = solicitar_nombre_jugador(screen, ancho_pantalla, alto_pantalla, clock)
                
                # Guardar puntaje
                guardar_puntaje(nombre_jugador, puntaje)
                
                # Cargar y mostrar mejores puntajes
                puntajes = cargar_puntajes()
                mostrar_mejores_puntajes(puntajes)
                
                # Mostrar tabla de puntajes en pantalla
                mostrar_tabla_puntajes_pantalla(screen, puntajes, ancho_pantalla, alto_pantalla, clock)
                
                juego_activo = False
    
    pygame.quit()

if __name__ == "__main__":
    ejemplo_bucle_juego()