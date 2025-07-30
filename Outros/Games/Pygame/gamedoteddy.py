import pygame
from random import randint

pygame.init()

window_width, window_height = 960, 640
screen = pygame.display.set_mode((window_width, window_height))

background_image = pygame.image.load("assets/Background/blue_blackground.png")
background_image = pygame.transform.scale(background_image, (window_width, window_height))

def get_image(sheet, frame, width, height, scale, color):
    character = pygame.image.load(sheet)
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(character, (0, 0), (frame*width, 0, width, height))
    image = pygame.transform.scale(image, (scale, scale))
    image.set_colorkey(color)

    return image

def caracter(final_steps, initial_frame, img):
    animation_list = []
    animation_steps = final_steps
    animation_countdown = 50
    last_update = pygame.time.get_ticks()
    frame = initial_frame

    lista = [animation_list, animation_steps, animation_countdown, last_update, frame, [animation_list.append(get_image(img, animation, 32, 32, 64, "black")) for animation in range(animation_steps)]]
    return lista

character = caracter(11, 0, "assets/Characters/Virtual Guy/Idle (32x32).png")
animation_list = character[0]
animation_steps = character[1]
animation_countdown = character[2]
last_update = character[3]
frame = character[4]


jumping = False
GRAVITY = 1
VELOCITY = 15
JUMP_HEIGHT = VELOCITY

x, y = 45, 545
initial_y = y
speed = 10

grass = pygame.image.load("assets/tilesets/grass.png")
tile_size = 32
grass = pygame.transform.scale(grass, (tile_size, tile_size))

tiled_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

blocks = [None, grass]

lucky_block = pygame.image.load("assets/Items/lucky-block.png")
lucky_block = pygame.transform.scale(lucky_block, (32, 32))
block_x, block_y = randint(50, 910), 450
false_block_y = block_y + 8


tocou = False
pontos = 0
font = pygame.font.SysFont("mono", 45, True)

fps = pygame.time.Clock()

running = True
while running:
    fps.tick(60)
    screen.fill("grey")
    screen.blit(background_image, (0, 0))

    text = font.render(f"Pontos: {pontos}", True, "black")
    screen.blit(text, (35, 70))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(lucky_block, (block_x, block_y))

    if (x >= block_x-50 and x <= block_x+50) and (y <= false_block_y):
        tocou = True

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and x > 10:
        character = caracter(11, 0, "assets/Characters/Virtual Guy/Idle - left(32x32).png")
        animation_list = character[0]
        animation_steps = character[1]
        animation_countdown = character[2]
        last_update = character[3]
        frame = character[4]

        x -= speed
    if key[pygame.K_RIGHT] and x < window_width-74:
        character = caracter(11, 0, "assets/Characters/Virtual Guy/Idle (32x32).png")
        animation_list = character[0]
        animation_steps = character[1]
        animation_countdown = character[2]
        last_update = character[3]
        frame = character[4]

        x += speed
    if key[pygame.K_UP]:
        jumping = True

    if frame >= animation_steps-1:
        frame = 0

    current_time = pygame.time.get_ticks()

    if not jumping:
        if current_time - last_update >= animation_countdown:
            frame += 1
            last_update = current_time

        screen.blit(animation_list[frame], (x, y))

    else:
        screen.blit(animation_list[frame], (x, y))

        y -= VELOCITY
        VELOCITY -= GRAVITY

        if VELOCITY < -JUMP_HEIGHT:
            jumping = False
            VELOCITY = JUMP_HEIGHT

    for row_index, row in enumerate(tiled_map):
        for col_index, tile in enumerate(row):
            if tile != 0:
                tile_x = col_index * tile_size
                tile_y = row_index * tile_size
                screen.blit(blocks[tile], (tile_x, tile_y))

    if tocou:
        pygame.display.update()
        pontos += 1
        block_x = randint(50, 910)
        tocou = False

    pygame.display.update()

pygame.quit()
