"""Escreva um programa que leia o valor de uma camisa e a quantidade de camisas. Leia o valor de outra camisa e a quantidade dessa camisa. Em seguida crie a variável total que armazene o total do preço das duas camisas"""
total = 0

for i in range(2):
    camisa = int(input(f'Digite o preço da camisa {i+1}: '))
    quantidade = int(input(f'Quantas unidades?: '))

    total += camisa * quantidade
print(f'O total a pagar é {total}')