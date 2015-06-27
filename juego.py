#!/usr/bin/env python3

#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from pygame.locals import *
from constantes import *
from jugador import Jugador

#====================================
#     ---------JUEGO---------
#====================================
pygame.init()

def jugar(surface, fps_clock):
    #------------------Fondo
    imagen_fondo = pygame.image.load("imagenes/imagen_fondo.jpg")

    #------------------Jugadores
    jugador1 = Jugador("jugador1_sprite", [500, ALTO_SCREEN-50])
    jugador1.direccion = 'derecha'

    jugador2 = Jugador("jugador2_sprite", [600, ALTO_SCREEN-50])
    jugador2.direccion = 'izquierda'

    #------------------Tiles y disparos
   # piedra = pygame.image.load("imagenes/tile_piedra.png")

    lista_disparos_j1 = pygame.sprite.Group()
    lista_disparos_j2 = pygame.sprite.Group()

    #========================BUCLE==========================
    while True: # main game loop
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                #------------------Movimiento y ataque jugador 1
                if event.key == K_a:
                    jugador1.moverse = True
                    jugador1.direccion = 'izquierda'
                elif event.key == K_d:
                    jugador1.moverse = True
                    jugador1.direccion = 'derecha'
                elif event.key == K_w:
                    jugador1.salto = 25  # La fuerza irá bajando gracias a la gravedad que se aplicará en cada vuelta

                elif event.key == K_SPACE:
                    jugador1.disparar = True
                elif event.key == K_1:
                    jugador1.tipo_disparo = jugador1.tipos_disparos[0]  # Cambiar el tipo de disparo (manzana, plátano, melón)
                elif event.key == K_2:
                    jugador1.tipo_disparo = jugador1.tipos_disparos[1]
                elif event.key == K_3:
                    jugador1.tipo_disparo = jugador1.tipos_disparos[2]

                #------------------Movimiento y ataque jugador 2
                if event.key == K_LEFT:
                    jugador2.moverse = True
                    jugador2.direccion = 'izquierda'
                elif event.key == K_RIGHT:
                    jugador2.moverse = True
                    jugador2.direccion = 'derecha'
                elif event.key == K_UP:
                    jugador2.salto = 25  # La fuerza irá bajando gracias a la gravedad que se aplicará en cada vuelta

                elif event.key == K_KP_ENTER:
                    jugador2.disparar = True
                elif event.key == K_KP1:
                    jugador2.tipo_disparo = jugador2.tipos_disparos[0]
                elif event.key == K_KP2:
                    jugador2.tipo_disparo = jugador2.tipos_disparos[1]
                elif event.key == K_KP3:
                    jugador2.tipo_disparo = jugador2.tipos_disparos[2]

            elif event.type == KEYUP:
                tecla_pulsada = pygame.key.get_pressed()  # Para que siga moviéndose si mantienes dos teclas pulsadas al mismo tiempo y sueltas una
                #------------------Movimiento y ataque jugador 1
                if event.key == K_a:
                    jugador1.moverse = False
                    if tecla_pulsada[K_d]:
                        jugador1.moverse = True
                        jugador1.direccion = 'derecha'
                elif event.key == K_d:
                    jugador1.moverse = False
                    if tecla_pulsada[K_a]:
                        jugador1.moverse = True
                        jugador1.direccion = 'izquierda'
                elif event.key == K_SPACE:
                    jugador1.disparar = False

                #------------------Movimiento y ataque jugador 2
                if event.key == K_LEFT:
                    jugador2.moverse = False
                    if tecla_pulsada[K_RIGHT]:
                        jugador2.moverse = True
                        jugador2.direccion = 'derecha'
                elif event.key == K_RIGHT:
                    jugador2.moverse = False
                    if tecla_pulsada[K_LEFT]:
                        jugador2.moverse = True
                        jugador2.direccion = 'izquierda'
                elif event.key == K_KP_ENTER:
                    jugador2.disparar = False


        jugador1.actualizar_frecuencia_disparos()
        if jugador1.disparar == True:
            jugador1.atacar(lista_disparos_j1)

        jugador2.actualizar_frecuencia_disparos()
        if jugador2.disparar == True:
            jugador2.atacar(lista_disparos_j2)

        #========================UPDATE==========================
        #------------------Surface
        surface.blit(imagen_fondo, (0, 0))

        #------------------Jugadores
        jugador1.actualizar_movimiento()
        surface.blit(jugador1.image, (jugador1.rect.x, jugador1.rect.y))

        jugador2.actualizar_movimiento()
        surface.blit(jugador2.image, (jugador2.rect.x, jugador2.rect.y))

        #------------------Frutas/disparos
        #--Jugador 1
        for disparo in lista_disparos_j1:
            disparo.actualizar_movimiento()
            colision = pygame.sprite.spritecollide(jugador2, lista_disparos_j1, True, pygame.sprite.collide_mask)
            if colision != []:
                disparo.kill()
                jugador2.life -= 10
            else:
                surface.blit(disparo.image, (disparo.rect.x, disparo.rect.y))
                #pygame.display.update()
                #time.sleep(1)

        #--Jugador 2
        for disparo in lista_disparos_j2:
            disparo.actualizar_movimiento()
            colision = pygame.sprite.spritecollide(jugador1, lista_disparos_j2, True, pygame.sprite.collide_mask)
            if colision != []:
                disparo.kill()
                jugador1.life -= 10
            else:
                surface.blit(disparo.image, (disparo.rect.x, disparo.rect.y))

        #------------------Dibujar, FPS
        pygame.display.update()
        fps_clock.tick(FPS)


# Con el jugador 2 al tener varias teclas pulsadas no funciona correctamente (2 movimiento: no disparar, 1 mov & disparar: not 2º mov)
