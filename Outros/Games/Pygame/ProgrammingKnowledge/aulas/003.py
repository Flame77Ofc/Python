# AONDE VOCÊ CLICA O MOUSE SEGUE! (APENAS CLIQUE!!!)
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Meu Jogo")

speed = 10
x, y = 400, 300

fps = pygame.time.Clock()


running = True
while running:
    fps.tick(60)
    bg = screen.fill("gray")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # MOUSE
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]

    if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]

    pygame.draw.circle(screen, "red", (x, y), 50)
    pygame.display.update()


pygame.quit()
