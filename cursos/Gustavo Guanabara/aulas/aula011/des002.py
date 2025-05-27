numeros = []
while True:
    numero = int(input('Digite um número:\n>>>'))
    if numero in numeros:
        numero = int(input(f'Este número já está na lista, digite novamente:\n>>>'))
    numeros.append(numero)

    continuar = input("Deseja continuar? [S/N]\n>>>").strip().upper()
    while continuar not in 'SN':
        continuar = input("Digite corretamente: [S/N]\n>>>").strip().upper()
    if continuar == 'N':
        break
numeros.sort()
print(f'Os valor digitados foram {numeros}')