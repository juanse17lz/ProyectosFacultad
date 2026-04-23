import pygame as pg
import pygame.mixer as mixer
mixer.init()
pg.init()

#COLORES
color_verde = (22,244,8)
color_azul = (8,105,244)
color_blanco = (255,255,255)
color_negro = (0,0,0)

#POSICIONES
eje_x = 30
eje_y = 30
cordenadas=(eje_x,eje_y,60,60)
cordenadas2 = (100,100,100,100) 

#PERSONAJES
spiderman = {}
spiderman["surface"] = pg.image.load("C:/Users/juans/programacion_full/Programacion2025/Clases/Clase_14_Pygame/Elementos_Pygame/spiderman_run.png")
spiderman["surface"] = pg.transform.scale(spiderman["surface"],(100,100))
spiderman["rect_pos"] = pg.Rect(eje_x,eje_y,200,200)
spiderman["rect"] = pg.Rect((eje_x+100/2)-10, eje_y+90,40,20)
spiderman["score"] = 0


#TAMAÑOS
ALTO_VENTANA = 600
ANCHO_VENTANA = 800
pantalla = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

"""
mixer.music.load("./assets/sound/02. Crazy Dave (Intro Theme).mp3")
mixer.music.set_volume(0.5)
mixer.music.play(-1)
"""
#INICIACION
while True:
    #EVENTOS
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        mouse_pos = pg.mouse.get_pos()
        cordenadas=(mouse_pos[0],mouse_pos[1],60,60)

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                eje_x -= 10
            elif event.key == pg.K_RIGHT:
                eje_x += 10
            elif event.key == pg.K_DOWN:
                eje_y += 10
            elif event.key == pg.K_UP:
                eje_y -= 10
        
    #DISPLAY
    pantalla.fill(color_blanco)
    rectangulo = pg.draw.rect(pantalla,color_verde,cordenadas)
    rectangulo2 = pg.draw.rect(pantalla,color_azul,cordenadas2)
    if rectangulo.collidepoint(rectangulo2.x,rectangulo2.y):
        print("Colisionando")
    pantalla.blit(spiderman["surface"],spiderman["rect_pos"])

    pg.display.flip()