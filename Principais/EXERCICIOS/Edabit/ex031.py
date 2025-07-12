# Crie uma função que retorne uma string determinada quantidade de vezes
def repetir(string: str, quantidade: int) -> str:
  if string == str(string):
    return string * quantidade
  else:
    return 'Não é uma string'
print(repetir('Ho Ho Ho!', 2))
print(repetir('Super Man', 6))
print(repetir('6554', 2))
print(repetir(24, 2))
