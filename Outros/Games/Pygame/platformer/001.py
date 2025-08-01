# Configurando a janela do jogo, definindo o FPS, a cor de fundo e o título do Jogo.
import pygame

pygame.init()

width, height = 960, 640
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Platformer Game")

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
