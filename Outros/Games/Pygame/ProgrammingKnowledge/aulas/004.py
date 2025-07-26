import pygame
from random import randint

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Meu Jogo")

x, y = 400, 300
speed = 10

fps = pygame.time.Clock()

running = True
while running:
    fps.tick(60)
    bg = screen.fill("gray")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # MOUSE MOTION!!!
    if event.type == pygame.MOUSEMOTION:
        pos = pygame.mouse.get_pos()
        x, y = pos[0], pos[1]

    character = pygame.draw.circle(screen, "red", (x, y), 50)
    pygame.display.update()

pygame.quit()
