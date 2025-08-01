import pygame

pygame.init()

width, height = 960, 640
screen = pygame.display.set_mode((width, height))

class Sprite:
    def __init__(self, file, x, y):
        self.file = file
        self.x = x
        self.y = y
        self.image = pygame.image.load(self.file)

    def get_image(self, sheet, frame, width, height, scale, color):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (scale, scale))
        image.set_colorkey(color)

        return image

cow = Sprite("assets/Animals/cow.png", 10, 10)


animation_list = []
animation_steps = 4
animation_countdown = 125
last_update = pygame.time.get_ticks()
frame = 0

for animation in range(animation_steps):
    animation_list.append(cow.get_image(cow.image, animation, 32, 32, 64, "black"))


x, y = 500, 120


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

    screen.blit(animation_list[frame], (x, y))


    pygame.display.update()

pygame.quit()
