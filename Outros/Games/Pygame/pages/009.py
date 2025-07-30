# Jumping
import pygame

pygame.init()

width, height = 960, 640
screen = pygame.display.set_mode((width, height))

mario_idle = pygame.image.load("assets/Characters/marioidle.png")
mario_idle = pygame.transform.scale(mario_idle, (128, 128))

mario_jumping = pygame.image.load("assets/Characters/mario-jumping.png")
mario_jumping = pygame.transform.scale(mario_jumping, (128, 128))

x, y = width / 2, height / 2
speed = 10

# JUMPING VARIABLES
jumping = False

GRAVITY_Y = 0.9
JUMP_HEIGHT = 15
VELOCITY_Y = JUMP_HEIGHT

fps = pygame.time.Clock()

running = True
while running:
    fps.tick(60)
    bg = screen.fill("gray")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        x -= speed
    if key[pygame.K_RIGHT]:
        x += speed
    if key[pygame.K_UP]:
        jumping = True


    if jumping:
        screen.blit(mario_jumping, (x, y))

        y -= VELOCITY_Y
        VELOCITY_Y -= GRAVITY_Y
        if VELOCITY_Y < -JUMP_HEIGHT:
            jumping = False
            VELOCITY_Y = JUMP_HEIGHT
    else:
        y = 320
        screen.blit(mario_idle, (x, y))

    pygame.draw.rect(screen, "orange", (0, 448, width, 500), 0)
    pygame.display.update()

pygame.quit()
