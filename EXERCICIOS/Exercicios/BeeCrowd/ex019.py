"""Ler um número inteiro N e calcular todos os seus divisores.
"""

n = int(input('Digite um número:'))
i = 0
while True:
    i += 1
    if n % i == 0:
        print(i)

    if i == n:
        break