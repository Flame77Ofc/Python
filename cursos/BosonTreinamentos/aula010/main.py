# Funções lambda ou Funções Anônimas
# função normal:
"""def soma(x, y):
    print(x + y)
soma(12, 8)"""
# função lambda

soma = lambda x, y: x + y
print(soma(12, 3))


par = lambda num: num % 2 == 0
print(par(4))

celsius_fahreinheit = lambda f: (f - 32) + 5/9
print(celsius_fahreinheit(100))

# Função map()
# map(função, iterável)
num = [1,2,3,4,5,6,7,8,9,10]
dobro = list(map(lambda x: x*2, num))
print(dobro)

palavras = ['Python', 'É', 'Uma', 'Linguagem', 'Legal!']
maiusculas = list(map(str.upper, palavras))
print(maiusculas)

# Função filter()
# filter(função, sequência)
def par(x):
    return x % 2 == 0

numeros = [1,2,3,4,5,6,7,8,9,10]
num_par = list(filter(par, numeros))
print(num_par)

numeros = [1,2,3,4,5,6,7,8,9,10]
num_impar = list(filter(lambda x: x %2 != 0, numeros))
print(num_impar)

# Função reduce()
# reduce(função, sequência, valor_inicial)
from functools import reduce
def mult(x, y):
    return x * y
numeros = [1,2,3,4,5,6]
total = reduce(mult, numeros)
print(total)