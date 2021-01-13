import pygame
from Button import Button
from Text import Text
from Points import Points
from Constants import WIDTH, HEIGHT


class HUD:
    def __init__(self):
        self.is_start_menu = False
        self.is_game_menu = False
        self.is_lose_menu = False

        self.restart_button = Button((WIDTH // 2,
                                      HEIGHT // 2),
                                     (340, 100), "RESTART")
        self.start_text = Text("PRESS ANY KEY", 35, (WIDTH // 2,
                                                     HEIGHT // 2 - 100))

        self.points = Points(85, (WIDTH // 2,
                                  HEIGHT // 2 - 300))

    def update(self, fps):
        if self.is_lose_menu:
            self.update_lose_menu(fps)

    def update_lose_menu(self, fps):
        self.restart_button.update(fps)

    def start_menu(self, a):
        self.is_start_menu = a

    def game_menu(self, a):
        self.is_game_menu = a

    def lose_menu(self, a):
        self.is_lose_menu = a

    def draw(self, surface):
        if self.is_start_menu:
            self.start_text.draw(surface)
        if self.is_game_menu:
            self.points.draw(surface)
        if self.is_lose_menu:
            self.restart_button.draw(surface)

    def get_buttons(self):
        if self.is_lose_menu:
            return [self.restart_button]
        return []
