import pygame
from random import randint

pygame.init()

window_width = 1350
window_height = 750

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Eat The Food and Get Stronger!")

main_x, main_y = window_width / 2, window_height / 2
collision_x, collision_y = randint(100, window_width-100), randint(100, window_height-100)
speed = 10
food = 45

font = pygame.font.SysFont("cambriamath", 40)

fps = pygame.time.Clock()

running = True
while running:
    fps.tick(120)
    bg = screen.fill((56, 67, 175))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and main_x > food:
        main_x -= speed
    if key[pygame.K_RIGHT] and main_x < window_width-food:
        main_x += speed
    if key[pygame.K_UP] and main_y > food:
        main_y -= speed
    if key[pygame.K_DOWN] and main_y < window_height-food:
        main_y += speed


    collision_character = pygame.draw.circle(screen, "orange", (collision_x, collision_y), 45)
    main_character = pygame.draw.circle(screen, "white", (main_x, main_y), food)

    if main_character.colliderect(collision_character):
        food += 5
        collision_x, collision_y = randint(100, window_width-100), randint(100, window_height-100)

    text = font.render(f"Tamanho: {food}", True, "grey")
    screen.blit(text, (15, 5))

    if food >= 1000:
        running = False

    pygame.display.update()

pygame.quit()
