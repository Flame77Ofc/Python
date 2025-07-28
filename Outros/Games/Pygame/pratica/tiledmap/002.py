import pygame

pygame.init()

width, height = 320, 160
screen = pygame.display.set_mode((width, height))

dirt = pygame.image.load("assets/tiles/dirt.png")
grass = pygame.image.load("assets/tiles/grass.png")
water = pygame.image.load("assets/tiles/water.png")

tile_size = 32

dirt = pygame.transform.scale(dirt, (tile_size, tile_size))
grass = pygame.transform.scale(grass, (tile_size, tile_size))
water = pygame.transform.scale(water, (tile_size, tile_size))

tiled_map = [
    [0, 0, 2, 2, 2, 2, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 3, 3, 3, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

blocks = [None, dirt, grass, water]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for row_index, row in enumerate(tiled_map):
        for col_index, tile in enumerate(row):
            if tile != 0:
                tile_x = row_index * tile_size
                tile_y = col_index * tile_size
                screen.blit(blocks[tile], (tile_x, tile_y))

    pygame.display.update()

pygame.quit()
