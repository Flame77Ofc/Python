import pygame
from random import randint

pygame.init()

width, height = 960, 640
screen = pygame.display.set_mode((width, height))

class Sprite(pygame.sprite.Sprite):
    def __init__(self, file):
        super().__init__()
        self.file = file
        self.x = randint(0, 960)
        self.y = randint(0, 640)

        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


sprite_group = pygame.sprite.Group()

for i in range(10):
    mario = Sprite("assets/Characters/mario-idle.png")

    sprite_group.add(mario)



fps = pygame.time.Clock()

running = True
while running:
    fps.tick(60)
    screen.fill("lightskyblue")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mario.x = randint(0, 960)

    sprite_group.update()
    sprite_group.draw(screen)


    pygame.display.update()

pygame.quit()
