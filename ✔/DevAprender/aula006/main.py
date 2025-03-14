class Pessoa:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def prazer(self):
        if self.age < 18:
            return f"Olá, {self.name}. Infelizmente você não pode entrar pois tem {self.age} anos."
        else:
            return f"Olá, {self.name}. Você pode entrar, tem {self.age} anos."
        
flame = Pessoa('Flame', 18)
print(flame.prazer())

import random
class Celular:
    def __init__(self, marca, cor, modelo):
        self.marca = marca
        self.cor = cor
        self.modelo = modelo

    def caracteristicas(self):
        return f"Caracteristicas do celular: marca {self.marca}, cor {self.cor}, modelo {self.modelo}"
    
    def ligar(self):
        parentes = ['Mãe', 'Pai', 'Vó', 'Tia', 'Tio']
        return f'ligando para... {random.choice(parentes)}'

iphone = Celular('apple', 'branco diamond', '14 PRO')
print(iphone.caracteristicas())
print(iphone.ligar())