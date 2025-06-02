def timer(segundos):
    minutos = (segundos % 3600) // 60
    horas = segundos // 3600
    segundos_restantes = segundos % 60

    tempo = f'{horas:02}:{minutos:02}:{segundos_restantes:02}'
    return tempo

print(timer(60))
print(timer(60000))
