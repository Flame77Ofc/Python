import pygame

pygame.init()

width, height = 960, 640
screen = pygame.display.set_mode((width, height))

sprite_sheet = pygame.image.load("assets/Characters/Ninja Frog/Idle (32x32).png")

def get_image(sheet, frame, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (frame * width, 0, width, height))
    image = pygame.transform.scale(image, (scale, scale))
    image.set_colorkey("black")

    return image


animation_list = []
animation_steps = 11
animation_countdown = 50
last_update = pygame.time.get_ticks()
frame = 0

for animation in range(animation_steps):
    animation_list.append(get_image(sprite_sheet, animation, 32, 32, 128, "black"))


fps = pygame.time.Clock()

running = True
while running:
    fps.tick(60)
    screen.fill("grey")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if frame >= animation_steps-1:
        frame = 0

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_countdown:
        frame += 1
        last_update = current_time

    screen.blit(animation_list[frame], (0, 0))

    pygame.display.update()

pygame.quit()
