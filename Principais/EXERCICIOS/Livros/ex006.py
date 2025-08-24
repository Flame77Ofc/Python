# Crie um programa que leia 3 números e mostre qual o maior e o menor e em quais posições esses números foram digitados

numeros = []
for i in range(3):
    numero = int(input(f"Digite o numero {i+1}: "))
    numeros.append(numero)

maior = numeros.index(max(numeros))
menor = numeros.index(min(numeros))
print(f'O maior número é {numeros[maior]} e está na posição {maior+1}')
print(f'O menor número é {numeros[menor]} e está na posição {menor+1}')
