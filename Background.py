import pygame
from random import randint
from ObjectWithSprite import *
from Constants import HEIGHT, WIDTH, shadows_color, bg_color, bg_rect_size


class Background(ObjectWithSprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.rects = []
        self.create()

    def get_rectangles(self):
        return self.rects

    def create(self):
        for y in range(HEIGHT // bg_rect_size + 1):
            for x in range(WIDTH // bg_rect_size):
                self.rects.append([self.random_color(),
                                   [x * bg_rect_size,
                                    y * bg_rect_size,
                                    bg_rect_size,
                                    bg_rect_size]])

    def new_line(self):
        y = self.rects[0][1][1] - bg_rect_size
        for x in range(WIDTH // bg_rect_size):
            self.rects.insert(0, [self.random_color(),
                                  [x * bg_rect_size,
                                   y,
                                   bg_rect_size,
                                   bg_rect_size]])

    def delete_line(self):
        delete = []
        for rect in self.rects:
            if rect[1][1] >= 1500:
                delete.append(rect)
        new_rects = []
        for rect in self.rects:
            if rect not in delete:
                new_rects.append(rect)
        self.rects = new_rects

    def update(self, fps, *shadows):
        self.update_logic()
        self.update_image(shadows)

    def update_logic(self):
        if self.rects[0][1][1] >= 0:
            self.new_line()
            self.delete_line()

    def update_image(self, shadows):
        self.image.fill(bg_color)
        for rct in self.rects:
            pygame.draw.rect(self.image, rct[0], rct[1])
        for shadow in shadows:
            pygame.draw.rect(self.image, shadows_color, (shadow.rect.x,
                                                         shadow.rect.y + 85,
                                                         shadow.rect.w,
                                                         20))

    def update_colors(self):
        for rect in self.rects:
            rect[0] = self.random_color()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def random_color(self):
        return pygame.Color(bg_color.r + randint(-5, 5),
                            bg_color.g + randint(-5, 5),
                            bg_color.b + randint(-5, 5))

    def lose(self):
        delta = 2
        for rect in self.rects:
            rect[0].r = max(0, rect[0].r - delta)
            rect[0].g = max(0, rect[0].g - delta)
            rect[0].b = max(0, rect[0].b - delta)
