#!/usr/bin/env python3
"""A simple skiing game.

Day-iteration:
2-1: Screen with stationary rectangle
2-2: Game loop and movement
2-3: User input
"""
import pygame


BOARD_SIZE = 480, 640
FRAME_RATE = 20

pygame.init()

BOARD = pygame.display.set_mode(BOARD_SIZE)
CLOCK = pygame.time.Clock()


player = pygame.Rect(100, 200, 50, 50)

game_on = True
while game_on:
    BOARD.fill((255, 255, 0))
    pygame.draw.rect(BOARD, (255, 0, 0), (player))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_on = False
            elif event.key == pygame.K_LEFT:
                player.x = player.x - 1
            elif event.key == pygame.K_RIGHT:
                player.x = player.x + 1
            elif event.key == pygame.K_UP:
                player.y = player.y - 1
            elif event.key == pygame.K_DOWN:
                player.y = player.y + 1
    pygame.display.flip()
    CLOCK.tick(FRAME_RATE)

pygame.quit()
