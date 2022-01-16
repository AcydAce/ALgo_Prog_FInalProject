import sys
import pygame
import random
from pygame.math import Vector2

class SNEK:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]       #  Snek starting position
        self.direction = Vector2(1, 0)                                     #  Snek starting direction = right
        self.new_block = False                                             #  Stops Snek from growing until it gains a point

        self.head_up = pygame.image.load("../Sprites/Snek_up.png").convert_alpha()                     #-----------------------------
        self.head_right = pygame.image.load("../Sprites/Snek_right.png").convert_alpha()
        self.head_down = pygame.image.load("../Sprites/Snek_down.png").convert_alpha()
        self.head_left = pygame.image.load("../Sprites/Snek_left.png").convert_alpha()

        self.tail_up = pygame.image.load("../Sprites/tail_up.png").convert_alpha()
        self.tail_right = pygame.image.load("../Sprites/tail_right.png").convert_alpha()                # Snek Sprites
        self.tail_down = pygame.image.load("../Sprites/tail_down.png").convert_alpha()
        self.tail_left = pygame.image.load("../Sprites/tail_left.png").convert_alpha()

        self.body_vertical = pygame.image.load("../Sprites/body_vertical.png").convert_alpha()
        self.body_horizontal = pygame.image.load("../Sprites/body_horizontal.png").convert_alpha()

        self.up_left = pygame.image.load("../Sprites/up_left.png").convert_alpha()
        self.up_right = pygame.image.load("../Sprites/up_right.png").convert_alpha()
        self.down_right = pygame.image.load("../Sprites/down_right.png").convert_alpha()
        self.down_left = pygame.image.load("../Sprites/down_left.png").convert_alpha()                 #----------------------------


    def draw_snek(self):
        self.update_head_graphics()                 # manages sprite direction
        self.update_tail_graphics()
        for index,block in enumerate(self.body):

            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)    # manages Grid Position for snek

            if index == 0:                                                  # figures out which block is the head
                screen.blit(self.head, block_rect)       # through which block moves first
            elif index == len(self.body) - 1:            # detects the tail
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block  # detects previous and next body parts                       ---------
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:            # if block after and previous same x pos = vertical         #the body
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:            # if block after and previous same y pos = horizontal     ---------
                    screen.blit(self.body_horizontal, block_rect)

                else:
                    if previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:  # if previous block is bottom and if next block is right
                        screen.blit(self.up_left, block_rect)
                    if previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:  # if previous left is left and if next block is below
                        screen.blit(self.up_right, block_rect)
                    if previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:  # if previous above is left and if next block is right
                        screen.blit(self.down_left, block_rect)
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:  # if previous block is above and if next block is left
                        screen.blit(self.down_right, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]  # selects the block before the head
        if head_relation == Vector2(1, 0):
            self.head = self.head_left          # snake faces right
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right         # snake faces left
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up            # snake faces down
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]  # selects the block before the head
        if tail_relation == Vector2(-1, 0):
            self.tail = self.tail_left  # snake faces right
        elif tail_relation == Vector2(1, 0):
            self.tail = self.tail_right  # snake faces left
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_up  # snake faces down
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_down


    def move_snek(self):
        if self.new_block == True:
            body_copy = self.body[:]  # copy and add snek body and removes last body
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]  # copy and add snek body and removes last body
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

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

class MAIN:
    def __init__(self):
        self.snek = SNEK()
        self.fruit = FRUIT()

    def update(self):
        self.snek.move_snek()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_bg()
        self.fruit.draw_fruit()
        self.snek.draw_snek()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snek.body[0]:
            self.fruit.randomize()
            self.snek.add_block()

        for block in self.snek.body[1:]:  # if fruit spawns on body, rerandomize
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snek.body[0].x < cell_number or not 0 <= self.snek.body[0].y < cell_number:
            self.game_over()

        for block in self.snek.body[1:]:
            if block == self.snek.body[0]:
                self.game_over()

    def game_over(self):
        pygame.display.quit()
        sys.exit()

    def draw_bg(self):
        bg_1 = (234, 234, 255)

        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        bg_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, bg_1, bg_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        bg_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, bg_1, bg_rect)

    def draw_score(self):
        score_text = str(len(self.snek.body) - 3)  # starting score starts with 0, since snek starts with 3, score -3
        score_surface = game_font.render(score_text, True, (15, 15, 15))
        score_x = int(60)                         # positions the score from top left
        score_y = int(40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))    # gives score rect
        borgir_rect = borgir.get_rect(midright = (score_rect.left - 5, score_rect.centery))
        bg_rect = pygame.Rect(borgir_rect.left - 4, borgir_rect.top - 5, borgir_rect.width + score_rect.width + 10, borgir_rect.height + 10)

        pygame.draw.rect(screen, (229, 255, 204), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(borgir, borgir_rect)
        pygame.draw.rect(screen, (0, 204, 102), bg_rect, 2)

pygame.init()
cell_size = 32
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))  # displays window
clock = pygame.time.Clock()  # keeps fps from going too high
borgir = pygame.image.load("../Sprites/Borgir 100%.png").convert_alpha()
game_font = pygame.font.Font("../Font/pixelmix.ttf", 25)

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