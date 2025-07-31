import pygame
from random import randint

pygame.init()

window_width, window_height = 960, 640
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Hit The Lucky Block!")

game_sound = pygame.mixer.Sound("assets/Sounds/Retro Music - ABMU - ChipWave 01.wav")
game_sound.set_volume(0.7)
game_sound.play(-1)

backgrounds_list = ["assets/Background/bgs/summer8/Summer8.png", "assets/Background/bgs/summer 4/Summer4.png"]
choosen_background = backgrounds_list[randint(0, 1)]
background = pygame.image.load(choosen_background)
background = pygame.transform.scale(background, (window_width, window_height))

tree = pygame.image.load("assets/Object/Trees/2.png")
tree = pygame.transform.scale(tree, (240, 240))

pointer = pygame.image.load("assets/Object/Pointers/2.png")
pointer = pygame.transform.scale(pointer, (38, 38))

bushe1 = pygame.image.load("assets/Object/Bushes/9.png")
bushe1 = pygame.transform.scale(bushe1, (183, 75))

bushe2 = pygame.image.load("assets/Object/Bushes/8.png")
bushe2 = pygame.transform.scale(bushe2, (126, 54))

bushe3 = pygame.image.load("assets/Object/Bushes/8.png")

bushe4 = pygame.image.load("assets/Object/Bushes/8.png")
bushe4 = pygame.transform.scale(bushe4, (125, 65))

def get_image(sheet, frame, width, height, scale, color_key):
    character = pygame.image.load(sheet).convert_alpha()
    image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
    image.blit(character, (0, 0), (frame * width, 0, width, height))
    image = pygame.transform.scale(image, (scale, scale))
    if color_key:
        image.set_colorkey(pygame.Color(color_key))

    return image


def get_effect_image(final_steps, initial_frame, img):
    animation_list = []
    animation_steps = final_steps
    animation_countdown = 100
    last_update = pygame.time.get_ticks()
    frame = initial_frame

    lista = [animation_list, animation_steps, animation_countdown, last_update, frame, [animation_list.append(get_image(img, animation, 7, 7, 16, "black")) for animation in range(animation_steps)]]

    return lista


effect = get_effect_image(7, 0, "assets/Effects/Glint/glint1.png")
animation_list_effect = effect[0]
animation_steps_effect = effect[1]
animation_countdown_effect = effect[2]
last_update_effect = effect[3]
frame_effect = effect[4]


def get_monster_image(final_steps, initial_frame, img):
    animation_list = []
    animation_steps = final_steps
    animation_countdown = 55
    last_update = pygame.time.get_ticks()
    frame = initial_frame

    lista = [animation_list, animation_steps, animation_countdown, last_update, frame, [animation_list.append(get_image(img, animation, 44, 30, 56, "black")) for animation in range(animation_steps)]]

    return lista


monster = get_monster_image(10, 0, "assets/Enemies/Slime/Idle-Run (44x30).png")
animation_list_monster = monster[0]
animation_steps_monster = monster[1]
animation_countdown_monster = monster[2]
last_update_monster = monster[3]
frame_monster = monster[4]

monster_x, monster_y = 900, 553
monster_facing_right = True
monster_speed = 1


def get_character_image(final_steps, initial_frame, img):
    animation_list = []
    animation_steps = final_steps
    animation_countdown = 50
    last_update = pygame.time.get_ticks()
    frame = initial_frame

    lista = [animation_list, animation_steps, animation_countdown, last_update, frame, [animation_list.append(get_image(img, animation, 32, 32, 64, "black")) for animation in range(animation_steps)]]

    return lista


character = get_character_image(11, 0, "assets/Characters/Virtual Guy/Idle (32x32).png")
animation_list = character[0]
animation_steps = character[1]
animation_countdown = character[2]
last_update = character[3]
frame = character[4]
character_right = True


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

touch = False
pause = False
points = 0

font = pygame.font.SysFont("thinsansregular", 25, True)
pause_text = font.render('"p" para pausar o Jogo.', True, "black")
pause_text_rect = pause_text.get_rect(center=(window_width-250, 45))

continue_text = font.render('"c" para continuar.', True, "black")
continue_text_rect = continue_text.get_rect(center=(window_width-250, 45))

