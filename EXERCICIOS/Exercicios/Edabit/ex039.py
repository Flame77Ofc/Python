# Crie uma função que receba uma lista e um número, e deve retornar o índice em que foi dado o número.
def index(lista: list, numero: int) -> int:
  return lista.index(numero) if numero in lista else 'O número não está na lista'
print(index([1, 2, 3, 4, 5], 5))
print(index([1, 5, 3], 5))
print(index([9, 8, 3], 3))
print(index([1, 2, 3], 4))