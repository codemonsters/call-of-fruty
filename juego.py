#!/usr/bin/env python3

#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from pygame.locals import *
from constantes import *
import jugador

#====================================
#     ---------JUEGO---------
#====================================
pygame.init()

def jugar(surface, fps_clock):
    #------------------Fondo
    imagen_fondo = pygame.image.load("imagenes/imagen_fondo.jpg")

    #------------------Jugadores
    jugador1 = jugador.Jugador("jugador1_sprite", [500, 500])
    jugador2 = jugador.Jugador("jugador2_sprite", [600, 500])

    #------------------Tiles
   # piedra = pygame.image.load("imagenes/tile_piedra.png")

    #========================BUCLE==========================
    while True: # main game loop
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                #------------------Movimiento jugador 1
                if event.key == K_a:
                    jugador1.direccion = 'izquierda'
                elif event.key == K_d:
                    jugador1.direccion = 'derecha'
                elif event.key == K_w:
                    jugador1.salto = 25  # La fuerza irá bajando gracias a la gravedad que se aplicará en cada vuelta
                elif event.key == K_SPACE:
                    jugador1.disparar = True

                #------------------Movimiento jugador 2
                if event.key == K_LEFT:
                    jugador2.direccion = 'izquierda'
                elif event.key == K_RIGHT:
                    jugador2.direccion = 'derecha'
                elif event.key == K_UP:
                    jugador2.salto = 25  # La fuerza irá bajando gracias a la gravedad que se aplicará en cada vuelta
                elif event.key == K_KP_ENTER:
                    jugador2.disparar = True

            elif event.type == KEYUP:
                tecla_pulsada = pygame.key.get_pressed()
                #------------------Movimiento jugador 1
                if event.key == K_a:
                    jugador1.direccion = None
                    if tecla_pulsada[K_d]:
                        jugador1.direccion = 'derecha'
                elif event.key == K_d:
                    jugador1.direccion = None
                    if tecla_pulsada[K_a]:
                        jugador1.direccion = 'izquierda'
                elif event.key == K_SPACE:
                    jugador1.disparar = False

                #------------------Movimiento jugador 2
                if event.key == K_RIGHT:
                    jugador2.direccion = None
                    if tecla_pulsada[K_LEFT]:
                        jugador2.direccion = 'izquierda'
                elif event.key == K_LEFT:
                    jugador2.direccion = None
                    if tecla_pulsada[K_RIGHT]:
                        jugador2.direccion = 'derecha'
                elif event.key == K_KP_ENTER:
                    jugador2.disparar = False

        #========================UPDATE==========================
        #------------------Surface
        surface.blit(imagen_fondo, (0, 0))

        #------------------Jugadores
        jugador1.actualizar_movimiento()
        surface.blit(jugador1.image, jugador1.pos)

        jugador2.actualizar_movimiento()
        surface.blit(jugador2.image, jugador2.pos)

        #------------------Frutas/disparos

        #------------------Dibujar, FPS
        pygame.display.update()
        fps_clock.tick(FPS)


# Si mantengo presionado dos teclas de movimiento(derecha e izquierda) del mismo jugador y salto no entra al bucle de KEYDOWN (no capta la señal)