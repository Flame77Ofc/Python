# Módulos em python
import math
numero = int(input("Digite um número: "))
raiz = math.sqrt(numero)
print(f'A raíz de {numero} é {raiz}')


# Números aleatórios
from random import randint
aleatorio = randint(1, 10)
print(f'O número escolhido é {aleatorio}')


# Desafios
# Crie um programa que leia um número e imprima o número na sua porção inteira, ou seja, sem casas decimais.
numero = float(input("Por favor, digite um número decimal: "))
print(f"O número foi convertido para {math.floor(numero)}")