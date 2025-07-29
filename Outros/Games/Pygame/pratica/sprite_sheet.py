import pygame

pygame.init()

screen = pygame.display.set_mode((960, 640))

# PRIMEIRO PASSO: DEFINIR O SPRITE SHEET


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()