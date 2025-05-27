from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os números sorteados foram ', end='')
for numero in numeros:
    print(f'{numero}', end=' ')

print(f'\nO maior número foi {max(numeros)}')
print(f'O maior número foi {min(numeros)}')