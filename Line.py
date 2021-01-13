import pygame
from random import choice, randint
from Constants import WIDTH, HEIGHT, line_width, delete_and_create_speed, \
    space_between_display_and_block, CENTER, LEFT, RIGHT, block_grow_speed, colors
from Object import *
from Block import *


class Line(Object):
    def __init__(self, parent, coord, player_color):
        super().__init__((coord[0], coord[1] - 200))
        self.collision = True
        self.parent = parent
        self.target_coord = coord
        self.width = line_width
        self.blocks = pygame.sprite.Group()
        self.is_created = True
        self.is_deleted = False
        self.is_growing = False
        self.is_max = False
        self.s = None
        self.colors = colors
        self.color = choice(self.colors)
        while self.color == player_color:
            self.color = choice(self.colors)
        self.speed = randint(block_grow_speed - 10, block_grow_speed + 20)
        self.create()

    def get_is_max(self):
        return self.is_max

    def get_blocks(self):
        return self.blocks

    def get_collision(self):
        return self.collision

    def get_color(self):
        return self.color

    def create(self):
        width = randint(200, 210)
        self.add_block((space_between_display_and_block
                        - HEIGHT // 2 + width // 2, 0), (width, line_width), self.color, LEFT,
                       self.speed)
        self.add_block((-space_between_display_and_block
                        + HEIGHT // 2 - width // 2, 0), (width, line_width), self.color, RIGHT,
                       self.speed)
        width_center = randint(50, 65)
        self.add_block((0, 0), (width_center, line_width), self.color, CENTER, self.speed)
        self.s = HEIGHT // 2 - space_between_display_and_block - width - width_center / 2

    def add_block(self, coord, size, color, side, speed):
        coord = list(coord)
        coord[0] += self.rect.x
        coord[1] += self.rect.y
        new_block = Block(coord, size, color, side, speed)
        self.blocks.add(new_block)

    def delete(self):
        self.is_deleted = True

    def update(self, fps):
        if self.is_created:
            self.update_create_animation(fps)
        elif self.is_deleted:
            self.update_delete_animation(fps)
        elif self.is_growing and not self.is_max and self.parent.get_first_touch():
            self.update_growing_animation(fps)

    def update_delete_animation(self, fps):
        self.move((0, delete_and_create_speed / fps))
        if self.get_coord()[1] > HEIGHT + line_width:
            self.parent.delete_line(self)
            self.collision = False

    def update_create_animation(self, fps):
        self.move((0, delete_and_create_speed / fps))
        if self.get_coord()[1] >= self.target_coord[1]:
            self.set_coord(self.target_coord)
            self.is_created = False
            self.is_growing = True

    def update_growing_animation(self, fps):
        for block in self.blocks:
            block.grow(fps)
            self.s -= self.speed / fps / 2
        if self.s <= -5:
            self.is_max = True

    def move(self, delta):
        super().move(delta)
        for block in self.get_blocks():
            block.move(delta)
