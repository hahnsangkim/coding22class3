#!/usr/bin/env python3
"""A simple skiing game.
"""
import pygame


BOARD_SIZE = 480, 640
FRAME_RATE = 20

pygame.init()

BOARD = pygame.display.set_mode(BOARD_SIZE)
CLOCK = pygame.time.Clock()

player_x = 50
player_y = 50

player_image = pygame.image.load('images/kiiro.png')

game_on = True
while game_on:
    BOARD.fill((255, 255, 255))
    BOARD.blit(player_image, (player_x, player_y))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_on = False
            elif event.key == pygame.K_LEFT:
                player_x = player_x - 1
            elif event.key == pygame.K_RIGHT:
                player_x = player_x + 1
            elif event.key == pygame.K_UP:
                player_y = player_y - 1
            elif event.key == pygame.K_DOWN:
                player_y = player_y + 1
                
    pygame.display.flip()
    CLOCK.tick(FRAME_RATE)

pygame.quit()
