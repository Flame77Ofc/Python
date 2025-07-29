import pygame

pygame.init()

window_width, window_height = 960, 640
screen = pygame.display.set_mode((window_width, window_height))

# Primeiro passo
sprite_sheet = pygame.image.load("assets/Characters/vita.png")

# Segundo passo
def get_image(sheet, frame, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (frame * width, 0, width, height))
    image = pygame.transform.scale(image, (scale, scale))
    image.set_colorkey(color)

    return image

# Terceiro passo
animation_list = []
animation_steps = 10
animation_countdown = 90
last_update = pygame.time.get_ticks()
frame = 4

# Quarto passo
for animation in range(animation_steps):
    animation_list.append(get_image(sprite_sheet, animation, 24, 24, 64, "black"))

fps = pygame.time.Clock()

running = True
while running:
    fps.tick(60)
    screen.fill("gray")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Quinto passo
    if frame >= animation_steps-1:
        frame = 4

    # Sexto passo
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_countdown:
        frame += 1
        last_update = current_time

    screen.blit(animation_list[frame], (0, 0))

    pygame.display.update()

pygame.quit()
