# Crie uma função que recebe uma string e retorna uma lista das letras que aparecem apenas uma vez.
def letras_unicas(string: str) -> list:
  letras = []
  for i in string:
    if string.lower().count(i) == 1:
      letras.append(i)
  return letras
print(letras_unicas('Teste'))
print(letras_unicas('Python'))
print(letras_unicas('Mercado'))
print(letras_unicas('Tesoura'))
print(letras_unicas('Avião de Plástico'))
