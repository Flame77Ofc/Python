# Crie uma função que retorne uma lista dos números entre o primeiro e o segundo número do paramêtro
def entre(n1: int, n2: int) -> list:
  numeros = [x for x in range(n1, n2+1)]
  return numeros
print(entre(5, 10))
print(entre(5, 5))
print(entre(6, 24))
