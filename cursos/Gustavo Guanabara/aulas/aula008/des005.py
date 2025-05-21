# faça um programa que leia 6 números inteiras e imprima a soma se eles forem pares
soma = 0
for i in range(1, 7):
    numero = int(input("Digite o número: "))
    if numero % 2 == 0:
        soma += numero
print(f'A soma dos números pares é {soma}')