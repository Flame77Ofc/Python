tupla = ('Lápis', 1.75,
         'Borracha', 0.69,
         'Caneta', 2.99,
         'Caderno', 12.99,
         'Apontador', 3.49)

for pos in range(len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end='')
    else:
        print(f'R${tupla[pos]:>7.2f}')