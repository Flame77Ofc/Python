"""Crie uma função que retorne a diferença entre o maior e o menor número de uma lista"""
def diferenca(lista):
    maior = max(lista)
    menor = min(lista)
    return maior - menor
print(diferenca([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))