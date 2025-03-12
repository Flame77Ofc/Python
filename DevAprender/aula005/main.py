class Usuario:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def boas_vindas(self):
        return f'Olá, {self.name}! Seu id é {self.id}'
flame = Usuario('Flame', 1)
print(flame.boas_vindas())