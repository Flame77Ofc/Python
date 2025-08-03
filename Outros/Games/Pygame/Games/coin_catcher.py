import pygame
import random

pygame.init()

width, height = 1150, 640
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Coin Catcher")

bg = pygame.image.load("assets/Background/bgs/summer7/Summer7.png")
bg = pygame.transform.scale(bg, (width, height))

def draw_background():
    screen.blit(bg, (0, 0))


class Animals(pygame.sprite.Sprite):
    def __init__(self, file_path, steps, countdown, scale, x, y, speed):
        super().__init__()
        self.scale = scale
        self.x = x
        self.y = y
        self.speed = speed
        self.moving_left = True
        self.sprite_sheet = pygame.image.load(file_path).convert_alpha()
        self.animation_list = []
        self.animation_steps = steps
        self.animation_countdown = countdown
        self.last_update = pygame.time.get_ticks()
        self.frame = 0
        for i in range(self.animation_steps):
            self.animation_list.append(self.get_image(i, 16, 16, "black"))

    def get_image(self, frame, width, height, color):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sprite_sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (self.scale, self.scale))
        image.set_colorkey(color)
        return image

    def update(self):
        if self.moving_left:
            self.x -= self.speed
        else:
            self.x += self.speed
        if self.x <= 0:
            self.moving_left = False
        elif self.x + self.scale >= width:
            self.moving_left = True
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_countdown:
            self.frame = (self.frame + 1) % self.animation_steps
            self.last_update = current_time
        frame_image = self.animation_list[self.frame]
        if not self.moving_left:
            frame_image = pygame.transform.flip(frame_image, True, False)
        screen.blit(frame_image, (self.x, self.y))

bird = Animals("assets/Animals/bird.png", 3, 125, 32, 750, 595, 0.3)
bird2 = Animals("assets/Animals/bird.png", 3, 155, 32, 1045, 610, 0.4)
bird3 = Animals("assets/Animals/bird.png", 3, 195, 32, 15, 605, 0.2)

class Sprite(pygame.sprite.Sprite):
    GRAVITY = 1
    VELOCITY = 15
    JUMP_HEIGHT = VELOCITY

    def __init__(self, idle_path, run_path, steps, countdown, speed, jump_path, scale):
        super().__init__()
        self.x = 35
        self.y = 525
        self.speed = speed
        self.scale = scale
        self.image_idle = pygame.image.load(idle_path)
        self.image_run = pygame.image.load(run_path)
        self.sprite_jumping = pygame.transform.scale(pygame.image.load(jump_path), (scale, scale))
        self.sprite_jumping_flipped = pygame.transform.flip(self.sprite_jumping, True, False)
        self.animation_list = []
        self.animation_steps = steps
        self.animation_countdown = countdown
        self.last_update = pygame.time.get_ticks()
        self.frame = 0
        self.run_animation_list = []
        self.run_animation_steps = steps
        self.run_animation_countdown = countdown
        self.last_update_run = pygame.time.get_ticks()
        self.frame_run = 0
        self.jumping = False
        self.running = False
        self.right = True
        self.jump_velocity = self.VELOCITY
        self.rect = pygame.Rect(self.x, self.y, scale, scale)

    def get_image(self, sprite_sheet, frame, width, height, color):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sprite_sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (self.scale, self.scale))
        image.set_colorkey(color)
        return image

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_countdown:
            self.frame = (self.frame + 1) % self.animation_steps
            self.last_update = current_time
        if current_time - self.last_update_run >= self.run_animation_countdown:
            self.frame_run = (self.frame_run + 1) % self.run_animation_steps
            self.last_update_run = current_time
        key = pygame.key.get_pressed()
        self.running = False
        if key[pygame.K_LEFT] and self.x > 15:
            self.right = False
            self.running = True
            self.x -= self.speed
        if key[pygame.K_RIGHT] and self.x < 1075:
            self.right = True
            self.running = True
            self.x += self.speed
        if key[pygame.K_UP]:
            if not self.jumping:
                self.jumping = True
                self.jump_velocity = self.VELOCITY
        self.rect.topleft = (self.x, self.y)
        if self.jumping:
            self.y -= self.jump_velocity
            self.jump_velocity -= self.GRAVITY
            if self.jump_velocity < -self.JUMP_HEIGHT:
                self.jumping = False
                self.jump_velocity = self.VELOCITY
            if self.right:
                screen.blit(self.sprite_jumping, (self.x, self.y))
            else:
                screen.blit(self.sprite_jumping_flipped, (self.x, self.y))
        else:
            if self.running:
                frame = self.run_animation_list[self.frame_run]
            else:
                frame = self.animation_list[self.frame]
            if self.right:
                screen.blit(frame, (self.x, self.y))
            else:
                screen.blit(pygame.transform.flip(frame, True, False), (self.x, self.y))

