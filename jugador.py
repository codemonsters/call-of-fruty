#!/usr/bin/env python3

#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from constantes import *
from disparo import Disparo

#====================================
#     -------- CLASE Jugador --------
#====================================

class Jugador(pygame.sprite.Sprite):
    def __init__(self, imagen, posicion):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/" + imagen + "_0.png")
        self.images = ["imagenes/"+imagen+"_0.png", "imagenes/"+imagen+"_1.png", "imagenes/"+imagen+"_2.png",
                       "imagenes/"+imagen+"_3.png", "imagenes/"+imagen+"_4.png", "imagenes/"+imagen+"_5.png"]
        self.life = 500

        self.rect = self.image.get_rect()
        self.direccion = None
        self.salto = 0
        self.moverse = False
        self.contador_cambiar_imagen = 0  # Para dar el efecto de andar, si es True se cambia a quieto
        self.rect.x, self.rect.y = posicion[0], posicion[1]

        self.disparar = False
        self.contador_frecuencia_disparos = 10
        self.tipos_disparos = ["manzana", "platano", "melon"]
        self.tipo_disparo = self.tipos_disparos[0]

    def actualizar_movimiento(self):
        if self.moverse == True:
            #------------------Hacia los lados
            if self.direccion == 'izquierda':
                self.rect.x -= 5
                if self.rect.x <= 0:
                    self.moverse = False
                    self.rect.x = 0

            elif self.direccion == 'derecha':
                self.rect.x += 5
                if self.rect.x+self.image.get_rect()[2] >= ANCHO_SCREEN:
                    self.moverse = False
                    self.rect.x = ANCHO_SCREEN-self.image.get_rect()[2]

        #------------------Salto y gravedad
        if self.salto != 0:
            self.rect.y -= self.salto  # Salto (puede ser positivo al dar el salto o negativo cuando no le queda fuerza)
            self.salto -= 1  # Gravedad, cada vez el salto será mas pequeño y pasará a ser negativo (cuando baja)
            if self.rect.y+self.image.get_rect()[3] >= ALTO_SCREEN:
                self.rect.y = ALTO_SCREEN-self.image.get_rect()[3]
                self.salto = 0

    def actualizar_frecuencia_disparos(self):
        self.contador_frecuencia_disparos += 1
        if self.contador_frecuencia_disparos >= 10:
            self.contador_frecuencia_disparos = 10

    def atacar(self, lista_disparos):
        if self.contador_frecuencia_disparos == 10:
            self.contador_frecuencia_disparos = 0
            if self.tipo_disparo == "manzana":
                lista_disparos.add(Disparo("manzana", (self.rect.x, self.rect.y), self.direccion, 5))
            elif self.tipo_disparo == "platano":
                lista_disparos.add(Disparo("platano", (self.rect.x, self.rect.y), self.direccion, 10))
            elif self.tipo_disparo == "melon":
                lista_disparos.add(Disparo("melon", (self.rect.x, self.rect.y), self.direccion, 15))
