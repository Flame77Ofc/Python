# Como criar números sortidos pela máquina (Quase telesena)
import random

numeros = []
for i in range(6):
    lista = list(range(1, 100))
    num = random.choice(lista)
    numeros.append(num)
print(f'Os números sorteados foram {numeros}')