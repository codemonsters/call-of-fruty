#!/usr/bin/env python3

#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from pygame.locals import *
from constantes import *
from jugador import Jugador
import time
#====================================
#     ---------JUEGO---------
#====================================
pygame.init()


# Hacer el quieto y disparando, el saltando y el saltnado y disparando

def movimiento_jugador(jugador, lista_imagenes):
    #----------Estando quieto
    if jugador.moverse == False and jugador.salto == 0:  # Si no se está desplazando hacia los lados ni hacia arriba
        jugador.contador_cambiar_imagen = 0  # Contador para regular el tiempo de cada imagen en un movimiento

        if jugador.disparar == False:  # Si no está haciendo absolutamente nada
            jugador.image = pygame.image.load(lista_imagenes[0])  # Quieto
        else:
            jugador.contador_cambiar_imagen += 1  # Contador para regular el tiempo de cada imagen en un movimiento
            if jugador.contador_cambiar_imagen < 3:
                jugador.image = pygame.image.load(lista_imagenes[0])  # Sentado y sin disparar
            else:
                jugador.image = pygame.image.load(lista_imagenes[2])  # Sentado y disparando
                if jugador.contador_cambiar_imagen >= 6:
                    jugador.contador_cambiar_imagen = 0  # Reiniciamos el movimiento

    #----------Moviéndose
    elif jugador.moverse == True and jugador.salto == 0:  # Si se está movimiendo lateralmente
        jugador.contador_cambiar_imagen += 1  # Contador para regular el tiempo de cada imagen en un movimiento

        if jugador.contador_cambiar_imagen < 3:
            jugador.image = pygame.image.load(lista_imagenes[1])  # Está normal con las 4 patas apoyadas
            jugador.rect.x += 7  # Por el cambio que hay en la posición de la cabeza según la imagen, para que no parezca una gaviota
        elif jugador.contador_cambiar_imagen < 6:
            jugador.image = pygame.image.load(lista_imagenes[2])  # Adelanta las patas delanteras
        elif jugador.contador_cambiar_imagen < 16:
            jugador.image = pygame.image.load(lista_imagenes[3])  # Estira todo el cuerpo
            jugador.rect.x += 10  # Avanza cuando después del impulso salta
            #--Mini efecto de salto hacia arriba
            if jugador.contador_cambiar_imagen < 11:  # Va subiendo
                jugador.rect.y -= 2
            else:  # Va bajando
                jugador.rect.y += 2
        elif jugador.contador_cambiar_imagen < 21:
            jugador.image = pygame.image.load(lista_imagenes[4])  # Recoge solo las patas de delante
            jugador.rect.x += 4  # Adelantamos la imagen para que no parezca que va hacia atrás al terminar el salto
        else:
            jugador.contador_cambiar_imagen = 0  # Se reinicia el movimiento
            jugador.image = pygame.image.load(lista_imagenes[1])

        if jugador.direccion == 'izquierda':
            if jugador.contador_cambiar_imagen < 3:
                jugador.rect.x -= 14  # Contrarrestamos el 7 que le dábamos por el 'movimiento gaviota' (posicion de la cabeza)
            elif jugador.contador_cambiar_imagen < 16 and jugador.contador_cambiar_imagen >= 6:
                jugador.rect.x -= 20  # Contrarrestamos el +10 que se le daba cuando daba el salto
            elif jugador.contador_cambiar_imagen < 21 and jugador.contador_cambiar_imagen >= 16:
                jugador.rect.x -= 8  # Contrarrestamos el +4 que se le daba cuando terminaba el salto

    #----------Saltando
    elif jugador.salto == True:  # Si está saltando
        if jugador.disparar == False:
            jugador.image = pygame.image.load(lista_imagenes[5])  # Salto normal
        else:
            jugador.contador_cambiar_imagen += 1  # Contador para regular el tiempo de cada imagen en un movimiento
            if jugador.contador_cambiar_imagen < 3:
                jugador.image = pygame.image.load(lista_imagenes[5])  # Saltando normal
            else:
                jugador.image = pygame.image.load(lista_imagenes[6])  # Saltando y disparando
                jugador.contador_cambiar_imagen = 0  # Se reinicia el movimiento

    #--Transformar imagen
    if jugador.direccion == 'izquierda':  # Si la dirección es hacia la izquierda rotamos la imagen horizontalmente
        jugador.image = pygame.transform.flip(jugador.image, 1, 0)


