import pygame

pygame.init()
screen = pygame.display.set_mode((850, 670))
title = pygame.display.set_caption("Meu Jogo")

IMGicon = pygame.image.load("aulas/player-pixelart.png")
icon = pygame.display.set_icon(IMGicon)

IMGcharacter = pygame.image.load("aulas/pokemon-pixelart.png")
Xcharacter, Ycharacter = 200, 400


fps = pygame.time.Clock()

running = True
while running:
    fps.tick(60)

    screen.fill((98, 54, 189))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(IMGcharacter, (Xcharacter, Ycharacter))
    pygame.display.update()


pygame.quit()
