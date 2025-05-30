lista = [[], []]

for repeticao in range(7):
    numero = int(input('Digite um número:\n>>>'))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)


print(f'A lista completa é {lista}')
print(f'A lista com pares é {sorted(lista[0])}')
print(f'A lista com ímpares é {sorted(lista[1])}')