import pygame
from Text import Text


class Points(Text):
    def __init__(self, size, coord):
        self.points = 0
        super().__init__(str(self.points), size, coord)

    def shake(self):
        pass

    def update(self):
        pass

    def add(self):
        self.points += 1
        self.text = str(self.points)
