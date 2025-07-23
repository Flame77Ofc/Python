import pygame

# Mecânica de movimentos: Animando e movendo objetos
pygame.init()

screen = pygame.display.set_mode((750, 590))
title = pygame.display.set_caption("Meu Jogo")

IMG = pygame.image.load("pokemon-pixelart.png")
x = 50
y = 50

def movimentar():
    screen.blit(IMG, (x, y))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    x += 1
    movimentar()

    pygame.display.update()

pygame.quit()
