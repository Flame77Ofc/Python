# Crie um dicionário que possui votos positivos e votos negativos. Crie uma função e retorne quantos votos são

def eleicao(votos: dict):
  calculo = votos['votos positivos'] - votos['votos negativos']
  return calculo
print(eleicao({ 'votos positivos': 5, 'votos negativos': 2 }))
print(eleicao({ 'votos positivos': 12, 'votos negativos': 36 }))
print(eleicao({ 'votos positivos': 1600, 'votos negativos': 554 }))
