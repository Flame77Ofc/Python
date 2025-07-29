import pygame

pygame.init()

window_width, window_height = 960, 640
screen = pygame.display.set_mode((window_width, window_height))

sprite_sheet = pygame.image.load("assets/sprites/doux.png").convert_alpha()

def get_image(sheet, frame, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (frame * width, 0, width, height))
    image = pygame.transform.scale(image, (scale, scale))
    image.set_colorkey(color)

    return image

animation_list = []
animation_steps = 24
last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame = 18

# Montar a lista de frames
for i in range(animation_steps):
    animation_list.append(get_image(sprite_sheet, i, 24, 24, 64, "black"))

x, y = window_width / 2, window_height / 2
speed = 10

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    screen.fill("grey")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Animação
    if frame >= animation_steps - 1:
        frame = 18

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time

    screen.blit(animation_list[frame], (x, y))
    pygame.display.update()

pygame.quit()
