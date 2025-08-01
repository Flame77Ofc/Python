import pygame
import random

pygame.init()

width, height = 960, 640
screen = pygame.display.set_mode((width, height))

class Sprite(pygame.sprite.Sprite):
    def __init__(self, file, x, y):
        super().__init__()

fps = pygame.time.Clock()
running = True

while running:
    fps.tick(60)
    screen.fill("grey")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
