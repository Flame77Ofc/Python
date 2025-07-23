# Desafio4: Criar uma simples movimentação de direita e esquerda, com um personagem
import pygame

pygame.init()

screen = pygame.display.set_mode((780, 690))
title = pygame.display.set_caption("Movimentação de personagem simples para direita e esquerda")


rightIMG = pygame.image.load("desafios/mario-right.png")
leftIMG = pygame.image.load("desafios/mario-left.png")
x = 40
y = 400
speed = 5

current_img = rightIMG

fonte = pygame.font.SysFont(None, 36)
l = fonte.render("L", True, (76, 45, 178))
texto = fonte.render("Para aumentar a velocidade", True, (255, 255, 255))

clock = pygame.time.Clock()

running = True
while running:
    velocidade = fonte.render(f"Velocidade: {speed}", True, (34, 87, 99))

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                speed += 1

    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        x += speed
        current_img = rightIMG
    if key[pygame.K_LEFT]:
        x -= speed
        current_img = leftIMG

    bg = screen.fill((22, 54, 45))

    screen.blit(current_img, (x, y))
    screen.blit(l, (10, 25))
    screen.blit(texto, (30, 25))
    screen.blit(velocidade, (550, 50))

    pygame.display.flip()

pygame.quit()
