import pygame

pygame.init()

width, height = 960, 640
screen = pygame.display.set_mode((width, height))

class Sprite:
    def __init__(self, file, x, y, steps, countdown, speed):
        self.file = file
        self.x = x
        self.y = y

        self.image = pygame.image.load(self.file)

        self.animation_list = []
        self.animation_steps = steps
        self.animation_countdown = countdown
        self.last_update = pygame.time.get_ticks()
        self.frame = 0
        self.speed = speed


    def get_image(self, frame, width, height, scale, color, right):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.image, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (scale, scale))
        image.set_colorkey(color)


        return image


    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.y -= self.speed
        if key[pygame.K_LEFT]:
            self.x -= self.speed
        if key[pygame.K_RIGHT]:
            self.x += self.speed


        if self.frame >= self.animation_steps-1:
            self.frame = 0

        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.last_update >= self.animation_countdown:
            self.frame += 1
            self.last_update = self.current_time

        screen.blit(self.animation_list[self.frame], (self.x, self.y))


virtual_guy = Sprite("assets/Characters/Virtual Guy/Idle (32x32).png", 120, 420, 10, 50, 10)
for animation in range(virtual_guy.animation_steps):
    virtual_guy.animation_list.append(virtual_guy.get_image(animation, 32, 32, 64, "black", True))


x, y = 500, 120


fps = pygame.time.Clock()

running = True
while running:
    fps.tick(60)
    screen.fill("grey")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    virtual_guy.update()

    pygame.display.update()

pygame.quit()
