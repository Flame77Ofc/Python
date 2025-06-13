import time
import json
import datetime
from pathlib import Path

def initialize_data_file():
    data_file = Path('data.json')
    if not data_file.exists() or data_file.stat().st_size == 0:
        nome = input('Digite o seu nome: ').strip()
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump({'Nome': nome}, f, indent=4)
    with open(data_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_horas():
    horas_file = Path('horas.json')
    if horas_file.exists():
        with open(horas_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_horas(data):
    with open('horas.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def pomodoro(nome):
    iniciar = input('Deseja iniciar? [S/N]\n>>> ').strip().upper()
    while iniciar not in ['S', 'N']:
        iniciar = input('Digite corretamente.\nDeseja iniciar? [S/N]\n>>> ').strip().upper()

    if iniciar != 'S':
        return

    tarefa = input('Digite o nome da tarefa: ').strip().title()
    if not tarefa:
        print("Tarefa inválida!")
        return

    inicio = time.time()
    input('Pressione Enter para parar o Pomodoro:\n>>> ')
    fim = time.time()
    segs = round(fim - inicio)

    horas = segs // 3600
    minutos = (segs % 3600) // 60
    segundos = segs % 60
    horario = f'{horas:02d}:{minutos:02d}:{segundos:02d}'

    guardar = input(f'Deseja guardar {horario}? [S/N]\n>>> ').strip().upper()
    while guardar not in ['S', 'N']:
        guardar = input(f'Digite corretamente.\nDeseja guardar {horario}? [S/N]\n>>> ').strip().upper()

    if guardar == 'S':
        horas_data = load_horas()
        if tarefa in horas_data:
            horas_data[tarefa]['horas'] += horas
            horas_data[tarefa]['minutos'] += minutos
            horas_data[tarefa]['segundos'] += segundos
        else:
            horas_data[tarefa] = {'horas': horas, 'minutos': minutos, 'segundos': segundos}

        for task in horas_data:
            secs = horas_data[task]['segundos']
            mins = horas_data[task]['minutos']
            hrs = horas_data[task]['horas']
            if secs >= 60:
                mins += secs // 60
                horas_data[task]['segundos'] = secs % 60
            if mins >= 60:
                hrs += mins // 60
                horas_data[task]['minutos'] = mins % 60
            horas_data[task]['horas'] = hrs

        save_horas(horas_data)

        with open('tarefas.txt', 'a', encoding='utf-8') as arquivo:
            data = datetime.datetime.now().strftime('%d/%m/%Y -> %H:%M:%S')
            arquivo.write(f'➥{data}\n{nome} adicionou a tarefa "{tarefa}" {horas} horas, {minutos} minutos e {segundos} segundos.\n\n')
    else:
        print(f"Tempo de {horario} descartado.")

def main():
    dados = initialize_data_file()
    nome = dados['Nome']

    while True:
        print('\n=== MENU ===')
        print('1: Pomodoro')
        print('2: Sair')
        try:
            menu = int(input('Digite o menu:\n>>> '))
            if menu not in [1, 2]:
                print('Digite um número entre 1 e 2.')
                continue
        except ValueError:
            print('Digite um número válido.')
            continue

        if menu == 1:
            pomodoro(nome)
        elif menu == 2:
            print("Saindo...")
            break

if __name__ == '__main__':
    main()