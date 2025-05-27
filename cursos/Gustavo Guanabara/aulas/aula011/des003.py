numeros = []

while True:
    numero = int(input('Digite um número:\n>>>'))
    numeros.append(numero)

    continuar = input("Deseja continuar? [S/N]\n>>>").strip().upper()
    while continuar not in 'SN':
        continuar = input("Digite corretamente: [S/N]\n>>>").strip().upper()
    if continuar == 'N':
        break

print(f'A quantidade de números digitados foram {len(numeros)}')
print(f'A lista em ordem decrescente é {sorted(numeros, reverse=True)}')
print(f'5 está presente na lista' if 5 in numeros else '5 não está presente na lista')