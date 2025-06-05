# Faça uma função que recebe segundos e retorna também por parâmetro esse tempo em horas e minutos e segundos.
def tempo(segundos):
  horas = segundos // 3600
  segundos -= horas * 3600
  minutos = segundos // 60
  segundos -= minutos * 60

  return f'{horas} {"hora" if horas == 1 else "horas"}, {minutos} {"minuto" if minutos == 1 else "minutos"} e {segundos} {"segundo" if segundos == 1 else "segundos"}'

print(tempo(60))
print(tempo(120))
print(tempo(179))
print(tempo(6578))
