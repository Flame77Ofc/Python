import pygame
import random

pygame.init()

width, height = 960, 640
screen = pygame.display.set_mode((width, height))

background = pygame.image.load("assets/Background/bgs/summer 3/Summer3.png")
background = pygame.transform.scale(background, (width, height))

character_idle = pygame.image.load("assets/Characters/Ninja Frog/Idle (32x32).png")
character_run = pygame.image.load("assets/Characters/Ninja Frog/Run (32x32).png")
monster = pygame.image.load("assets/Enemies/Pink/Pink_Monster_Idle_4.png")


def get_image(sheet, frame, width, height, scale, color=None):
    image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
    image.blit(sheet, (0, 0), (width * frame, 0, width, height))
    image = pygame.transform.scale(image, (scale, scale))
    image.set_colorkey(pygame.Color(color))

    return image

animation_list = []
animation_steps = 11
animation_countdown = 50
last_update = pygame.time.get_ticks()
frame = 0

for animation in range(animation_steps):
    animation_list.append(get_image(character_idle, animation, 32, 32, 64, "black"))


animation_list_running = []
animation_steps_running = 12
animation_countdown_running = 25
last_update_running = pygame.time.get_ticks()
frame_running = 0

for animation in range(animation_steps_running):
    animation_list_running.append(get_image(character_run, animation, 32, 32, 64, "black"))


animation_list_monster = []
animation_steps_monster = 4
animation_countdown_monster = 150
last_update_monster = pygame.time.get_ticks()
frame_monster = 0

side = [0, 960]
monster_x, monster_y = side[random.randint(0, 1)], 550
speed_monster = 1

for animation in range(animation_steps_monster):
    animation_list_monster.append(get_image(monster, animation, 32, 32, 64, "black"))


jumping = False
GRAVITY = 1
VELOCITY = 15
JUMP_HEIGHT = VELOCITY

right = True
x, y = 450, 550
shoot_x, shoot_y = x, y
speed = 10

character_running = False
shots = []
speed_shot = 15
fail = False

fps = pygame.time.Clock()

# ignore
shot_object = pygame.draw.rect(screen, "black", (-50, -50, -50, -50), 0, 100)
monster_object = screen.blit(animation_list_monster[frame_monster], (monster_x, monster_y))
character = screen.blit(animation_list[frame], (x, y))

font = pygame.font.SysFont("thinsansregular", 30, True)
initial_seconds = pygame.time.get_ticks()

running = True
while running:
    fps.tick(60)
    screen.blit(background, (0, 0))

    seconds = pygame.time.get_ticks()
    second_text = font.render(f"Segundos: {(seconds - initial_seconds) // 1000}", True, "black")
    screen.blit(second_text, (45, 5))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # shoot
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                direction = 1 if right else -1
                offset = 50 if right else -10
                shots.append([x + offset, y + 25, direction])

    for shot in shots[:]:
        shot_object = pygame.draw.rect(screen, "black", (shot[0], shot[1], 15, 5), 0, 100)
        shot[0] += speed_shot * shot[2]

        if shot[0] > width or shot[0] < -50 or shoot_x == monster_x:
            shots.remove(shot)

    # keys
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and x > 10:
        right = False
        character_running = True

        x -= speed
    elif not key[pygame.K_LEFT]:
        character_running = False

        if key[pygame.K_RIGHT] and x < width-60:
            character_running = True
            right = True

            x += speed
        else:
            character_running = False

    if key[pygame.K_UP]:
        jumping = True

    # SPRITE SHEETS
    # Character Running
    if frame_running >= animation_steps_running-1:
        frame_running = 0

    current_time_running = pygame.time.get_ticks()
    if current_time_running - last_update_running >= animation_countdown_running:
        frame_running += 1
        last_update_running = current_time_running

    if character_running and right:
        screen.blit(animation_list_running[frame_running], (x, y))

    if character_running and not right:
        character_run_flipped = pygame.transform.flip(animation_list_running[frame_running], True, False)
        screen.blit(character_run_flipped, (x, y))

    # Character Jumping
    if jumping:
        jump = pygame.image.load("assets/Characters/Ninja Frog/Jump (32x32).png")
        jump = pygame.transform.scale(jump, (64, 64))

        if right:
            screen.blit(jump, (x, y))
        else:
            jump_flipped = pygame.transform.flip(jump, True, False)
            screen.blit(jump_flipped, (x, y))

        y -= VELOCITY
        VELOCITY -= GRAVITY

        if VELOCITY < -JUMP_HEIGHT:
            jumping = False
            VELOCITY = JUMP_HEIGHT

    else:
        # Character Idle
        if frame >= animation_steps-1:
            frame = 0

        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_countdown:
            frame += 1
            last_update = current_time

        if right and not character_running:
            character = screen.blit(animation_list[frame], (x, y))

        elif not right and not character_running:
            flipped_image = pygame.transform.flip(animation_list[frame], True, False)
            character = screen.blit(flipped_image, (x, y))

    # monster
    if x > monster_x:
        if x - abs(int(monster_x)) < 50:
            fail = True

        monster_object = screen.blit(animation_list_monster[frame_monster], (monster_x, monster_y))
        monster_x += speed_monster
    elif x < monster_x:
        if x - abs(int(monster_x)) > -45:
            fail = True

        monster_flip = pygame.transform.flip(animation_list_monster[frame_monster], True, False)
        monster_object = screen.blit(monster_flip, (monster_x, monster_y))
        monster_x -= speed_monster

    if frame_monster >= animation_steps_monster-1:
        frame_monster = 0

    current_time_monster = pygame.time.get_ticks()
    if current_time_monster - last_update_monster >= animation_countdown_monster:
        frame_monster += 1
        last_update_monster = current_time_monster

    if not speed_monster > 5:
        speed_monster += 0.001

    # Collision
    if shot_object.colliderect(monster_object):
        monster_x = side[random.randint(0, 1)]

    if fail:
        fail_text = font.render("Você perdeu!", True, "red")
        fail_text_rect = fail_text.get_rect(center=(width / 2, height / 2))
        screen.blit(fail_text, (fail_text_rect))

        pygame.display.update()
        pygame.time.delay(1500)

        running = False

    pygame.display.update()

pygame.quit()
