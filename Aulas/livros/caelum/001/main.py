import random

numero = random.randint(1, 100)
tentativas = 5
while tentativas > 0:
    print(f'Tentativas: {tentativas}')
    chute = int(input('Acerte o número entre 1 a 100: '))

    tentativas -= 1

    if chute == numero:
        print('Você acertou!')
        break
    elif tentativas == 0:
        print(f'O número era {numero}')
    elif chute > numero: 
        print('Mais baixo')
    elif chute < numero: 
        print('Mais alto')
    