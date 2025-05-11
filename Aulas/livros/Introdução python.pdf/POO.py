class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def prazer(self):
        print(f'Prazer, {self.nome}!')
user1 = Pessoa('Gustavo', 23)
user1.prazer()

# Herança
class Carros:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

class Gol(Carros):
    def buzinar(self):
        print(f'Gol {self.nome} buzinou!')

MTX503 = Gol('MTX503', 'vermelho')
MTX503.buzinar()


# Polimorfismo (super)
class Animais:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

class Leopardo(Animais):
    # def __init__(self, nome, cor): Isso não é obrigatório
    #     super().__init__(nome, cor)

    def rugido(self):
        print(f'{self.nome} fez "Warrrrhh"')
prynce = Leopardo('Prynce', 'laranja e preto')
prynce.rugido()



# Encapsulamento: Deixando as variáveis privadas
class Informacoes:
    def __init__(self, nome, idade, cpf):
        self.__nome__ = nome
        self.__idade__ = idade
        self.__cpf__ = cpf