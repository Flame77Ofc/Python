import pygame

pygame.init()

window_width = 800
window_height = 600

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Meu Jogo")

x1, y1, = 50, 300
x2, y2 = window_width-50, 300
speed = 8

fps = pygame.time.Clock()

running = True
while running:
    fps.tick(60)
    bg = screen.fill("darkblue")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        x1 -= speed
        x2 += speed
    if key[pygame.K_RIGHT]:
        x1 += speed
        x2 -= speed
    if key[pygame.K_UP]:
        y1 -= speed
        y2 += speed
    if key[pygame.K_DOWN]:
        y1 += speed
        y2 -= speed

    character1 = pygame.draw.circle(screen, "blue", (x1, y1), 50)
    character2 = pygame.draw.circle(screen, "blue", (x2, y2), 50)

    pygame.display.update()

pygame.quit()
