import time, json

def pomodoro():
    iniciar = input('Deseja iniciar? [S/N]\n>>>').strip().upper()
    while iniciar not in ['S', 'N']:
        iniciar = input('Digite corretamente.\nDeseja iniciar? [S/N]\n>>>').strip().upper()

    if iniciar == 'S':
        inicio = time.time()

        for _ in range(1):
            parar = input('Digite qualquer coisa para parar:\n>>>')

            fim = time.time()
            segs = round(fim - inicio, 2)


            horas = int(segs // 3600)
            minutos = int((segs % 3600) // 60)
            segundos = int(segs % 60)
            
            horario = f'{horas:02d}:{minutos:02d}:{segundos:02d}'
            
            guardar = input(f'Deseja guardar {horario}? [S/N]\n>>>').strip().upper()
            while guardar not in ['S', 'N']:
                guardar = input(f'Digite corretamente. \nDeseja guardar {horario}? [S/N]\n>>>').strip().upper()

            if guardar == 'S':
                try:
                    with open('arquivo.json', 'r') as arquivo:
                        dados = json.load(arquivo)

                        secs = dados['segundos']; secs += segundos
                        mins = dados['minutos']; mins += minutos
                        hrs = dados['horas']; hrs += horas

                        if secs >= 60:
                            secs -= 60
                            mins += 1

                        if mins >= 60:
                            mins -= 60
                            hrs += 1

                    atualizado = {
                        "horas": hrs,
                        "minutos": mins,
                        "segundos": secs,
                    }

                    with open('arquivo.json', 'w') as arquivo:
                        json.dump(atualizado, arquivo)
                except:
                    dados = {
                        "horas": horas,
                        "minutos": minutos,
                        "segundos": segundos,
                    }
                    with open('arquivo.json', 'w') as arquivo:
                        json.dump(dados, arquivo)

            elif guardar == 'N':
                pass

    elif iniciar == 'N':
        pass

while True:
    print('\n=== MENU ===')
    print('1: Pomodoro')
    print('2: Sair')

    menu = int(input('Digite o menu:\n>>>'))
    while menu not in range(1, 3):
        menu = int(input('Digite corretamente:\n>>>'))

    if menu == 1:
        pomodoro()
    elif menu == 2:
        break
