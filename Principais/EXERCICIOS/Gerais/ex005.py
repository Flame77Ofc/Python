# Crie um programa que armazene 10 números digitados pelo usuário em dois vetores: um somente para números pares, e outro somente para números ímpares. Após, exiba os valores dos dois vetores na tela, em sequência.
vetor = []
pares = []
impares = []

for i in range(10):
    numero = int(input(f'Digite o número {i+1}: '))
    vetor.append([numero])
    if numero % 2 == 0:
        pares.append([numero])
    else:
        impares.append([numero])

print(f'O vetor original é {vetor}')
print(f'Os valores pares do vetor são {pares}')
print(f'Os valores ímpares do vetor são {impares}')
