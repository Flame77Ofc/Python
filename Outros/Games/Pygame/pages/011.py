# Key boards
import pygame

pygame.init()

width, height = 960, 640
screen = pygame.display.set_mode((width, height))

fps = pygame.time.Clock()

game_running = True
while game_running:
    fps.tick(60)
    screen.fill("grey")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space")

    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        print("Character is in right")

    pygame.display.update()

pygame.quit()
