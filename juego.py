#!/usr/bin/env python3

#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from pygame.locals import *
from constantes import *


pygame.init()

def jugar(surface, fps_clock):
    imagen_fondo = pygame.image.load("imagenes/imagen_fondo.jpg")
    imagen_jugador = pygame.image.load("imagenes/jugador_sprite.png")
    while True: # main game loop
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()

        surface.blit(imagen_fondo, (0, 0))
        surface.blit(imagen_jugador, (300, 500))
        #pygame.draw.rect(surface, pygame.Color(255, 0, 0), pygame.Rect(360, 100, 20, 20))  # Rojo
        #pygame.draw.rect(surface, pygame.Color(255, 0, 0), pygame.Rect(385, 100, 30, 50))  # Rojo

        #------------------Dibujar, FPS
        pygame.display.update()
        fps_clock.tick(FPS)