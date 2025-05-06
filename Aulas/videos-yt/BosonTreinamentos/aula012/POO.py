# O tão odiado POO...
class Veiculo:
    def __init__(self, nome, cor, modelo):
        self.nome = nome
        self.cor = cor
        self.modelo = modelo

    def buzinar(self):
        print(f'{self.nome} buzinou!')

Fusca = Veiculo('Fusca', 'Azul', 'RG52')
print(Fusca.nome)
Fusca.buzinar()


# Encapsulamento: elementos privados
class Cachorro:
    def __init__(self, nome, cor):
        self.__nome = nome
        self.__cor = cor
    
    # Getter: acessar os elementos privados
    def get_nome(self):
        print(f'Nome do cachorro: {self.__nome}, cor: {self.__cor}')


    def latir(self):
        print(F'{self.nome} latiu!')

Snoopy = Cachorro('Snoopy', 'Branco')
Snoopy.get_nome()



# Herança
class Animal:
    def __init__(self, nome, cor, comida):
        self.nome = nome
        self.cor = cor
        self.comida = comida

    # É possível criar funções tanto aqui(pre-definidas) tanto na herança!
    def comer(self):
        print(f'{self.nome} está comendo {self.comida}')


class Gato(Animal):
    def andar(self):
        print(f"{self.nome} está andando")


Fluffy = Gato('Fluffy', 'cinza e branco', 'ração de peixe')
Fluffy.comer()
Fluffy.andar()