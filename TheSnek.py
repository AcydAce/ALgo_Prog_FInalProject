from system import *
class SNEK:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]       #  Snek starting position
        self.direction = Vector2(1, 0)                                     #  Snek starting direction = right
        self.new_block = False                                             #  Stops Snek from growing until it gains a point

        self.head_up = pygame.image.load("Sprites/Snek_up.png").convert_alpha()                     #-----------------------------
        self.head_right = pygame.image.load("Sprites/Snek_right.png").convert_alpha()
        self.head_down = pygame.image.load("Sprites/Snek_down.png").convert_alpha()
        self.head_left = pygame.image.load("Sprites/Snek_left.png").convert_alpha()

        self.tail_up = pygame.image.load("Sprites/tail_up.png").convert_alpha()
        self.tail_right = pygame.image.load("Sprites/tail_right.png").convert_alpha()                # Snek Sprites
        self.tail_down = pygame.image.load("Sprites/tail_down.png").convert_alpha()
        self.tail_left = pygame.image.load("Sprites/tail_left.png").convert_alpha()

        self.body_vertical = pygame.image.load("Sprites/body_vertical.png").convert_alpha()
        self.body_horizontal = pygame.image.load("Sprites/body_horizontal.png").convert_alpha()

        self.up_left = pygame.image.load("Sprites/up_left.png").convert_alpha()
        self.up_right = pygame.image.load("Sprites/up_right.png").convert_alpha()
        self.down_right = pygame.image.load("Sprites/down_right.png").convert_alpha()
        self.down_left = pygame.image.load("Sprites/down_left.png").convert_alpha()                 #----------------------------


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