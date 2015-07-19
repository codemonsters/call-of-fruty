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
    def __init__(self, posicion):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/jugador_sprite" + "_0.png")
        self.images = ["imagenes/jugador_sprite"+"_0.png", "imagenes/jugador_sprite"+"_1.png", "imagenes/jugador_sprite"+"_2.png",
                       "imagenes/jugador_sprite"+"_3.png", "imagenes/jugador_sprite"+"_4.png", "imagenes/jugador_sprite"+"_5.png",
                       "imagenes/jugador_sprite"+"_6.png", "imagenes/jugador_sprite"+"_7.png", "imagenes/jugador_sprite"+"_8.png"]
        self.life = 500

        self.rect = self.image.get_rect()
        self.direccion = None
        self.salto = 0  # Fuerza del salto
        self.moverse = False
        self.contador_cambiar_imagen = 0  # Contador para regular el tiempo de cada imagen en un movimiento
        self.rect.x, self.rect.y = posicion[0], posicion[1]

        self.disparar = False
        self.contador_frecuencia_disparos = 10  # Que haya que esperar un tiempo para poder disparar otro disparo
        self.tipos_disparos = ["manzana", "platano", "melon"]
        self.tipo_disparo = self.tipos_disparos[0]

    def ajustar_posicion(self):  # Si se sale de la pantalla
        if self.moverse == True or self.salto != 0:
            #------------------Hacia los lados
            if self.rect.x <= 0 and self.direccion == 'izquierda':
                self.moverse = False
                self.rect.x = 1  # Para que en la siguiente vuelta del bucle no cuente como que está en 0 y su movimiento no sea False
            if self.rect.x+self.image.get_rect()[2] >= ANCHO_SCREEN and self.direccion == 'derecha':
                self.moverse = False
                self.rect.x = ANCHO_SCREEN-pygame.image.load(self.images[0]).get_rect()[2]-1   # -1 para que en la siguiente vuelta del bucle no cuente como que está en ANCHO_SCREEN y su movimiento no sea False

            if self.rect.y+self.image.get_rect()[3] > ALTO_SCREEN:
                self.rect.y = ALTO_SCREEN-self.image.get_rect()[3]

        #------------------Salto
        if self.salto != 0:  # La fuerza puede ser mayor (subiendo) o menor (volviendo al suelo)
            if self.rect.y+self.image.get_rect()[3] >= ALTO_SCREEN:
                self.image = pygame.image.load(self.images[0])
                self.rect.y = ALTO_SCREEN-self.image.get_rect()[3]
                self.salto = 0  # Toca el suelo
        elif self.salto == 0 and self.contador_cambiar_imagen == 0:
            self.rect.y = ALTO_SCREEN-self.image.get_rect()[3]  # Por si queda un poco en el aire debido al minisalto del desplazamiento lateral

    def actualizar_frecuencia_disparos(self):
        self.contador_frecuencia_disparos += 1
        if self.contador_frecuencia_disparos >= 10:
            self.contador_frecuencia_disparos = 10

    def atacar(self, lista_disparos):
        if self.contador_frecuencia_disparos == 10:  # Si el contador está al máximo (10) significa que ya pasó el tiempo suficiente para volver a disparar
            self.contador_frecuencia_disparos = 0  # Cuando dispara el contador se pone a 0
            if self.tipo_disparo == "manzana":
                lista_disparos.add(Disparo("manzana", (self.rect.x, self.rect.y), self.direccion, 5))
            elif self.tipo_disparo == "platano":
                lista_disparos.add(Disparo("platano", (self.rect.x, self.rect.y), self.direccion, 10))
            elif self.tipo_disparo == "melon":
                lista_disparos.add(Disparo("melon", (self.rect.x, self.rect.y), self.direccion, 15))
