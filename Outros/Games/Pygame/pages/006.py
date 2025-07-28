# Movimentos restritos
import pygame

pygame.init()

window_width = 1000
window_height = 750

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Meu Jogo")

x, y = 500, 350
speed = 8

fps = pygame.time.Clock()

running = True
while running:
    fps.tick(180)
    screen.fill("grey")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    character = pygame.draw.circle(screen, "black", (x, y), 45)

    key = pygame.key.get_pressed()
    if (key[pygame.K_LEFT] or key[pygame.K_a]) and x > 50:
        x -= speed
    if (key[pygame.K_RIGHT] or key[pygame.K_d]) and x < window_width - 50:
        x += speed
    if (key[pygame.K_UP] or key[pygame.K_w]) and y > 50:
        y -= speed
    if (key[pygame.K_DOWN] or key[pygame.K_s]) and y < window_height - 50:
        y += speed

    pygame.display.update()

pygame.quit()
