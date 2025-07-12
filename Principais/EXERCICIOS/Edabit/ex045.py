# Crie uma função que recebe ano e mês com parâmetros e return em que ano será após a quantidade de meses passar.
def tempo(ano, meses):
  mes = meses // 12
  return ano + mes
print(tempo(2020, 24))
print(tempo(1832, 2))
print(tempo(1444, 60))
