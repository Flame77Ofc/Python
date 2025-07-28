import pygame
import time

pygame.init()

width, height = 1280, 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Scape To The Stalker!")

main_x, main_y = width / 2, height / 2
main_speed = 20

stalker_x, stalker_y = 0, 0
stalker_speed = 3.5

fps = pygame.time.Clock()

start = time.time()

running = True
while running:
    fps.tick(60)
    screen.fill("grey")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and main_x > 50:
        main_x -= main_speed
    if key[pygame.K_RIGHT] and main_x < width-50:
        main_x += main_speed
    if key[pygame.K_UP] and main_y > 50:
        main_y -= main_speed
    if key[pygame.K_DOWN] and main_y < height-50:
        main_y += main_speed

    stalker_character = pygame.draw.rect(screen, "red", (stalker_x, stalker_y, 50, 50))
    main_character = pygame.draw.circle(screen, "orange", (main_x, main_y), 15)

    if stalker_x < main_x:
        stalker_x += stalker_speed
    if stalker_x > main_x:
        stalker_x -= stalker_speed
    if stalker_y < main_y:
        stalker_y += stalker_speed
    if stalker_y > main_y:
        stalker_y -= stalker_speed

    duration = time.time() - start
    font = pygame.font.SysFont("calibriamath", 50)
    duration_text = font.render(f"Tempo: {round(duration)}", True, "black")
    screen.blit(duration_text, (50, 25))

    if stalker_character.colliderect(main_character):
        font = pygame.font.SysFont("chiller", 120)
        game_over_text = font.render("Game Over!", True, "red")
        screen.blit(game_over_text, ((width / 2)-200, (height / 2)-139))

        pygame.display.update()
        pygame.time.delay(100)
        running = False

    if duration < 30:
        stalker_speed += 0.005

    pygame.display.update()

pygame.quit()
