# Usando list comprehensions, crie uma função que acha todos os números pares do número 1 até o número recebido
def acha_pares(numero):
  pares = [x for x in range(1, numero+1) if x % 2 == 0]
  return pares if len(pares) >= 1 else 'Não foi possível encontrar'
print(acha_pares(8))
print(acha_pares(4))
print(acha_pares(3))
print(acha_pares(0))
