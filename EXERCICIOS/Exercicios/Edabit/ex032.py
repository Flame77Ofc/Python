# Crie um função que retorne quantos caracteres uma string possui.
def caracteres(string: str) -> int:
  total = 0
  for i in string:
    total += 1
  return f'{string} possui {total} caracteres'

  # Ou simplesmente usar a função len()
  # return f'{string} possui {len(string)} caracteres'

print(caracteres('SpiderMan'))
print(caracteres('Python'))
print(caracteres('Linguagens de Programação'))
