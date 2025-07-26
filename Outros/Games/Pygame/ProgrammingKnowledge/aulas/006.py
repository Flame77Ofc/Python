# Adicionando texto
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Meu Jogo")

fps = pygame.time.Clock()

running = True
while running:
    fps.tick(60)
    bg = screen.fill("grey")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
