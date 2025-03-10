# Encadeamento de laços de repetição
for cont in range(1, 6):
    print(f'\n Rodada: {cont}')
    for contIn in range(2, 0, -1):
        print(f'valor: {contIn}')

import random
for a in range(1, 6):
    print(f'\n conjunto {a}')
    for b in range(5):
        num = random.randint(1,100)
        print(f'valor: {num}')