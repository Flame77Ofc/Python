import time

tempo = int(input())

for repeticao in range(tempo, 0, -1):
    segundos = repeticao % 60
    minutos = repeticao // 60
    horas = repeticao // 3600

    print(f'{horas:02d}:{minutos:02d}:{segundos:02d}')
    time.sleep(1)


# relogio 2
import time

tempo = int(input('Digite o tempo (em segundos): '))

while tempo >= 0:
    horas = tempo // 3600
    minutos = (tempo % 3600) // 60
    segundos = tempo % 60

    print(f'\r{horas:02d}:{minutos:02d}:{segundos:02d}', end='', flush=True)
    time.sleep(1)
    tempo -= 1
