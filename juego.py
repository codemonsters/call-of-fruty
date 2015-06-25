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
    while True: # main game loop
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()

        surface.blit(imagen_fondo, (0, 0))


        #------------------Dibujar, FPS
        pygame.display.update()
        fps_clock.tick(FPS)