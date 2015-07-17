#!/usr/bin/env python3

#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from pygame.locals import *
from constantes import *
import menu
import juego

#====================================
#     ----------CUERPO----------
#====================================
#------------------Inicializar
pygame.init()
DISPLAYSURF = pygame.display.set_mode((ANCHO_SCREEN, ALTO_SCREEN))
pygame.display.set_caption('Call Of Fruty')
fps_clock = pygame.time.Clock()

#====================================
#     ----------JUEGO----------
#====================================
menu.menu(DISPLAYSURF, fps_clock)  # Activamos el menú, desde donde se podrá activar el juego


