import pygame

pygame.init() # Inicializa o pygame

screen = pygame.display.set_mode((780, 640)) # Mostra o tamanho em largura e altura da janela
title = pygame.display.set_caption("Meu Jogo Em Pygame") # Define o título do jogo

# GAME LOOP
running = True
while running:
    for event in pygame.event.get(): # Itera sobre cada evento do pygame (evento = ação)
        if event.type == pygame.QUIT: # Se o tipo do evento for QUIT, então:
            pygame.quit() # Pare de executar o pygame

    bg = screen.fill((27, 54, 48)) # Define o background para verde
    pygame.display.update() # Atualiza a cada repetição, permitindo animações

pygame.quit()
