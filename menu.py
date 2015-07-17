#!/usr/bin/env python3

#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from pygame.locals import *
from constantes import *
import juego

#====================================
#     ----------CUERPO----------
#====================================
pygame.init()

logo_cof = pygame.image.load("imagenes/call of fruty.png")

font_pequeña = pygame.font.Font("Astounding news.ttf", 80)
font_grande = pygame.font.Font("Astounding news.ttf", 110)

#====================================
#     --------FUNCIONES--------
#====================================
def menu(surface, fps_clock):
    contador_cambiar_opcion_menu = 1  # Opción en la que estás de todo el menú (jugar, records o salir)
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
                    if contador_cambiar_opcion_menu == 1:
                        juego.jugar(surface, fps_clock)
                    elif contador_cambiar_opcion_menu == 2:
                        pass
                    elif contador_cambiar_opcion_menu == 3:
                        pygame.quit()
                        sys.exit()

        #========================UPDATE==========================
        #------------------Surface
        surface.fill((0, 0, 0))
        surface.blit(logo_cof, ((ANCHO_SCREEN-logo_cof.get_rect()[2])//2, 15))

        #------------------Textos menú
        if contador_cambiar_opcion_menu == 1:
            texto_inicio = font_grande.render("Inicio", True, BLANCO)
            texto_records = font_pequeña.render("Records", True, GRIS_LIGERO)
            texto_salir = font_pequeña.render("Salir", True, GRIS_LIGERO)
            texto_inicio_pos, texto_records_pos, texto_salir_pos = ((ANCHO_SCREEN-texto_inicio.get_rect()[2])//2, 295), ((ANCHO_SCREEN-texto_records.get_rect()[2])//2, 385), ((ANCHO_SCREEN-texto_salir.get_rect()[2])//2, 455)

        elif contador_cambiar_opcion_menu == 2:
            texto_inicio = font_pequeña.render("Inicio", True, GRIS_LIGERO)
            texto_records = font_grande.render("Records", True, BLANCO)
            texto_salir = font_pequeña.render("Salir", True, GRIS_LIGERO)
            texto_inicio_pos, texto_records_pos, texto_salir_pos = ((ANCHO_SCREEN-texto_inicio.get_rect()[2])//2, 300), ((ANCHO_SCREEN-texto_records.get_rect()[2])//2, 360), ((ANCHO_SCREEN-texto_salir.get_rect()[2])//2, 455)

        elif contador_cambiar_opcion_menu == 3:
            texto_inicio = font_pequeña.render("Inicio", True, GRIS_LIGERO)
            texto_records = font_pequeña.render("Records", True, GRIS_LIGERO)
            texto_salir = font_grande.render("Salir", True, BLANCO)
            texto_inicio_pos, texto_records_pos, texto_salir_pos = ((ANCHO_SCREEN-texto_inicio.get_rect()[2])//2, 300), ((ANCHO_SCREEN-texto_records.get_rect()[2])//2, 365), ((ANCHO_SCREEN-texto_salir.get_rect()[2])//2, 430)

        surface.blit(texto_inicio, texto_inicio_pos)
        surface.blit(texto_records, texto_records_pos)
        surface.blit(texto_salir, texto_salir_pos)

        #------------------Dibujar, FPS
        pygame.display.update()
        fps_clock.tick(FPS)