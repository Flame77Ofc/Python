import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Meu Jogo")

speed = 15
x, y = 400, 300

fps = pygame.time.Clock()

running = True
while running:
    fps.tick(60)
    screen.fill("lightblue")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.circle(screen, "red", (x, y), 50)
    pygame.draw.line(screen, "darkgreen", (0, 570), (900, 570), 90)

    if x > 800 or x < 0:
        x = 400
    if y > 600 or y < 0:
        y = 300

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        x -= speed
    if key[pygame.K_RIGHT]:
        x += speed
    if key[pygame.K_UP]:
        y -= speed
    if key[pygame.K_DOWN]:
        y += speed

    pygame.display.update()


pygame.quit()
