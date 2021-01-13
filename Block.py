import pygame
from Constants import WIDTH, HEIGHT, CENTER, LEFT, RIGHT
from ObjectWithSprite import *


class Block(ObjectWithSprite):
    def __init__(self, coord, size, color, side, speed):
        super().__init__()
        self.create_image(coord, size, color)
        self.coord_x = self.rect.x
        self.size = list(size)
        self.color = color
        self.side = side
        self.speed = speed

    def move(self, delta):
        self.rect.x += delta[0]
        self.rect.y += delta[1]

    def create_image(self, coord, size, color):
        w, h = size
        self.image = pygame.Surface((w, h))
        self.rect = self.image.get_rect(center=(coord[0], coord[1]))

        background_color = pygame.Color(color)
        outline_color = pygame.Color(background_color)
        outline_color.hsva = outline_color.hsva[0], outline_color.hsva[1], \
                             max(outline_color.hsva[2] - 30, 0)
        self.image.fill(background_color)
        pygame.draw.rect(self.image, outline_color, (0, 0, w, h), 10)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def grow(self, fps):
        delta = self.speed / fps
        if self.side == CENTER:
            self.size[0] += delta
            self.coord_x -= delta / 2
        if self.side == LEFT:
            self.size[0] += delta
        if self.side == RIGHT:
            self.size[0] += delta
            self.coord_x -= delta
        self.create_image((self.coord_x + self.size[0] // 2,
                           self.rect.y + self.size[1] // 2), self.size, self.color)
