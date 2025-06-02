# Vamos melhorar o jogo que fizemos no exercício 28(Computador excolhe um número entre 1 a 5 e o usuário deve adivinhar o número). A partir de agora, o computador vai sortear um número entre 1 e 10 e o jogador vai ter 4 tentativas para tentar acertar.
from random import randint

computador = randint(1, 10)

for i in range(4):
    print(f'⏳Tentativa {i+1}/4⏳'.center(50, '-'))

    escolha = int(input('Tente adivinhar o número entre 1 a 10: '))
    while escolha <= 0 or escolha > 10:
        escolha = int(input('❓Por favor, escolha um número entre 1 a 10❓: '))
    
    if escolha == computador:
        print('🎇 Você acertou!🎇')
        break
    else:
        if i == 3:
            print(f'🎈O número era {computador}🎈')
        else:
            print('❌ Você errou. Tente novamente❌')


# exercicio 28:
# from random import randint

# computador = randint(1, 5)
# escolha = int(input('Tente adivinhar o número entre 1 a 5: '))

# while escolha <= 0 or escolha > 5:
#     escolha = int(input('Por favor, escolha um número entre 1 a 5: '))

# print(f'Você acertou' if escolha == computador else f'Você errou, o número era {computador}')