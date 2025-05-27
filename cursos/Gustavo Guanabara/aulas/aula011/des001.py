numeros = []

for repeticao in range(5):
    numero = int(input('Digite um número:\n>>>'))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)
print(f'Você digitou os números {numeros}')
print(f'O menor número foi {menor} e aparece na posição {numeros.index(menor)+1}')
print(f'O maior número foi {maior} e aparece na posição {numeros.index(maior)+1}')
