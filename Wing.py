import pygame
from Constants import *
from ObjectWithSprite import *


class Wing(ObjectWithSprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.w, self.h = wing_size
        self.image = pygame.Surface((self.w, self.h))
        self.rect = self.image.get_rect()
        self.create_image()

    def get_size(self):
        return self.w, self.h

    def update(self, fps):
        pass

    def create_image(self, color="White"):
        background_color = pygame.Color(color)
        outline_color = pygame.Color(background_color)
        outline_color.hsva = outline_color.hsva[0], outline_color.hsva[1], \
                             max(outline_color.hsva[2] - 30, 0)
        self.image.fill(background_color)
        pygame.draw.rect(self.image, outline_color, (0, 0, self.w, self.h), 10)

    def update_image(self, color):
        self.create_image(color=color)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
