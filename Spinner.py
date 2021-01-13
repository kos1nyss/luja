import pygame
from math import sin, cos, radians
from random import choice, randint
from Constants import radius, rotate_speed, G, acceleration, delete_and_create_speed, shadows_color
from Object import *
from Wing import *


class Spinner(Object):
    def __init__(self, coord):
        super().__init__(coord)
        self.direction = choice([-1, 1])
        self.speed_y = 0
        self.acceleration_y = 0
        self.angle = 0
        self.rotate_speed = randint(rotate_speed - 20, rotate_speed + 50)
        self.radius = randint(radius - 10, radius + 20)
        self.wings = [Wing() for _ in range(2)]
        self.first_touch = False
        self.is_lost = False
        self.color = None

    def get_color(self):
        return self.color

    def get_is_first_touch(self):
        return self.first_touch

    def get_wings(self):
        return self.wings

    def update(self, fps):
        self.update_speed(fps)
        self.update_coord(fps)
        self.update_rotate(fps)
        self.update_wings(fps)
        self.update_image()

    def update_speed(self, fps):
        if not self.first_touch:
            return
        self.speed_y -= G / fps
        if not self.is_lost and self.speed_y < -acceleration:
            self.speed_y = -acceleration
        elif self.is_lost and self.speed_y < -delete_and_create_speed:
            self.speed_y = -delete_and_create_speed

    def update_coord(self, fps):
        self.move((0, -self.speed_y / fps))

    def update_rotate(self, fps):
        new_rotate_speed = self.rotate_speed
        delta = 20
        if 90 - delta <= self.angle <= 90 + delta or \
                270 - delta <= self.angle <= 270 + delta:
            new_rotate_speed *= 0.75
        self.angle += new_rotate_speed / fps * self.direction
        self.angle %= 360

    def update_wings(self, fps):
        for wing in self.wings:
            wing.update(fps)

    def update_image(self):
        assert len(self.wings) == 2
        self.wings[0].rect = self.wings[0].image.get_rect(
            center=(self.rect.x + self.radius * cos(radians(self.angle - 90)),
                    self.rect.y + self.radius * sin(radians(self.angle - 90))))

        self.wings[1].rect = self.wings[1].image.get_rect(
            center=(self.rect.x + self.radius * cos(radians(self.angle + 90)),
                    self.rect.y + self.radius * sin(radians(self.angle + 90))))

    def update_setting(self, color):
        self.color = color
        self.direction = choice([-1, 1])
        self.rotate_speed = randint(rotate_speed - 20, rotate_speed + 50)
        self.radius = randint(radius - 10, radius + 20)
        for wing in self.wings:
            wing.update_image(color)

    def add_power(self):
        self.speed_y = acceleration
        if not self.first_touch:
            self.first_touch = True

    def draw(self, surface):
        pygame.draw.circle(surface, shadows_color, (self.rect.x, self.rect.y), 3)
        for wing in self.wings:
            wing.draw(surface)

    def lose(self):
        self.is_lost = True
        self.speed_y = -delete_and_create_speed / 2
