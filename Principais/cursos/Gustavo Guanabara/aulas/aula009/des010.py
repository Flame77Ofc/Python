total = precos1000 = menor = i = 0
barato = ''

while True:
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$"))
    i += 1

    total += preco

    if preco > 1000:
        precos1000 += 1

    if i == 1 or preco < menor:
        menor = preco
        barato = produto

    continuar = input("Deseja continuar? [S/N]: ").upper()
    while continuar not in ['N', 'S']:
        continuar = input("Deseja continuar? [S/N]: ").upper()
    if continuar == 'N':
        break


print(f'O total dos produtos foi {total}')
print(f'Há {precos1000} {"produto" if precos1000 == 1 else "produtos"} acima de 1000 reais')
print(f'O produto mais barato foi {barato}, que custou {menor}')