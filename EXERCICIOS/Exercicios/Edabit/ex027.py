# Crie um programa que seja capaz de converter quilômetros para metros e vice-versa.
def conversor(unidade, distancia):
  unidade = unidade.lower()
  if unidade == 'quilômetro' or unidade == 'quilometros' or unidade == 'quilômetros' or unidade == 'quilômetros':
    conversao = round(distancia * 1000, 2)
    return f'A distância em metros é de {conversao}'
  elif unidade == 'metro' or unidade == 'metros':
    conversao = round(distancia / 1000, 2)
    return f'A distância em quilômetros é de {conversao}'

print(conversor('metros', 6500))
print(conversor('quilometros', 120))
print(conversor('metros', 130))
print(conversor('quilômetros', 134))
