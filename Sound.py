import pygame
from os import path
from random import randint


class Sound:
    def __init__(self):
        self.sounds = [pygame.mixer.Sound(path.join("data", "jump.wav")),
                       pygame.mixer.Sound(path.join("data", "pointsup.wav")),
                       pygame.mixer.Sound(path.join("data", "pointsup1.wav")),
                       pygame.mixer.Sound(path.join("data", "pointsup2.wav")),
                       pygame.mixer.Sound(path.join("data", "lose.wav")),
                       pygame.mixer.Sound(path.join("data", "newgame.wav"))
                       ]
        self.last_coin_n = None

    def jump(self):
        self.sounds[0].play()

    def point(self):
        n = randint(1, 3)
        while n == self.last_coin_n:
            n = randint(1, 3)
        self.sounds[n].play()
        self.last_coin_n = n

    def lose(self):
        self.sounds[4].play()

    def new_game(self):
        self.sounds[5].play()
