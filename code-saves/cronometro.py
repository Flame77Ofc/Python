import random, time

minutos = random.randint(1, 5)
segundos = 59

def relogio(minutos, segundos):
    while minutos > 0 or segundos > 0:
        print(f'{minutos:02d}:{segundos:02d}')
        time.sleep(1)

        if segundos == 0:
            segundos = 59
            minutos -= 1
        else:
            segundos -= 1
    print('00:00')
relogio(minutos, segundos)
