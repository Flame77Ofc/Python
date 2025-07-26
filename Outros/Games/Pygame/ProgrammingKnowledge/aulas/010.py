import pygame

pygame.init()

window_width, window_height = 1350, 750
screen = pygame.display.set_mode((window_width, window_height))

fps = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()


pygame.quit()