def jugar(surface, fps_clock):
    #------------------Fondo
    imagen_fondo = pygame.image.load("imagenes/imagen_fondo.jpg")

    #------------------Jugadores
    jugador1 = Jugador("jugador1_sprite", [500, ALTO_SCREEN-39])
    jugador1.direccion = 'derecha'

    jugador2 = Jugador("jugador2_sprite", [600, ALTO_SCREEN-39])
    jugador2.direccion = 'izquierda'

    #------------------Tiles y disparos
   # piedra = pygame.image.load("imagenes/tile_piedra.png")

    lista_disparos_j1 = pygame.sprite.Group()  # Se almacenan los disparos del jugador 1
    lista_disparos_j2 = pygame.sprite.Group()  # Se almacenan los disparos del jugador 2

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
                    jugador1.tipo_disparo = jugador1.tipos_disparos[0]  # Cambiar el tipo de disparo a manzana
                elif event.key == K_2:
                    jugador1.tipo_disparo = jugador1.tipos_disparos[1]  # Cambiar el tipo de disparo a plátano
                elif event.key == K_3:
                    jugador1.tipo_disparo = jugador1.tipos_disparos[2]  # Cambiar el tipo de disparo a melón

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
                    jugador2.tipo_disparo = jugador2.tipos_disparos[0]  # Cambiar el tipo de disparo a manzana
                elif event.key == K_KP2:
                    jugador2.tipo_disparo = jugador2.tipos_disparos[1]  # Cambiar el tipo de disparo a plátano
                elif event.key == K_KP3:
                    jugador2.tipo_disparo = jugador2.tipos_disparos[2]  # Cambiar el tipo de disparo a melón

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


        #------------------Actualizar disparos jugador 1
        jugador1.actualizar_frecuencia_disparos()  # Esperar un rato para poder lanzar el siguiente disparo
        if jugador1.disparar == True:
            jugador1.atacar(lista_disparos_j1)

        #------------------Actualizar disparos jugador 2
        jugador2.actualizar_frecuencia_disparos()  # Esperar un rato para poder lanzar el siguiente disparo
        if jugador2.disparar == True:
            jugador2.atacar(lista_disparos_j2)

        #========================UPDATE==========================
        #------------------Surface
        surface.blit(imagen_fondo, (0, 0))

        #------------------Jugadores
        jugador1.ajustar_posicion()  # Si se sale de la pantalla
        movimiento_jugador(jugador1, jugador1.images)  # Cambiamos la imagen según su movimiento
        surface.blit(jugador1.image, (jugador1.rect.x, jugador1.rect.y))

        jugador2.ajustar_posicion()  # Si se sale de la pantalla
        movimiento_jugador(jugador2, jugador2.images)  # Cambiamos la imagen según su movimiento
        surface.blit(jugador2.image, (jugador2.rect.x, jugador2.rect.y))

        #------------------Frutas/disparos

        #--Jugador 1
        for disparo in lista_disparos_j1:
            disparo.ajustar_posicion()  # Si se sale de la pantalla
            colision = pygame.sprite.spritecollide(jugador2, lista_disparos_j1, True, pygame.sprite.collide_mask)
            if colision != []:  # Si hay una colisión
                jugador2.life -= disparo.daño
                disparo.kill()  # Eliminamos el disparo
            else:
                surface.blit(disparo.image, (disparo.rect.x, disparo.rect.y))

        #--Jugador 2
        for disparo in lista_disparos_j2:
            disparo.ajustar_posicion()  # Si se sale de la pantalla
            colision = pygame.sprite.spritecollide(jugador1, lista_disparos_j2, True, pygame.sprite.collide_mask)
            if colision != []:  # Si hay una colisión
                jugador1.life -= disparo.daño
                disparo.kill()  # Eliminamos el disparo
            else:
                surface.blit(disparo.image, (disparo.rect.x, disparo.rect.y))

        #------------------Dibujar, FPS
        pygame.display.update()
        fps_clock.tick(FPS)


# Con el jugador 2 al tener varias teclas pulsadas no funciona correctamente (2 movimiento: no disparar, 1 mov & disparar: not 2º mov)
