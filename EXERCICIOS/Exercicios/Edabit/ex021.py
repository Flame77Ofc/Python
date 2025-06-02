"""Crie uma função que verifica se um número especifico está na lista"""
def verifica(lista, num):
    return num in lista
print(verifica([1, 2, 3], 2))
print(verifica([5, 6, 7, 8, 9, 10], 3))
print(verifica([24, 65, 12, 76, 21, 87, 32, 45, 90], 56))
