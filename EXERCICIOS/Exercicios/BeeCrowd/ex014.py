"""Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.
"""
n = int(input('Digite um valor (deve ser abaixo de 10000): '))

i = 1
while i <= 10000:
    if i % n == 2:
        print(i)
    i += 1