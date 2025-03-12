# Tratamento de Erros e exceções ⇒ O try e o except são muito semelhantes ao if else, mas a diferença é que são específicos para tratamento de erros.

"""
try:
    numero = int(input('Digite um numero '))
    print('O número escolhido x 2:')
    print(numero * 2)
except:
    print('Caractere Invalido')
"""

"""
try:
    numero = 10 // 0
    print(numero)
except ZeroDivisionError:
    print('Caractere Invalido')
"""

"""
try:
    numero = 10
    print(numero // 0)
except ZeroDivisionError as erro:
    print(erro)
"""