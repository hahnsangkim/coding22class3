#!/usr/bin/env python3
"""A simple skiing game.
"""
import pygame


BOARD_SIZE = BOARD_WIDTH, BOARD_HEIGHT = 600, 800
FRAME_RATE = 20

pygame.init()

BOARD = pygame.display.set_mode(BOARD_SIZE)
CLOCK = pygame.time.Clock()

player_x = 50
player_y = 50

player_image = pygame.image.load('images/kiiro.png')

# 2: create a tree at (300, 400)
BOARD_WIDTH, BOARD_HEIGHT = 600, 800
import random
tree_image = pygame.image.load('images/tree.png')
tree_x = 300
tree_y = 400
# then at a random position
tree_width, tree_height = tree_image.get_size()
tree_x = random.randint(0, BOARD_WIDTH - tree_width)
tree_y = random.randint(0, BOARD_HEIGHT)
# 2: challenge 1 - make the tree moving-up
DOWNHILL_SPEED = 4
tree_y_inc = -DOWNHILL_SPEED

game_on = True
while game_on:
    BOARD.fill((255, 255, 255))
    BOARD.blit(player_image, (player_x, player_y))
    # 2: display a tree
    BOARD.blit(tree_image, (tree_x, tree_y))

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
    # 2: challenge 1 - update a tree coordinate
    tree_y = tree_y + tree_y_inc
    if tree_y < -tree_height:
        tree_y = BOARD_HEIGHT

    pygame.display.flip()
    CLOCK.tick(FRAME_RATE)

pygame.quit()
