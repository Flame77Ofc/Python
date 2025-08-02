$ Formas Geométricas $
- Para criar um círculo:
pygame.draw.circle(screen, color, coordinates, thickness, 0=fill, 1,...=outline only, draw_top_right, draw_top_left, draw_bottom_left,draw_bottom_right)

- Para criar uma linha:
pygame.draw.line(screen, color, initial pos., final pos., thickness)

- Para criar um retângulo:
pygame.draw.rect(screen, color,  x, y, width, height, 0 value, border-radius)


$ eventos $
**Game Loop**:
key = pygame.key.get_pressed()
if key[pygame.K_LEFT]:
    x -= speed
if key[pygame.K_RIGHT]:
    x += speed
if key[pygame.K_UP]:
    y -= speed
if key[pygame.K_DOWN]:
    y += speed


$ Background-Color $
definindo o fundo como RGB: **screen.fill((0, 0, 255))**
definindo o fundo como cor em string: **screen.filll("blue")**


$ Definindo fontes $
1. Definindo as configurações da cor (Fonte e Estilo)
font = pygame.font.SysFont("font", size, bold, italic)

2. Colocando o texto
text = font.render("text", antialias, "color")

3. Definindo o texto dentro do Game Loop
screen.blit(text, (x, y))


$ Fazer delay $
pygame.time.delay(mileseconds)


$ Adicionando Som $
sound = pygame.mixer.Sound("path")
sound.set_volume(float)  # Volume

sound.play(loops)  # nota: Se configurar loops para -1, repetirá para sempre.


$ Limitando os movimentos do personagem $
character = pygame.image.load("character.png")
character_width = 45
character_height = 45
x, y = window_width / 2, window_height / 2
speed = 10

**Game Loop**:

key = pygame.key.get_pressed()
if key[pygame.K_LEFT] and x > character_width-5:
    x -= speed
if key[pygame.K_RIGHT] and x < window_width-character_width-5:
    x += speed
if key[pygame.K_UP] and y > character_height-5:
    y -= speed
if key[pygame.K_DOWN] and y < character_height-character_height-5:
    y += speed


$ KeyBoard $
**Game Loop**:
    for event in pygame.event.key():

        # keydown: acontece quando o usuário clica na tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space")


        # keyup: acontece apenas quando o usuário solta a tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                print("Up")




$ mouse $
**Game Loop**:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse Down")
        if event.type == pygame.MOUSEBUTTONUP:
            print("Mouse Up")



$ Group $
class Square(pygame.sprite.Sprite):
    def __init__(self, color: str, width: int, height: int, x: int, y: int):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

square_group = pygame.sprite.Group()
square = Square("orange", 50, 50, 150, 340)
square_group.add(square)

**Game Loop**:
    square_group.draw(screen)
    pygame.display.update()
