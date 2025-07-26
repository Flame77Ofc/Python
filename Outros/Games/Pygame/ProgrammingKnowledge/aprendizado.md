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

