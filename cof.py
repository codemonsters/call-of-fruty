#!/usr/bin/env python3

#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from pygame.locals import *

#====================================
#    ---------CONSTANTES---------
#====================================
ANCHO_SCREEN = 1280
ALTO_SCREEN = 720
FPS = 60
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS_LIGERO = (200, 200, 200)

#====================================
#     --------FUNCIONES--------
#====================================

#====================================
#     ----------CUERPO----------
#====================================
#------------------Inicializar
pygame.init()
DISPLAYSURF = pygame.display.set_mode((ANCHO_SCREEN, ALTO_SCREEN))
pygame.display.set_caption('Call Of Fruty')
fps_clock = pygame.time.Clock()
pygame.key.set_repeat(1, 100)

#------------------Fondo menu
logo_cof = pygame.image.load("imagenes/call of fruty.png")

#------------------Font
font_pequeña = pygame.font.Font("Astounding news.ttf", 80)
font_grande = pygame.font.Font("Astounding news.ttf", 110)
contador_cambiar_opcion_menu = 1

#====================================
#    -----------BUCLE-----------
#====================================
while True: # main game loop
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                contador_cambiar_opcion_menu += 1
                if contador_cambiar_opcion_menu >= 4:
                    contador_cambiar_opcion_menu = 1
            elif event.key == K_UP:
                contador_cambiar_opcion_menu -= 1
                if contador_cambiar_opcion_menu <= 0:
                    contador_cambiar_opcion_menu = 3
            elif event.key == K_RETURN:
                if contador_cambiar_opcion_menu == 2:
                    pygame.quit()
                    sys.exit()

    #================================UPDATE============================
    #------------------Surface
    DISPLAYSURF.fill(NEGRO)

    #------------------Menu
    DISPLAYSURF.blit(logo_cof, ((ANCHO_SCREEN-logo_cof.get_rect()[2])//2, 15))

    if contador_cambiar_opcion_menu == 1:
        texto_inicio = font_grande.render("Inicio", True, BLANCO)
        texto_salir = font_pequeña.render("Salir", True, GRIS_LIGERO)
        texto_prueba = font_pequeña.render("Texto 3", True, GRIS_LIGERO)
        texto_inicio_pos, texto_salir_pos, texto_prueba_pos = ((ANCHO_SCREEN-texto_inicio.get_rect()[2])//2, 295), ((ANCHO_SCREEN-texto_salir.get_rect()[2])//2, 385), ((ANCHO_SCREEN-texto_prueba.get_rect()[2])//2, 455)
    elif contador_cambiar_opcion_menu == 2:
        texto_inicio = font_pequeña.render("Inicio", True, GRIS_LIGERO)
        texto_salir = font_grande.render("Salir", True, BLANCO)
        texto_prueba = font_pequeña.render("Texto 3", True, GRIS_LIGERO)
        texto_inicio_pos, texto_salir_pos, texto_prueba_pos = ((ANCHO_SCREEN-texto_inicio.get_rect()[2])//2, 300), ((ANCHO_SCREEN-texto_salir.get_rect()[2])//2, 360), ((ANCHO_SCREEN-texto_prueba.get_rect()[2])//2, 455)
    elif contador_cambiar_opcion_menu == 3:
        texto_inicio = font_pequeña.render("Inicio", True, GRIS_LIGERO)
        texto_salir = font_pequeña.render("Salir", True, GRIS_LIGERO)
        texto_prueba = font_grande.render("Texto 3", True, BLANCO)
        texto_inicio_pos, texto_salir_pos, texto_prueba_pos = ((ANCHO_SCREEN-texto_inicio.get_rect()[2])//2, 300), ((ANCHO_SCREEN-texto_salir.get_rect()[2])//2, 365), ((ANCHO_SCREEN-texto_prueba.get_rect()[2])//2, 430)

    DISPLAYSURF.blit(texto_inicio, texto_inicio_pos)
    DISPLAYSURF.blit(texto_salir, texto_salir_pos)
    DISPLAYSURF.blit(texto_prueba, texto_prueba_pos)

    #------------------Update, FPS
    pygame.display.update()
    fps_clock.tick(FPS)
