import pygame

pygame.init()

width, height = 800, 640
side_margin = 300
lower_margin = 100
screen_size = (width + side_margin, height + lower_margin)
screen = pygame.display.set_mode(screen_size)

# game variables
scroll = 0
scroll_speed = 1

# Backgrounds
def load_backgrounds(file):
    image = pygame.image.load(file).convert_alpha()
    image = pygame.transform.scale(image, (screen_size))

    return image

sky = load_backgrounds("assets/Background/bgs/summer 5/1.png")
mountain = load_backgrounds("assets/Background/bgs/summer 5/2.png")
floor = load_backgrounds("assets/Background/bgs/summer 5/3.png")

backgrounds = [sky, mountain, floor]

def draw_background():
    width = sky.get_width()
    for x in range(5):
        screen.blit(sky, ((x * width) - scroll * 0.2, 0))
        screen.blit(mountain, ((x * width) - scroll * 0.6, height - mountain.get_height() + 100))
        screen.blit(floor, ((x * width) - scroll * 0.7, height - floor.get_height() + 100))


fps = pygame.time.Clock()

running = True
while running:
    fps.tick(60)

    draw_background()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and scroll > 0:
        scroll -= 50
    if key[pygame.K_RIGHT] and scroll < 4400:
        scroll += 50


    pygame.display.update()

pygame.quit()
