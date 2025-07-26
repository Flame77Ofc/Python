import pygame
import pygame.display

# Capturando teclas do teclado
pygame.init()

screen = pygame.display.set_mode((850, 650))
title = pygame.display.set_caption("Capturando Teclas Do Teclado")
IMG = pygame.image.load("aulas/simple-ball-pixelart.png")
x = 1
y = 2
speed = 5

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)
    bg = screen.fill((27, 55, 42)) # Lembre-se: SEMPRE PRIMEIRO VEM O BACKGROUND, E DEPOIS A IMAGEM!!!

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        x += speed
    if key[pygame.K_LEFT]:
        x -= speed
    if key[pygame.K_DOWN]:
        y += speed
    if key[pygame.K_UP]:
        y -= speed

    screen.blit(IMG, (x, y))

    pygame.display.update()

pygame.quit()
