# Faça uma função que recebe 3 valores inteiros por parâmetro e retorna-os ordenados em ordem crescente.
def crescente(n1, n2, n3):
  ordem = [item for item in [n1, n2, n3]]
  ordem.sort()
  return ordem
print(crescente(12, 6, 5))
print(crescente(3, 25, 16))
print(crescente(240, 3, 176))
