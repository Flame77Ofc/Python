# Funções
"""def nome da função(parametros ou argumentos opcionais):
    bloco de codigo"""

def hello():
    print('Oi!')
hello()

def soma(x, y):
    print(f"A soma é {x + y}")
soma(12, 4)

def mult(x, y):
    return x * y
a = 5
b = 8
c = mult(a, b)
print(c)