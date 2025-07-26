import pygame
from random import randint
import json
from datetime import datetime

pygame.init()

window_width, window_height = 1350, 750
screen = pygame.display.set_mode((window_width, window_height))

x, y = window_width / 2, window_height / 2
rand_x, rand_y = randint(50, window_width-50), 0

character_speed = 10
ball_speed = 8

font = pygame.font.SysFont("consolas", 45, True)
fps = pygame.time.Clock()

times = 1
stage = 1
lifes = 3

already_collided = False
ball_moduled_by_ten = False

running = True
while running:
    fps.tick(60)

    screen.fill("grey")

    text = font.render(f"Pontos: {times}", True, "black")
    screen.blit(text, (15, 5))

    text = font.render(f"Vidas: {lifes}", True, "darkgreen")
    screen.blit(text, (1000, 50))

    text = font.render(f"Estágio: {stage}", True, "black")
    screen.blit(text, (15, 75))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and x > 50:
        x -= character_speed
    if key[pygame.K_RIGHT] and x < window_width-50:
        x += character_speed
    if key[pygame.K_UP] and y > 50:
        y -= character_speed
    if key[pygame.K_DOWN] and y < window_height-50:
        y += character_speed
    if key[pygame.K_SPACE]:
        character_speed += 100
        character_speed -= 10

    character = pygame.draw.circle(screen, "orange", (x, y), 45)
    obj = pygame.draw.circle(screen, "red", (rand_x, rand_y), 10)

    if character.colliderect(obj):
        if not already_collided:
            lifes -= 1
            already_collided = True
    else:
        already_collided = False
        if lifes < 1:
            agora = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

            try:
                with open("data.json", "r") as f: data = json.load(f)
                data[agora] = times
                with open("data.json", "w") as f: json.dump(data, f, indent=4)
            except:
                data = {agora: times}
                with open("data.json", "w") as f:json.dump(data, f, indent=4)
            running = False

    rand_y += ball_speed

    if rand_y > window_height:
        times += 1
        rand_x, rand_y = randint(50, window_width-50), 0

    if times % 10 == 0:
        ball_speed += 0.1
        character_speed += 0.02
        if not ball_moduled_by_ten:
            stage += 1
            ball_moduled_by_ten = True
    else:
        ball_speed += 0.0001
        ball_moduled_by_ten = False

    pygame.display.update()

pygame.quit()
