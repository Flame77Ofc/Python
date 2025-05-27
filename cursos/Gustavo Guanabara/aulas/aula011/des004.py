numeros = []
pares = []
impares = []

while True:
    numero = int(input('Digite um número:\n>>>'))
    numeros.append(numero)

    if numero % 2 == 0: 
        pares.append(numero)
    else:
        impares.append(numero)

    continuar = input("Deseja continuar? [S/N]\n>>>").strip().upper()
    while continuar not in 'SN':
        continuar = input("Digite corretamente: [S/N]\n>>>").strip().upper()
    if continuar == 'N':
        break

print(f'A lista completa é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')