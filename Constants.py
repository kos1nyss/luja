import pygame

# - Экран
SIZE = WIDTH, HEIGHT = 1024, 1024  # Размеры экрана

# - Стороны
CENTER = "center"
LEFT = "left"
RIGHT = "right"

# - Камера
left = 0
top = 200

# - Спиннер
radius = 150  # Радиус вращения
rotate_speed = 90  # Скорость вращения
acceleration = 600  # Ускорение при толчке
G = 9.81 * 80  # Ускорение свободного падения

# - Крыло
wing_size = 75, 75

# - Карта
line_width = 75
space_between_lines = 230  # Расстояние между линиями
space_between_new_line = 650  # Расстояние перед новой линией
space_between_display_and_block = 20  # Расстояние между блоками и экраном
delete_and_create_speed = 1200  # Скорость появления и удаления блоков
block_grow_speed = 20  # Скорость увеличения блоков
colors = [pygame.Color("#01c5c4"),
          pygame.Color("#b8de6f"),
          pygame.Color("#b691ff"),
          pygame.Color("#fff38c"),
          pygame.Color("#f4a490"),
          ]

# - Задний фон
bg_rect_size = 256
bg_color = pygame.Color("#410F70")
shadows_color = pygame.Color("#220B4E")

# - Кнопка
button_color = pygame.Color("#6e236f")
button_color_text = pygame.Color("#d43b9b")
button_grow_speed = 2000
button_anim_speed = 15

# -  Текст
text_color = pygame.Color(255, 255, 255)
