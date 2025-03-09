# Class inheritance
class Veiculo:
    velocidadeAtual = 0

class Ferrari(Veiculo):
    def dirigir(self):
        print('Começou a dirigir')

carro = Ferrari()
carro.dirigir()
print(carro.velocidadeAtual)