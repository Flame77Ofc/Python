import pygame
from time import sleep

pygame.init()

screen = pygame.display.set_mode((840, 650))
title = pygame.display.set_caption("Ghost Fly")

IMGicon = pygame.image.load("assets/pixelart-ghost.png")
icon = pygame.display.set_icon(IMGicon)

IMGcharacter = pygame.image.load("assets/pixelart-ghost.png")
x, y = 50, 200
speed = 8

retangulo = pygame.Rect(0, 600, 840, 50)

fps = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

running = True
while running:
    fps.tick(120)
    bg = screen.fill((12, 57, 108))

    fps_text = font.render(f"Fps: {int(fps.get_fps())}", True, (12, 12, 12))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        y -= speed
    if key[pygame.K_DOWN]:
        y += speed
    if key[pygame.K_LEFT]:
        x -= speed
    if key[pygame.K_RIGHT]:
        x += speed

    if y <= -450:
        y = 525
        screen.blit(IMGcharacter, (x, y))
    if y >= 600:
        y = -450
        screen.blit(IMGcharacter, (x, y))
    if x <= -335:
        x = 800
        screen.blit(IMGcharacter, (x, y))
    if x >= 850:
        x = -300
        screen.blit(IMGcharacter, (x, y))
    else:
        screen.blit(IMGcharacter, (x, y))

    pygame.draw.rect(screen, (98, 14, 7), retangulo)
    screen.blit(fps_text, (50, 50))
    pygame.display.update()

pygame.quit()
