# Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares, ao final do processo exiba em tela quantos números ímpares foram encontrados nesse intervalo, assim como a soma dos mesmos

lista = []
impares = 0
soma = 0
for i in range(1, 101):
    if i % 2 == 1:
        lista.append(i)
        impares += 1
        soma += i
print(*lista, sep=', ')
print(f'Foram encontrados {impares} números ímpares')
print(f'A soma destes números ímpares é de {soma}')
