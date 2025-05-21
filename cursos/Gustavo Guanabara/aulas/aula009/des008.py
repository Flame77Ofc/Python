from random import randint
partidas = 0

while True:
    computador = randint(1, 10)

    numero = int(input('Digite o número: '))
    while numero < 0 or numero > 10:
        numero = int(input('Deve ser um número entre 0 a 10!: '))

    escolha = input('Par ou Ímpar? [P/I]: ').strip().upper()
    while escolha not in ['P', 'I']:
        print('Por favor, escolha corretamente.')
        escolha = input('Par ou Ímpar? [P/I]: ').strip().upper()

    total = numero + computador
    print(f'Você jogou {numero} e o computador {computador} resultando em {total}')

    if (escolha == 'P' and total % 2 == 0) or (escolha == 'I' and total % 2 == 1):
        print('Você ganhou!')
        partidas += 1
    else:
        print('Infelizmente você perdeu.')
        break

print(f'Você venceu {partidas} {'partida' if partidas == 1 else 'partidas'}.')