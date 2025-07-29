# APRENDENDO SPRITE SHEETS (SÓ FUNCIONAM PARA SPRITE SHEETS LONGOS)
import pygame

pygame.init()

window_width, window_height = 960, 640
screen = pygame.display.set_mode((window_width, window_height))

# PRIMEIRO PASSO: IMPORTAR O SPRITE SHEET POR MEIO DE UMA IMAGEM.
sprite_sheet = pygame.image.load("assets/Characters/tard.png")

# SEGUNDO PASSO: CRIAR A FUNÇÃO RESPONSÁVEL POR CONFIGURAR E AJEITAR O SPRITE: QUAL SPRITE SERÁ, EM QUAL FRAME ESTÁ, QUAL O TAMANHO DO SPRITE, QUAL A APLIAÇÃO, QUAL A COR QUE REMOVE O FUNDO.
def get_image(sheet: str, frame: int, width: int, height: str, scale: int, color: str):
    """
    sheet: A imagem do sprite_sheet, que já foi definida antes.
    frame: O frame em que a animação está. Por exemplo: Frame 0, 1, 2, 3, ...
    width: A largura que o sprite terá.
    height: A altura que o sprite terá.
    scale: Ampliação de imagem que o sprite terá.
    color: Cor que removerá o fundo.
    """

    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (frame * width, 0, width, height))
    image = pygame.transform.scale(image, (scale, scale))
    image.set_colorkey(color)

    return image

# get_image(sprite_sheet, 0, 24, 24, 64, "black")  # Exemplo de argumentos

# TERCEIRO PASSO: DEFINIR AS FUNCIONALIDADES GERAIS DO SPRITE: QUANTAS ANIMAÇÕES TEM, QUANTO TEMPO CADA ANIMAÇÃO SERÁ MOSTRADA NA TELA, EM QUAL FRAME ESTÁ, ETC.
animation_list = []
animation_steps = 23
animation_countdown = 75
last_update = pygame.time.get_ticks()
frame = 17

# QUARTO PASSO: ITERAR SOBRE CADA ANIMATIONS_STEPS.
for frame in range(animation_steps):
    animation_list.append(get_image(sprite_sheet, frame, 24, 24, 64, "black"))

running = True
while running:
    screen.fill("grey")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # QUINTO PASSO: VERIFICAR SE FRAME JÁ ULTRAPASSOU DE ANIMATION_STEPS.
    if frame >= animation_steps-1:
        frame = 17

    # QUINTO PASSO: ATUALIZAR O FRAME.
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_countdown:
        frame += 1
        last_update = current_time

    # SEXTO PASSO: MOSTRAR O SPRITE NA TELA.
    screen.blit(animation_list[frame], (0, 0))

    pygame.display.update()

pygame.quit()
