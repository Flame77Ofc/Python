# Crie uma função que retorne a quantidade de parâmetros que foi passado
def quantidade(*parametros):
  return len(parametros)
print(quantidade(1, 2, 3, 4, 5))
print(quantidade('x', 'y', True, False))
print(quantidade(False))