#!/usr/bin/env python3

#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from pygame.locals import *
from constantes import *
import juego

#====================================
#     ----------CLASES----------
#====================================
class Jugador(pygame.sprite.Sprite):
    def __init__(self, imagen, posicion):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/" + imagen + ".png")
        self.images = []

        self.rect = self.image.get_rect()
        self.direccion = None
        self.salto = None
        self.pos = posicion

        self.disparar = False

    def actualizar_movimiento(self):
        #------------------Hacia los lados
        if self.direccion == 'izquierda':
            self.pos[0] -= 5
            if self.pos[0] <= 0:
                self.pos[0] = 0

        elif self.direccion == 'derecha':
            self.pos[0] += 5
            if self.pos[0]+self.image.get_rect()[2] >= ANCHO_SCREEN:
                self.pos[0] = ANCHO_SCREEN-self.image.get_rect()[2]

        #------------------Salto y gravedad
        if self.salto != None:
            self.pos[1] -= self.salto  # Salto (puede ser positivo al dar el salto o negativo cuando no le queda fuerza)
            self.salto -= 1  # Gravedad, cada vez el salto será mas pequeño y pasará a ser negativo (cuando baja)
            if self.pos[1]+self.image.get_rect()[3] >= ALTO_SCREEN:
                self.pos[1] = ALTO_SCREEN-self.image.get_rect()[3]
                self.salto = None

    def atacar(self, tipo_arma):
        pass