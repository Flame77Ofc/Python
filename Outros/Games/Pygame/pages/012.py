import pygame

pygame.init()

width, height = 960, 640
screen = pygame.display.set_mode((width, height))

running = True
while running:
    screen.fill("grey")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Click")

    mouse = pygame.mouse.get_pressed()
    if mouse[0]:
        print(mouse)


    pygame.display.update()

pygame.quit()
