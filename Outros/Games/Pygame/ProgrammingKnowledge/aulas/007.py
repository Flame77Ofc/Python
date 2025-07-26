# Adicionando som
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Meu Jogo")

fps = pygame.time.Clock()

# Carregando o som
sound = pygame.mixer.Sound("aulas/game-music-external.mp3")
sound.set_volume(5)
sound.play(-1)

# sound2 = pygame.mixer.Sound("aulas/game-start-external.mp3")
# sound2.play(1, 0)

running = True
while running:
    fps.tick(60)
    bg = screen.fill("darkgreen")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()