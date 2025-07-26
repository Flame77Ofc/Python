import pygame

# Colocando imagens na tela
pygame.init()


screen = pygame.display.set_mode((850, 740))
title = pygame.display.set_caption("Colocando Imagens na janela")

playerIMG = pygame.image.load("player-pixelart.png")
playerX = 200
playerY = 200


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(playerIMG, (playerX, playerY))
    pygame.display.update()

pygame.quit()
