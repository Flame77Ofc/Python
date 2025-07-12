matriz = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

esq = dir = 0
pares = impares = 0

for i in range(9):
    if dir > 2:
        dir = 0
        esq += 1
    valor = int(input(f'Digite um valor para matriz{[esq]}{[dir]}: '))
    matriz[esq][dir] = valor
    dir += 1

for linha in matriz:
    print(f'{linha}')
    for coluna in linha:
        if coluna % 2 == 0:
            pares += coluna
        elif coluna % 2 == 1:
            impares += coluna
    
print(f'A soma dos valores pares é {pares} e a soma dos valores ímpares é {impares}')
print(f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é {max(matriz[1][0], matriz[1][1], matriz[1][2])}')