# Formas Geométricas
- Para criar um círculo:
pygame.draw.circle(screen, color, coordinates, thickness, 0=fill, 1,...=outline only, draw_top_right, draw_top_left, draw_bottom_left,draw_bottom_right)

- Para criar uma linha:
pygame.draw.line(screen, color, initial pos., final pos., thickness)

- Para criar um retângulo:
pygame.draw.rect(screen, color,  x, y, width, height, 0 value, border-radius)


# eventos
*Dentro do Game Loop*
key = pygame.key.get_pressed()
if key[pygame.K_LEFT]:
    x -= speed
if key[pygame.K_RIGHT]:
    x += speed
if key[pygame.K_UP]:
    y -= speed
if key[pygame.K_DOWN]:
    y += speed


# Background-Color
definindo o fundo como RGB: **screen.fill((0, 0, 255))**
definindo o fundo como cor em string: **screen.filll("blue")**


# Definindo fontes
1. Definindo as configurações da cor (Fonte e Estilo)
font = pygame.font.SysFont("font", size, bold, italic)

2. Colocando o texto
text = font.render("text", antialias, "color")

3. Definindo o texto dentro do Game Loop
screen.blit(text, (x, y))


# Fazer delay (SEM time.sleep()!):
pygame.time.delay(mileseconds)


# Adicionando Som
sound = pygame.mixer.Sound("path")
sound.set_volume(float)  # Volume

sound.play(loops)  # nota: Se configurar loops para -1, repetirá para sempre.


# Limitando os movimentos do personagem
*Dentro do Game Loop:*

key = pygame.key.get_pressed()
if (key[pygame.K_LEFT] or key[pygame.K_a]) and **x > 50**:
    x -= speed
if (key[pygame.K_RIGHT] or key[pygame.K_d]) and **x < window_width - 50**:
    x += speed
if (key[pygame.K_UP] or key[pygame.K_w]) and **y > 50**:
    y -= speed
if (key[pygame.K_DOWN] or key[pygame.K_s]) and **y < window_height - 50**:
    y += speed
