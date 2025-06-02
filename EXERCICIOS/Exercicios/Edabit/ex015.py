"""Crie uma função que receba dois números como argumento e retorne se a soma entre estes dois números é menor que 100. Se a soma dos números for menor que 100, imprima True, se não, False"""
def menor100(x, y):
    return x + y <= 100
print(menor100(50, 50))