# Faça um programa que recebe a altura de um triangulo em um número inteiro e imprima-o utilizando asteriscos. Veja o Exemplo: 
# Entrada: 5
# *
# **
# ***
# ****
# *****
triangulo = int(input('Digite a altura do triângulo: '))
if triangulo <= 0 or triangulo > 20:
  print('Altura atingida. Deve ser entre 1 a 20.')
else:
  for i in range(1, triangulo + 1):
    print(i * '*')
