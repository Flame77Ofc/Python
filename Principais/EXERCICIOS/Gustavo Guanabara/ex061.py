# Escreva um programa que leia um número qualquer e mostre a tabuada desse número, usando a estrutura “para”.
# Ex: Digite um valor: 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15 ...

tabuada = int(input('Digite um número para tabuada: '))
for i in range(1, 11):
    print(f'{i} X {tabuada} = {i * tabuada}')