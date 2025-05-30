import random, time
jogos = int(input('Quantos jogos você quer?\n>>>'))
lista = []

for i in range(jogos):
    # Modo Antigo
        # num1 = random.randint(1, 60)
        # num2 = random.randint(1, 60)
        # num3 = random.randint(1, 60)
        # num4 = random.randint(1, 60)
        # num5 = random.randint(1, 60)
        # num6 = random.randint(1, 60)
        # jogo = [num1, num2, num3, num4, num5, num6]
    for a in range(6):
        num = random.randint(1, 60)
        while num in lista:
            num = random.randint(1, 60)
        lista.append(num)
        lista.sort()
    time.sleep(1)
    print(f'Jogo {i+1}: {lista}')
    lista = []
