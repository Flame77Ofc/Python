numeros = 0
soma = 0
maior = 0
menor = 0

while True:
    numero = int(input("Digite um número: "))

    numeros += 1
    soma += numero

    if numeros == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

    continuar = input("Deseja continuar? [S/N]: ").upper()
    if continuar == 'N':
        break

media = soma / numeros
print(f'Foram {numeros} numeros com a média de {media}')
print(f'O maior número foi {maior} e o menor número foi {menor}')