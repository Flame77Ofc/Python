import pygame
import spritesheet_class008

pygame.init()

window_width, window_height = 960, 640
screen = pygame.display.set_mode((window_width, window_height))

sprite = pygame.image.load("assets/sprites/doux.png").convert_alpha()
sprite_sheet = spritesheet_class008.SpriteSheet(sprite)

animation_list = []
animation_steps = 24
last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame = 18

for i in range(animation_steps):
    animation_list.append(sprite_sheet.get_image(i, 24, 24, 64, "black"))


fps = pygame.time.Clock()

running = True
while running:
    fps.tick(60)
    screen.fill("grey")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if frame >= animation_steps-1:
        frame = 18

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time

    screen.blit(animation_list[frame], (0, 0))

    pygame.display.update()

pygame.quit()
