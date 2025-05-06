# Crie um programa que receba 5 números digitados e, ao fim, exibir quantos números são pares.
pares = 0

for cont in range(5):
  num = int(input("Digite um número: "))
  if num % 2 == 0:
    pares += 1

print(f"Quantidade de pares: {pares}")