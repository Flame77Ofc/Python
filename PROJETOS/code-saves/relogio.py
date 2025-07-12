import time

tempo = int(input('Digite o tempo (em segundos): '))

while tempo >= 0:
    horas = tempo // 3600
    minutos = (tempo % 3600) // 60
    segundos = tempo % 60

    print(f'\r{horas:02d}:{minutos:02d}:{segundos:02d}', end='', flush=True)
    time.sleep(1)
    tempo -= 1
