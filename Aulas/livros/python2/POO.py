class Cachorro:
    def __init__(self, nome, idade, cor):
        self.nome = nome
        self.idade = idade
        self.cor = cor
    
    def falar(self, som):
        print(f'{self.nome} disse {som}') # Não é utilizado self.som, pois não é uma variável de init.

    def andar(self, passos):
        print(f'{self.nome} andou {passos} passos')

    def cor(self):
        print(f'{self.nome} é um cachorro de cor {self.cor} muito bonzinho!')

Snoopy = Cachorro('Snoopy', 4, 'branco')
Snoopy.falar('Woof')
Snoopy.andar(96)
print(Snoopy.cor)


# Create a Car class with two instance attributes: .color, which stores the name of the car’s color as a string, and .mileage, which storesthe number of miles on the car as an integer. Then instantiate two Car objects—a blue car with 20,000 miles and a red car with 30,000 miles—and print out their colors and mileage. Your output should look like this:
# The blue car has 20,000 miles.
# The red car has 30,000 miles.

class Carro:
    def __init__(self, cor, km):
        self.cor = cor
        self.km = km
    
    def caracteristica(self):
        print(f'O carro {self.cor} tem {self.km}km.')

blue_car = Carro('azul', 56000)
blue_car.caracteristica()

red_car = Carro('vermelho', 32000)
red_car.caracteristica()