import pygame


class ObjectWithSprite(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
