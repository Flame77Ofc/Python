# Funções
"""
def nome_da_função(parametro):
    corpo_da_função
    return retorno

Invocar
nome_da_função(argumentos)
"""

def maior(x, y):
    return max(x, y)
print(maior(12, 5))

def calculaQuadrados(lista):
    for elemento in lista:
        quadrado = elemento ** 2
        print(quadrado)
lista_inteiros = [1,2,3,4,5]
calculaQuadrados(lista_inteiros)