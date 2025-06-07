# Crie uma função que receba uma lista de números e retorne todos os números da lista menores que 5
def menores5(lista):
  menores = [item for item in lista if item < 5]
  return menores if len(menores) > 0 else 'A lista não possui nenhum número menor que 5'
print(menores5([1, 2, 3, 4, 5, 6]))
print(menores5([4, 8, 12, 3, 6, 9]))
print(menores5([550, 220, 430, 340, 125]))
