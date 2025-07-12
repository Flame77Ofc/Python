"""Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente.
"""

x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))

if x > y:
    print('Ordem Decrescente')
else:
    print('Ordem Crescente')
    