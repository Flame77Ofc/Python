# des001: Mude a cor do fundo para roxo, sabendo que: RGB = (156, 0, 203)
import pygame

pygame.init()

screen = pygame.display.set_mode((750, 690))
title = pygame.display.set_caption("Cor de Fundo Roxo")

RGB = (156, 0, 203)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    screen.fill(RGB)
    pygame.display.update()

pygame.quit()