class Falcao:
    def __init__(self, cor, velocidade):
        self.cor = cor
        self.velocidade = velocidade

    def voando(self):
        print(f'O falcão está voando a {self.velocidade}Km/h')

Halk = Falcao('branco', 245)
Halk.voando()





class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

class Rinoceronte(Animal):
    def correndo(self):
        print(f'O rinoceronte está correndo atrás de suas presas!')

rinoceronte = Rinoceronte('Rinoceronte', 'Branco')
rinoceronte.correndo()