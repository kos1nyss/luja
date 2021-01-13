import pygame


class Object:
    def __init__(self, coord):
        self.rect = pygame.Rect((*coord, 0, 0))

    def set_coord(self, coord):
        self.rect.x, self.rect.y = coord

    def get_coord(self):
        return self.rect.x, self.rect.y

    def move(self, delta):
        self.rect.x += delta[0]
        self.rect.y += delta[1]
