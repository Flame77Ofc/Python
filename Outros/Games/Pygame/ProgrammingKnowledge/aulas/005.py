# Desenhando formas geométricas!
import pygame
from random import randint

pygame.init()

window_width = 800
window_height = 600

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Meu Jogo")

fps = pygame.time.Clock()

running = True
while running:
    fps.tick(60)
    bg = screen.fill((73, 125, 241))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_l: ...

    # Coordenadas
    # Quando vamos para direita, x incrementa, e quando vamos para baixo, y incrementa.

    # Desenhando uma linha
    # screen, color, initial pos., final pos., thickness
    pygame.draw.line(screen, "darkgreen", (0, window_height-50), (window_width, window_height-50), 100)

    # Desenhando um círculo
    # screen, color, coordinates, thickness, 0=fill, 1,...=outline only, draw_top_right, draw_top_left, draw_bottom_left,draw_bottom_right
    pygame.draw.circle(screen, "red", (window_width / 2, window_height / 2), 50, 10, True, True, True, True)

    # Desenhando um retângulo
    # screen, color,  x, y, width, height, 0 value, border-radius
    pygame.draw.rect(screen, "blue", (10, 10, 100, 100), 0)

    pygame.display.update()

pygame.quit()
