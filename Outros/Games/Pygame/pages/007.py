# Colisões
import pygame

pygame.init()

window_width, window_height = 800, 600
screen = pygame.display.set_mode((window_width, window_height))

x, y = 125, 300
x_colision, y_colision = 400, 300
speed = 10

font = pygame.font.SysFont("calibriamath", 45)
text = font.render("You Touch in The Cube!", True, "white")

fps = pygame.time.Clock()

running = True
while running:
    fps.tick(60)
    bg = screen.fill("lightskyblue")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and x > 50:
        x -= speed
    if key[pygame.K_RIGHT] and x < window_width-50:
        x += speed
    if key[pygame.K_UP] and y > 50:
        y -= speed
    if key[pygame.K_DOWN] and y < window_height-50:
        y += speed

    character = pygame.draw.circle(screen, "orange", (x, y), 45)
    object_collision = pygame.draw.rect(screen, "red", (x_colision, y_colision, 25, 25))

    if character.colliderect(object_collision):
        screen.blit(text, (50, 50))

    pygame.display.update()

pygame.quit()
