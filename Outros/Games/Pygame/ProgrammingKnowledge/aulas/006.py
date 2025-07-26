# Adicionando texto
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Meu Jogo")

# Vendo quais fontes temos no pc
fonts = pygame.font.get_fonts()
# print(fonts) # ['arial', 'cambriamath', 'consolas', 'cascadiamono'], ...

# Definindo as fontes

font = pygame.font.SysFont("consolas", 45, True, True)
texto = font.render("My Game", True, "black")

fps = pygame.time.Clock()

running = True
while running:
    fps.tick(60)
    bg = screen.fill("grey")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(texto, (295, 95))
    pygame.display.update()

pygame.quit()
