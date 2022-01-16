import pygame
import sys
from pygame.math import Vector2
from main import MAIN

pygame.init()
cell_size = 32
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))  # displays window
clock = pygame.time.Clock()  # keeps fps from going too high
borgir = pygame.image.load("Sprites/Borgir 100%.png").convert_alpha()
game_font = pygame.font.Font("Font/pixelmix.ttf", 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()


while True:                             # event loop
    for event in pygame.event.get():
        if event.type == pygame.display.quit:   # allows the window to be closed
            pygame.display.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:  # makes move_snek in line 40 into event
            main_game.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snek.direction.y != 1:
                    main_game.snek.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT:
                if main_game.snek.direction.x != -1:
                    main_game.snek.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN:
                if main_game.snek.direction.y != -1:
                    main_game.snek.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snek.direction.x != 1:
                    main_game.snek.direction = Vector2(-1, 0)

    screen.fill((255, 255, 255))         # Background Color
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)                      # runs max 60 fps
