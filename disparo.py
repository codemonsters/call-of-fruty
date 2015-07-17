#!/usr/bin/env python3

#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from constantes import *

#====================================
#     ------- CLASE Disparo ---------
#====================================

class Disparo(pygame.sprite.Sprite):
    def __init__(self, imagen, posicion, direccion_disparo, daño):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/" + imagen + ".png").convert_alpha()
        self.rect = self.image.get_rect()

        if direccion_disparo == 'izquierda':
            self.rect.x, self.rect.y = posicion[0], posicion[1]
        else:
            self.rect.x, self.rect.y = posicion[0], posicion[1]
        self.direccion = direccion_disparo
        self.daño = daño

    def ajustar_posicion(self):
        if self.direccion == 'izquierda':
            self.rect.x -= 15
            if self.rect.x <= 0:
                self.kill()
        elif self.direccion == 'derecha':
            self.rect.x += 15
            if self.rect.x+self.image.get_rect()[2] >= ANCHO_SCREEN:
                self.kill()
