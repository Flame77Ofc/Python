class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Lucas', 20)
print(f'{p1.nome} tem {p1.idade} anos.')



# Herança
class Animal:
    def __init__(self, name):
        self.name = name

class Cachorro(Animal):
    def speak(self):
        print('Wooooff!!')


Cachorro = Cachorro('Pitbull')
print(Cachorro.name)


