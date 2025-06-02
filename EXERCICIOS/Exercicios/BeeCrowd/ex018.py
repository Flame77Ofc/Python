"""Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. O último dado, que não entrará nos cálculos, contém o valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos.
"""

total = 0
idades = 0

while True:
    idade = int(input('Digite uma idade: '))
    if idade < 0:
        break

    total += idade
    idades += 1
media = total / idades
print(round(media, 2))