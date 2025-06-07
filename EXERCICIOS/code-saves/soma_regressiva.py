# Faça um programa que leia um número e mostre na tela esse número + o número antecessor dele até um, e mostre o resultado desta soma. Exemplo:
# número: 5
# 5 + 4 + 3 + 2 + 1 = 15
numero = int(input('Digite um número: '))
total = 0
for i in range(numero, 1, -1):
  print(f"{i} + ", end='')
  total += i
print(f"{1} = {total+1}")