# POO
class Veiculo:
    def movimentar(self):
        print('Sou um veículo e me desloco')

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None

        # Setter
    def num_registro(self, registro):
        self.__num_registro = registro

        # Getter
    def get_fab_modelo(self):
        print(f'{self.__modelo}, {self.__fabricante}')

    def get_num_registro(self):
        return self.__num_registro

if __name__=='__main__':
    meu_veiculo = Veiculo('Fabricante: BGHSA', 'Modelo: Corsa')
    meu_veiculo.movimentar()
    meu_veiculo.get_fab_modelo()
    meu_veiculo.num_registro(490321)
    print(meu_veiculo.get_num_registro())