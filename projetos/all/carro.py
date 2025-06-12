import time

class Carro:
    def __init__(self, nome, marca, modelo, cor):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.status = False
        self.velocidade_atual = 0

    def ligar(self):
        if self.status:
            print('O carro já está ligado')
        else:
            self.status = True
            print('Carro ligado')

    def desligar(self):
        if self.status:
            self.status = False
            print('Carro desligado')
        else:
            print('O carro já está desligado')

    def acelerar(self):
        if self.status:
            velocidade = int(input('Digite a Velocidade: '))

            self.velocidade_atual += velocidade
            print('Andando...')
            for i in range(self.velocidade_atual):
                print(f'\r{i}', end='', flush=True)
                time.sleep(0.1)
            print('Velocidade')
        else:
            print('Por favor, primeiramente ligue o carro.')


nome = input('Digite o nome do carro:\n>>>').strip()
marca = input('Digite a marca do carro:\n>>>').strip()
modelo = input('Digite o modelo do carro:\n>>>').strip()
cor = input('Digite a cor do carro:\n>>>').strip()

carro = Carro(nome, marca, modelo, cor)

while True:
    print('\n=== MENU ===')
    print('1: Ligar o carro')
    print('2: Andar')
    print('3: Desligar o carro')
    print('4: Sair')

    menu = int(input('Digite o menu:\n>>>'))
    while menu not in range(1, 5):
        menu = int(input('Digite corretamente:\n>>>'))
    

    if menu == 1:
        carro.ligar()
    elif menu == 2:
        carro.acelerar()
    elif menu == 3:
        carro.desligar()
    elif menu == 4:
        break
