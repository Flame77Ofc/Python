import pygame

pygame.init()

# Colocando a resolução certa que se encaixa com o tamanho dos tiles.
window_width, window_height = 320, 160
screen = pygame.display.set_mode((window_width, window_height))

# Carregando a imagem dos tiles
dirt = pygame.image.load("assets/tiles/dirt.png")
grass = pygame.image.load("assets/tiles/grass.png")
water = pygame.image.load("assets/tiles/water.png")

# Definindo o tamanho do tile
tile_size = 32

# Agora transformamos as imagens dos tiles em escalas/resoluções reais
#                             tile,    width,    height
dirt = pygame.transform.scale(dirt, (tile_size, tile_size))
grass = pygame.transform.scale(grass, (tile_size, tile_size))
water = pygame.transform.scale(water, (tile_size, tile_size))

# Definimos nosso tiled_map.
tiled_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [2, 2, 2, 2, 2, 3, 0, 0, 2, 2],
             [1, 1, 1, 1, 1, 1, 3, 3, 1, 1]]

# Agora definimos os blocos que usaremos dentro de uma lista.
blocks = [None, dirt, grass, water]


# Game Loop
running = True
while running:
    screen.fill("lightskyblue")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for row_index, row in enumerate(tiled_map):
        for col_index, tile in enumerate(row):
            if tile != 0:
                tile_x = col_index * tile_size
                tile_y = row_index * tile_size
                screen.blit(blocks[tile], (tile_x, tile_y))

    pygame.display.update()

pygame.quit()
