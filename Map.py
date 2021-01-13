import pygame
from Line import *


class Map:
    def __init__(self):
        self.lines = []
        self.first_touch = False

    def get_blocks(self):
        blocks = []
        for line in self.lines:
            blocks.extend(line.get_blocks())
        return blocks

    def get_lines(self):
        return self.lines

    def get_first_touch(self):
        return self.first_touch

    def add_line(self, coord, player_color):
        new_line = Line(self, coord, player_color)
        self.lines.append(new_line)

    def draw(self, surface):
        for line in self.lines:
            for block in line.get_blocks():
                block.draw(surface)

    def update(self, fps):
        for line in self.lines:
            line.update(fps)

    def update_first_touch(self):
        self.first_touch = True

    def delete_line(self, current_line):
        for i, line in enumerate(self.lines):
            if line is current_line:
                self.lines = self.lines[:i] + self.lines[i + 1:]
                break

    def is_collide(self, spinner):
        for line in self.lines:
            if not line.get_collision():
                return
            for wing in spinner.get_wings():
                if pygame.sprite.spritecollide(wing, line.get_blocks(), False):
                    return True
        return False
