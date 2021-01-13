import pygame
from os import path
from Constants import text_color


class Text:
    def __init__(self, text, size, coord):
        self.font = pygame.font.Font(path.join("data", "kongtext.ttf"), size)
        self.text = text
        self.coord = coord

    def draw(self, surface):
        text = self.font.render(self.text, False, text_color)
        rect = text.get_rect(center=self.coord)
        surface.blit(text, rect)
