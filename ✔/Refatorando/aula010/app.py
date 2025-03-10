# POO ⇒ Programação Orientada a Objetos
class Carro:
    def __init__(self, marca, modelo, cor, ligado=False):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ligado = ligado

    def ligar(self):
        if self.ligado:
            print('Carro já está ligado')
        else:
            print('Carro ligado')
            self.ligado = True


    def desligar(self):
        if self.ligado:
            print('Carro desligado')
            self.ligado = False
        else:
            print('Carro já está ligado')
            

