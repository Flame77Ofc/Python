import pygame

pygame.init()

screen = pygame.display.set_mode((740, 408))
pygame.display.set_caption("Meu Jogo")

IMGicon = pygame.image.load("aulas/pacman.png")
pygame.display.set_icon(IMGicon)

fps = pygame.time.Clock()
character = pygame.image.load("aulas/pacman-main-character.png")

bg_image = pygame.image.load("aulas/background-image-pixelart.png").convert()


running = True
while running:
    fps.tick(60)
    screen.blit(bg_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(character, (10, 10))

    pygame.display.update()

pygame.quit()
