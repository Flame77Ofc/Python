# Crie uma função que receba 3 argumentos (x, y, z) e retorne uma lista contendo x sublistas. (Exemplo [[], [], []]), cada contendo y números do item z
def matrix(sublistas, itens, conteudo):
  matriz = []
  for i in range(sublistas):
    matriz.append([conteudo] * itens)
  print(matriz)
matrix(3, 2, 3)
matrix(2, 1, "edabit")
matrix(3, 2, 0)
