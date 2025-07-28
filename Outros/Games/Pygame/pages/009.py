import pygame

pygame.init()

width, height = 1280, 750
screen = pygame.display.set_mode((width, height))

# class Character:
#     def __init__(self, x, y)

character = pygame.image.load("")

x, y = width / 2, height / 2
speed = 10

fps = pygame.time.Clock()

running = True
while running:
    fps.tick(60)
    screen.fill("lightblue")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and x > 50:
        x -= speed
    if key[pygame.K_RIGHT] and x < width-50:
        x += speed
    if key[pygame.K_UP] and y > 50:
        y -= speed
    if key[pygame.K_DOWN] and y < height-50:
        y += speed

    character = pygame.draw.circle(screen, "orange", (x, y), 45)

    pygame.display.update()

pygame.quit()
