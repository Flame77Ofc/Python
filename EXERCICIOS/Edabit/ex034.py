# Crie uma função que receba duas strings como argumento e retorna o número de vezes que a primeira string (a string única) é encontrada na segunda string.
def encontrar(letra: str, string: str) -> int:
  letra = letra.lower()
  string = string.lower()
  return string.count(letra) if letra in string else 'A letra não está presente'
print(encontrar('a', 'No mercado há abacaxis'))
print(encontrar('e', 'A praia tem um belo mar'))
print(encontrar('t', 'morcegos são mamíferos'))
