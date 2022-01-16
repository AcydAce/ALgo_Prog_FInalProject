from TheFruit import FRUIT
from TheSnek import SNEK
from system import *

class MAIN:
    def __init__(self):
        self.snek = SNEK()
        self.fruit = FRUIT()

    def system(self):
        self.system()

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