fps = pygame.time.Clock()

running = True
while running:
    fps.tick(60)
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause = True
            if event.key == pygame.K_c:
                pause = False

    if pause:
        screen.blit(continue_text, continue_text_rect)
    else:
        screen.blit(bushe4, (765, 545))
        screen.blit(tree, (750, 375))
        screen.blit(pointer, (738, 576))
        screen.blit(bushe1, (345, 540))
        screen.blit(bushe2, (34, 560))
        screen.blit(bushe3, (576, 581))

        screen.blit(pause_text, pause_text_rect)

        # LUCKY BLOCK
        if (x >= block_x-50 and x <= block_x+50) and (y <= false_block_y):
            effect = get_effect_image(10, 0, "assets/Enemies/Slime/Idle-Run (44x30).png")
            animation_list_effect = effect[0]
            animation_steps_effect = effect[1]
            animation_countdown_effect = effect[2]
            last_update_effect = effect[3]
            frame_effect = effect[4]

            touch = True

        screen.blit(lucky_block, (block_x, block_y))

        if touch:
            points += 1
            block_x = randint(50, 910)

            touch_sound = pygame.mixer.Sound("assets/Sounds/Magic.wav")
            touch_sound.play()
            touch = False

        # MONSTER
        if monster_x > x:
            monster_facing_right = True
            monster_x -= monster_speed
        elif monster_x < x:
            monster_facing_right = False
            monster_x += monster_speed

        if frame_monster >= animation_steps_monster-1:
            frame_monster = 0

        current_time_monster = pygame.time.get_ticks()

        if current_time_monster - last_update_monster >= animation_countdown_monster:
            frame_monster += 1
            last_update_monster = current_time_monster

        monster_image = animation_list_monster[frame_monster]
        if not monster_facing_right:
            monster_image = pygame.transform.flip(monster_image, True, False)

        screen.blit(monster_image, (monster_x, monster_y))

        # CHARACTER
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and x > 10:
            character_right = False
            character = get_character_image(11, 0, "assets/Characters/Virtual Guy/Idle - left(32x32).png")
            animation_list = character[0]
            animation_steps = character[1]
            animation_countdown = character[2]
            last_update = character[3]
            frame = character[4]

            x -= speed
        if key[pygame.K_RIGHT] and x < window_width-74:
            character_right = True
            character = get_character_image(11, 0, "assets/Characters/Virtual Guy/Idle (32x32).png")
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
            if character_right:
                jump = pygame.image.load("assets/Characters/Virtual Guy/Jump (32x32).png")
            else:
                jump = pygame.image.load("assets/Characters/Virtual Guy/Jump - left(32x32).png")

            jump = pygame.transform.scale(jump, (64, 64))
            screen.blit(jump, (x, y))

            y -= VELOCITY
            VELOCITY -= GRAVITY

            if VELOCITY < -JUMP_HEIGHT:
                VELOCITY = JUMP_HEIGHT
                jumping = False
                jump_sound = pygame.mixer.Sound("assets/Sounds/Jump.wav")
                jump_sound.set_volume(0.5)
                jump_sound.play()

        # MAP
        for row_index, row in enumerate(tiled_map):
            for col_index, tile in enumerate(row):
                if tile != 0:
                    tile_x = col_index * tile_size
                    tile_y = row_index * tile_size
                    screen.blit(blocks[tile], (tile_x, tile_y))

        # Collision
        character_rect = pygame.Rect(x+17, y+8, 30, 56)
        monster_rect = pygame.Rect(monster_x+7, monster_y+14, 40, 26)

        text = font.render(f"Pontos: {points}", True, "black")
        screen.blit(text, (35, 70))

        if character_rect.colliderect(monster_rect):
            font = pygame.font.SysFont("thinsansregular", 35, True)
            text = font.render("Você perdeu!", True, "red")
            text_rect = text.get_rect(center=(window_width // 2, window_height // 2))

            screen.blit(text, text_rect)

            gameover_sound = pygame.mixer.Sound("assets/Sounds/gameover.wav")
            gameover_sound.play()
            game_sound.stop()
            pygame.display.update()

            pygame.time.delay(1350)
            running = False

    pygame.display.update()

pygame.quit()
