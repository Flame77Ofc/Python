import pygame

pygame.init()

width, height = 960, 640
screen = pygame.display.set_mode((width, height))

sword = pygame.image.load("assets/Weapons/Sword2/Sprite.png")
sword = pygame.transform.scale(sword, (24, 60))
sword = pygame.transform.flip(sword, True, False)
sword = pygame.transform.rotate(sword, 25)

meat = pygame.image.load("assets/Food/Meat.png")
meat = pygame.transform.scale(meat, (40, 40))
rotate_value = 0

meat_x, meat_y = 450, 690

pygame.mouse.set_visible(False)

jump = False
GRAVITY = 0.3
VELOCITY = 9
JUMP_HEIGHT = VELOCITY


fps = pygame.time.Clock()

running = True
while running:
    fps.tick(60)
    screen.fill("grey")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                jump = True


    mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
    screen.blit(sword, (mouse_x, mouse_y))

    if jump:
        rotate_value += 7
        screen.blit(pygame.transform.rotate(meat, rotate_value), (meat_x, meat_y))
        meat_x -= VELOCITY * 0.5
        meat_y -= VELOCITY * 0.6
        meat_y -= 9.8


    else:
        screen.blit(meat, (meat_x, meat_y))

    pygame.display.update()

pygame.quit()
