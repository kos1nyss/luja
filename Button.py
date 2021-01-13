import pygame
from os import path
from ObjectWithSprite import ObjectWithSprite
from Constants import button_color, button_color_text, button_grow_speed, shadows_color, \
    button_anim_speed


class Button(ObjectWithSprite):
    def __init__(self, coord, size, text):
        self.font = pygame.font.Font(path.join("data", "kongtext.ttf"), 45)
        super().__init__()
        self.cur_size = [size[0] - 35,
                         size[1] - 35]
        self.size = size
        self.coord = list(coord)
        self.target_coords = [(self.coord[0], self.coord[1] - 30),
                              (self.coord[0], self.coord[1] + 10)]
        self.target = 0
        self.text = text

        self.create_image(button_color)

    def update(self, fps):
        if self.cur_size[0] < self.size[0]:
            self.cur_size[0] += button_grow_speed / fps
        if self.cur_size[1] < self.size[1]:
            self.cur_size[1] += button_grow_speed / fps

        if self.cur_size[0] >= self.size[0] and self.cur_size[1] >= self.size[1]:
            if self.target == 0:
                self.coord[1] -= button_anim_speed / fps
                if self.coord[1] <= self.target_coords[0][1]:
                    self.target = 1
            elif self.target == 1:
                self.coord[1] += button_anim_speed / fps
                if self.coord[1] > self.target_coords[1][1]:
                    self.target = 0

        if self.coord[0] - self.size[0] // 2 <= pygame.mouse.get_pos()[0] <= self.coord[0] + \
                self.size[0] // 2 and \
                self.coord[1] - self.size[1] // 2 <= pygame.mouse.get_pos()[1] <= self.coord[1] + \
                self.size[1] // 2:
            color = pygame.Color(button_color)
            color.hsva = color.hsva[0], color.hsva[1], \
                         max(color.hsva[2] - 3, 0)
        else:
            color = pygame.Color(button_color)

        self.create_image(color)

    def create_image(self, color):
        self.image = pygame.Surface(self.cur_size)
        self.rect = self.image.get_rect(center=self.coord)
        background_color = pygame.Color(color)
        outline_color = pygame.Color(background_color)
        outline_color.hsva = outline_color.hsva[0], outline_color.hsva[1], \
                             max(outline_color.hsva[2] - 10, 0)
        self.image.fill(background_color)
        pygame.draw.rect(self.image, outline_color, (0, 0, *self.cur_size), 10)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        pygame.draw.rect(surface, shadows_color,
                         (self.coord[0] - self.size[0] / 2, self.coord[1] + 65,
                          self.size[0], 20))
        if self.cur_size[0] >= self.size[0] and self.cur_size[1] >= self.size[1]:
            text = self.font.render(self.text, False, button_color_text)
            place = text.get_rect(center=self.coord)
            surface.blit(text, place)
