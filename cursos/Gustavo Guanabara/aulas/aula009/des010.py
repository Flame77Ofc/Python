total = precos1000 = maior = menor = 0
barato = ''
i = 0

while True:
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$"))

    total += preco

    if preco > 1000:
        precos1000 += 1

    if i == 1:
        maior = preco
        barato = produto
    else:
        if preco > maior:
            maior = preco
        elif preco < menor:
            barato = produto
            menor = preco



    continuar = input("Deseja continuar? [S/N]: ").upper()
    while continuar not in ['N', 'S']:
        continuar = input("Deseja continuar? [S/N]: ").upper()
    if continuar == 'N':
        break

    i += 1

print(f'O total dos produtos foi {total}')
print(f'Há {precos1000} {'produto' if precos1000 == 1 else 'produtos'} acima de 1000 reais')
print(f'O produto mais barato foi {barato}, que custou {menor}')