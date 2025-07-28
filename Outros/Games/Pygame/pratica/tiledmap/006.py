import pygame

pygame.init()

width, height = 960, 640
screen = pygame.display.set_mode((width, height))




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True

    pygame.display.update()

pygame.quit()
