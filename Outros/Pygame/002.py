import pygame

pygame.init()
screen = pygame.display.set_mode((800, 640))

title = pygame.display.set_caption("Meu Jogo")
clock = pygame.time.Clock()



running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((35, 54, 55))

    pygame.display.update()
