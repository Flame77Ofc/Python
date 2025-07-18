import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
title = pygame.display.set_caption("Meu Game em Pygame")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 37))
    pygame.display.update()

pygame.quit()