# Crie uma função que tem um único argumento de string e retorna uma lista ordernada contedo os índices de todas as letras capitalizadas na string.
def capitalizadas(string: str):
  indices = []
  for letra in string:
    if letra.isupper():
      indices.append(string.index(letra))
  return indices
print(capitalizadas('STRIKE'))
print(capitalizadas('Pedro TEM 14 AnOs'))
