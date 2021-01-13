from Constants import WIDTH, HEIGHT, left, top


class Camera:
    def __init__(self):
        self.dx = self.dy = 0
        self.left, self.top = left, top

    def get_delta(self):
        return self.dx, self.dy

    def update(self, target):
        self.dx = WIDTH // 2 - target.rect.x - target.rect.w // 2 + self.left
        self.dy = HEIGHT // 2 - target.rect.y - target.rect.h // 2 + self.top

    def apply(self, sprite):
        sprite.rect.x += self.dx
        sprite.rect.y += self.dy
