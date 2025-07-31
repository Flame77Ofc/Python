import pygame

pygame.init()

width, height = 960, 640
screen = pygame.display.set_mode((width, height))

# Layers
def layers(file, scale_x, scale_y):
    image = pygame.image.load(file)
    image = pygame.transform.scale(image, (scale_x, scale_y))

    return image

background = layers("assets/Background/parallax/forest2/plx-1.png", width, height)
layer1 = layers("assets/Background/parallax/forest2/plx-2.png", width, height)
layer2 = layers("assets/Background/parallax/forest2/plx-4.png", width, height)
layer3 = layers("assets/Background/parallax/forest2/plx-5.png", width, height)
floor = layers("assets/Background/bgs/summer 2/3.png", width, height+100)

backgrounds = [background, layer1, layer2, layer3, floor]
background_width = background.get_width()

def draw_background():
    for x in range(5):
        speed = 1.3
        for i in backgrounds:
            screen.blit(i, ((x * background_width) - scroll * speed, 0))
            speed += 0.2

scroll = 0

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
        scroll -= 15
    if key[pygame.K_RIGHT] and scroll < 1800:
        scroll += 15

    pygame.display.update()

pygame.quit()
