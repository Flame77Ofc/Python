import pygame
from random import randint

pygame.init()

width, height = 960, 640
screen = pygame.display.set_mode((width, height))

class Square(pygame.sprite.Sprite):
    def __init__(self, color: str, width: int, height: int, x: int, y: int):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

square_group = pygame.sprite.Group()
square = Square("orange", 50, 50, 150, 340)
square_group.add(square)

running = True
while running:
    screen.fill("grey")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    square_group.draw(screen)
    pygame.display.update()

pygame.quit()
