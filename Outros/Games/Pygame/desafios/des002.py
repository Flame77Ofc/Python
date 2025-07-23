# Desafio2: Definir um ícone e posicionar uma imagem perto do centro 
import pygame

pygame.init()

screen = pygame.display.set_mode((780, 690))
title = pygame.display.set_caption("Desafio 2")
icon = pygame.display.set_icon(pygame.image.load("desafios/sword-pixelart.png"))
IMG = pygame.image.load("desafios/sword-pixelart.png")
x = 250
y = 225


running = True
while running:
    bg = screen.fill((34, 67, 83))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(IMG, (x, y))
    pygame.display.update()

pygame.quit()
