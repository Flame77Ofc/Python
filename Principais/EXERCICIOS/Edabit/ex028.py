# Crie uma função que tem um número como argumento e retorne uma sequência de 1 até o número informado, em uma lista
def contagem(numero):
  sequencia = [x+1 for x in range(numero)]
  return sequencia
print(contagem(5))
print(contagem(12))
print(contagem(25))