virtual_guy = Sprite("assets/Characters/Virtual Guy/Idle (32x32).png", "assets/Characters/Virtual Guy/Run (32x32).png", 11, 75, 15, "assets/Characters/Virtual Guy/Jump (32x32).png", 64)

for i in range(virtual_guy.animation_steps):
    virtual_guy.animation_list.append(virtual_guy.get_image(virtual_guy.image_idle, i, 32, 32, "black"))
    virtual_guy.run_animation_list.append(virtual_guy.get_image(virtual_guy.image_run, i, 32, 32, "black"))

class Coin(pygame.sprite.Sprite):
    collected = 0
    last_increment = 0
    lost = 0

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.image = pygame.image.load("assets/Object/coin.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = random.randint(1, 5)

    def update(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)

        if virtual_guy.rect.colliderect(self.rect):
            Coin.collected += 1
            self.kill()

        if self.y >= height:
            coin_group.add(Coin(random.randint(50, width - 50), -50))
            Coin.last_increment = Coin.collected
            self.kill()
            Coin.lost += 1


coin_group = pygame.sprite.Group()
coin_group.add(Coin(random.randint(50, width - 50), -50))



game_over_font = pygame.font.SysFont("perpetuatitling", 35, True)
game_over_text = game_over_font.render("Game Over!", True, "red")
game_over_text_rect = game_over_text.get_rect(center=(width / 2, height / 2))

coins_collected_font = pygame.font.SysFont(None, 45)
hearts_left_font = pygame.font.SysFont("cambriamath", 35, True)


def main():
    fps = pygame.time.Clock()
    running = True

    while running:
        fps.tick(60)
        draw_background()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        bird.update()
        bird2.update()
        bird3.update()

        virtual_guy.update()
        coin_group.update()
        coin_group.draw(screen)

        if Coin.collected != Coin.last_increment:
            if Coin.collected == 5 or Coin.collected % 20 == 0:
                coin_group.add(Coin(random.randint(50, width - 50), -50))

            coin_group.add(Coin(random.randint(50, width - 50), -50))
            Coin.last_increment = Coin.collected

        text_coins_collected = coins_collected_font.render(f"Total coletadas: {Coin.collected}", True, "black")
        screen.blit(text_coins_collected, (10, 10))

        for i in range(0, 7):
            if Coin.lost == i:
                bar = pygame.image.load(f"assets/HUD/UI/greenbar_0{6-i}.png")

        hearts_left = hearts_left_font.render(f"Vidas: {6-Coin.lost}", True, "#183D9B")
        hearts_left_rect = hearts_left.get_rect(topleft=(width-hearts_left.get_width()*2, 0))
        screen.blit(hearts_left, hearts_left_rect)

        if Coin.lost == 6:
            screen.blit(game_over_text, game_over_text_rect)

            pygame.display.update()
            pygame.time.delay(750)

            running = False

        bar = pygame.transform.scale(bar, (68, 21))
        screen.blit(bar, (virtual_guy.x, virtual_guy.y-15))

        pygame.display.update()


    pygame.quit()

if __name__ == "__main__":
    main()
