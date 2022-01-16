import random

from system import *

class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)    # manages Grid Position for fruit
        screen.blit(borgir, fruit_rect)                                                  # manages characteristics of fruit

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)  # randomizes x and y position
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)