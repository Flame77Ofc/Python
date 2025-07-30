import pygame

pygame.init()

width, height = 960, 640
screen = pygame.display.set_mode((width, height))

character_idle = pygame.image.load("assets/Characters/marioidle.png")
character_jump = pygame.image.load("assets/Characters/mario-jumping.png")

scale = 128

character_idle = pygame.transform.scale(character_idle, (scale, scale))
character_jump = pygame.transform.scale(character_jump, (scale, scale))

jumping = False

GRAVITY = 1
VELOCITY = 15
JUMP_HEIGHT = VELOCITY

x, y = 50, 520
initial_y = y

fps = pygame.time.Clock()

running = True
while running:
    fps.tick(60)
    screen.fill("grey")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_UP] or key[pygame.K_SPACE]:
        jumping = True

    print(JUMP_HEIGHT)

    if jumping:
        screen.blit(character_jump, (x, y))

        y -= VELOCITY
        VELOCITY -= GRAVITY

        if VELOCITY < -JUMP_HEIGHT:
            jumping = False
            VELOCITY = JUMP_HEIGHT
    else:
        y = initial_y
        screen.blit(character_idle, (x, y))

    pygame.display.update()

pygame.quit()
