# renderizando imagens, colisões e inputs
import pygame

pygame.init()

width, height = 960, 640
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Platformer Game")

image = pygame.image.load("assets/HUD/UI/sword.png")
meat = pygame.image.load("assets/Food/Meat.png")
x, y = width / 2, height / 2

image_rect = pygame.Rect(x, y, image.get_width(), image.get_height())

speed = 10
right = True


fps = pygame.time.Clock()

running = True
while running:
    fps.tick(60)
    screen.fill("grey")
    image_rect = pygame.Rect(x, y, image.get_width(), image.get_height())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("Right")

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        right = False
        x -= speed
    if key[pygame.K_RIGHT]:
        right = True
        x += speed

    if right:
        screen.blit(image, (x, y))
    else:
        screen.blit(pygame.transform.flip(image, True, False), (x, y))


    pygame.display.update()

pygame.quit()
