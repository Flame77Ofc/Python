# Crie uma função que recebe uma lista de números entre 1 e 10 e retorne o número que falta
def falta(lista):
  numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  if len(lista) == 9:
    for i in numeros:
      if i not in lista:
        return i
  else:
    return 'Não foi possível verificar'

print(falta([1, 2, 3, 4, 6, 7, 8, 9, 10]))
print(falta([2, 3, 4, 5, 6, 7, 8, 10]))
print(falta([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
