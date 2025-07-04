# Exercício 8.1 Escreva uma função que retorne o maior de dois números. Valores esperados: máximo(5,6) == 6 máximo(2,1) == 2 máximo(7,7) == 7
def maximo(n1: int, n2: int) -> int:
  # Maneira 1
  # return max(n1, n2)

  # Maneira 2
  # return n1 if n1 > n2 else n2

  # Maneira 3
  lista = [n1, n2]
  return max(lista)
print(maximo(7, 6))
print(maximo(5, 3))
print(maximo(12, 24))
