import pygame
import sys
from Constants import *

from Sound import *
from Camera import *
from Background import *
from HUD import *
from Map import *
from Spinner import *


def terminate():
    pygame.quit()
    sys.exit()


def new_game():
    global start, lose, camera, background, hud, game_map, spinner
    sound.new_game()
    start = True
    lose = False
    camera = Camera()
    background = Background()
    hud = HUD()
    hud.game_menu(False)
    hud.restart_button.push = new_game
    game_map = Map()
    spinner = Spinner((0, 0))
    update_camera(spinner)


def game_lose():
    global lose
    lose = True
    spinner.lose()
    background.lose()
    sound.lose()


def update_camera(target):
    camera.update(target)
    camera.apply(target)
    for line in game_map.get_lines():
        camera.apply(line)
        for block in line.get_blocks():
            camera.apply(block)
    if spinner.get_is_first_touch():
        for rect in background.get_rectangles():
            rect[1][0] += camera.get_delta()[0] / 1.5
            rect[1][1] += camera.get_delta()[1] / 1.5


def new_line():
    game_map.add_line((spinner.get_coord()[0],
                       spinner.get_coord()[1] - space_between_new_line), spinner.get_color())


pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("luja")
clock = pygame.time.Clock()

start = True
lose = False
sound = Sound()
camera = Camera()
background = Background()
hud = HUD()
hud.start_menu(True)
hud.restart_button.push = new_game
game_map = Map()
spinner = Spinner((0, 0))
update_camera(spinner)

FPS = 150
time = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            push = False
            for button in hud.get_buttons():
                if button.rect.collidepoint(pygame.mouse.get_pos()):
                    button.push()
                    push = True
                    break
            if push: break
            game_map.update_first_touch()
            hud.start_menu(False)
            hud.game_menu(True)
            if not lose:
                sound.jump()
                spinner.add_power()

    spinner.update(FPS)
    game_map.update(FPS)
    background.update(FPS, *spinner.get_wings(), *game_map.get_blocks())
    hud.update(FPS)

    if lose:
        if spinner.get_coord()[1] > 1200:
            hud.game_menu(False)
            hud.lose_menu(True)
    else:
        if game_map.is_collide(spinner):
            game_lose()
            for line in game_map.get_lines():
                line.delete()
        if game_map.get_lines() and \
                spinner.get_coord()[1] > game_map.get_lines()[-1].get_coord()[1] + 900:
            game_lose()
        for line in game_map.get_lines():
            if line.get_is_max():
                game_lose()
                for cur_line in game_map.get_lines(): cur_line.delete()
                break

        update_camera(spinner)
        if len(game_map.get_lines()) == 0:
            new_line()
        if spinner.get_coord()[1] < game_map.get_lines()[-1].get_coord()[
            1] - space_between_lines:
            sound.point()
            background.update_colors()
            spinner.update_setting(game_map.get_lines()[-1].get_color())
            game_map.get_lines()[-1].delete()
            new_line()
            hud.points.add()

    background.draw(screen)
    spinner.draw(screen)
    game_map.draw(screen)
    hud.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
    print(1000 / (pygame.time.get_ticks() - time))
    time = pygame.time.get_ticks()
