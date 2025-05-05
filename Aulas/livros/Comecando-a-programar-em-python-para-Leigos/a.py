# enumerate
"exemplo 1"
nomes = ['Gabriel', 'Lucas']
vendas = [135, 900]

for i, nome in enumerate(nomes):
    print(f'{nome} fez {vendas[i]} vendas')


# zip
"exemplo 1"
nomes = ['João', 'Felipe']
vendas = [120, 345]

for nome, venda in zip(nomes, vendas):
    print(f'{nome} fez {venda} vendas')

"exemplo 2"
nomes = ['Leonardo', 'Maria']
idades = [15, 24]

for nome, idade in zip(nomes, idades):
    print(f'{nome} tem {idade} anos')