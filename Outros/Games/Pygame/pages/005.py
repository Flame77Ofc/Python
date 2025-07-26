import pygame

pygame.init()

screen = pygame.display.set_mode((780, 650))
title = pygame.display.set_caption("Meu Jogo")
img_icon = pygame.image.load("ghost-fly-sdds-icon.png")
icon = pygame.display.set_icon(img_icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.display.update()

pygame.quit()
